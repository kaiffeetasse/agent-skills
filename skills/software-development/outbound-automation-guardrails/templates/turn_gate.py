#!/usr/bin/env python3
"""Kopiervorlage: Am-Zug-Gate + Idempotenz für sendende Automatik.

Zweck: verhindert (a) doppelte Nachrichten, (b) zwei Nachrichten hintereinander ohne Antwort der
Gegenseite, (c) wiederholte Meldungen an den Menschen. Die Funktionen sind bewusst domänenfrei.

Einbau in einen Job:
  1. Zustandsfelder je Konversation/Ziel initialisieren (siehe DEFAULT_FIELDS).
  2. VOR jedem Send:      allowed, why, is_followup = turn_state(st, event_id, kind)
     und zusätzlich den Text-Fingerprint prüfen (already_sent).
  3. NACH jedem Send:     record_outbound(st, event_id, now, is_followup)
  4. Für Meldungen an den Menschen: once_only(st, 'escalated_for', event_id).
Auf ALLEN Sendestellen anwenden — Antwort, Absage, Nachfassen, Ausspielen, Fixierung, Rücknahme,
Benachrichtigung. Ein Guard nur auf dem Hauptpfad ist ein Leck.
"""
from __future__ import annotations

import hashlib
import re
from datetime import datetime

# --- Konfiguration (per Umgebungsvariable übersteuerbar) ---------------------
FOLLOWUP_AFTER_H = 24.0     # Funkstille, nach der genau EIN Nachfassen erlaubt ist
MIN_TURN_GAP_MIN = 5.0      # Mindestabstand zwischen zwei eigenen Sendungen

DEFAULT_FIELDS = {
    'replied': {},              # event_id -> Zeitpunkt
    'sent_fingerprints': {},    # text_hash -> Zeitpunkt
    'last_outbound_at': None,
    'awaiting_reply_for': None, # event_id, auf die wir zuletzt geantwortet haben
    'awaiting_since': None,
    'followup_for': None,       # event_id, für die das Nachfassen raus ist
    'escalated_for': None,      # event_id, für die der Mensch schon informiert wurde
}


def minutes_since(iso, now=None):
    if not iso:
        return None
    now = now or datetime.now()
    try:
        return (now - datetime.fromisoformat(str(iso))).total_seconds() / 60.0
    except Exception:
        return None


def hours_since(iso, now=None):
    m = minutes_since(iso, now)
    return None if m is None else m / 60.0


def outbound_fingerprint(text):
    """Normalisierte Text-ID: derselbe Text darf je Konversation nur einmal raus."""
    normalized = re.sub(r'\s+', ' ', (text or '').strip().casefold())
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()[:24]


def already_sent(st, text):
    return outbound_fingerprint(text) in (st.get('sent_fingerprints') or {})


def turn_state(st, event_id, now=None, kind='reply'):
    """Sind wir am Zug?  -> (erlaubt, grund, ist_nachfassen)

    kind='reply'   : nur bei neuer Nachricht der Gegenseite ODER einmaligem Nachfassen nach
                     FOLLOWUP_AFTER_H Stunden Funkstille.
    kind='nudge'   : einmaliger Zug pro Ereignis (z. B. Ausspielen/Rücknahme), ohne Zeitzwang.
    """
    now = now or datetime.now()

    if not st.get('last_outbound_at'):
        return True, 'erste Nachricht', False

    # Neue Nachricht der Gegenseite -> zügig antworten (keine Mindestpause: sie hat eröffnet).
    if event_id and event_id != st.get('awaiting_reply_for'):
        return True, 'neue Nachricht der Gegenseite', False

    # Ab hier: keine neue Nachricht -> wir wären doppelt am Zug.
    gap = minutes_since(st.get('last_outbound_at'), now)
    if gap is not None and gap < MIN_TURN_GAP_MIN:
        return False, f'erst {gap:.0f} min seit unserer letzten Nachricht', False

    if st.get('followup_for') and st.get('followup_for') == event_id:
        return False, 'Nachfassen zu diesem Ereignis schon gesendet', False

    if kind == 'nudge':
        return True, f'{kind}: einmalig pro Ereignis', True

    hrs = hours_since(st.get('awaiting_since'), now) or 0.0
    if hrs >= FOLLOWUP_AFTER_H:
        return True, f'einmaliges Nachfassen nach {hrs:.0f} h Funkstille', True
    return False, (f'warten auf Antwort ({hrs:.1f} h; Nachfassen ab {FOLLOWUP_AFTER_H:.0f} h)'), False


def record_outbound(st, event_id, now=None, followup=False):
    """NACH jedem erfolgreichen Send aufrufen."""
    now = (now or datetime.now()).isoformat(timespec='seconds')
    st['last_outbound_at'] = now
    st['awaiting_since'] = now
    st['awaiting_reply_for'] = event_id
    if followup:
        st['followup_for'] = event_id
    else:
        st.pop('followup_for', None)   # neuer Zug -> Nachfassen wieder frei


def once_only(st, field, event_id):
    """Einmal-Sperre für Meldungen an den Menschen. True = jetzt melden (und verbuchen)."""
    if st.get(field) == event_id:
        return False
    st[field] = event_id
    return True


def migrate_legacy(st, last_replied_event_id, last_replied_at):
    """Nach Einführung der Gate-Felder einmalig aufrufen.

    Ohne Migration ist das Gate für Altfälle ein No-Op: `awaiting_reply_for` bleibt leer, jedes
    alte Ereignis gilt als neu, und der Job antwortet/escaliert endlos.
    """
    if (st.get('replied') or {}) and not st.get('awaiting_reply_for'):
        st['awaiting_reply_for'] = last_replied_event_id
        st['awaiting_since'] = last_replied_at
        st['last_outbound_at'] = last_replied_at
    return st


# --- Beispiel-Reihenfolge an einer Sendestelle ---------------------------------
def send_guarded(st, event_id, text, transport, now=None, kind='reply'):
    """Erlaubt-Schema. transport(text) ist der echte Sendeaufruf."""
    allowed, why, is_followup = turn_state(st, event_id, now=now, kind=kind)
    if not allowed:
        return False, f'nicht gesendet: {why}'
    if already_sent(st, text):
        return False, 'nicht gesendet: identischer Text bereits raus'
    if (st.get('replied') or {}).get(event_id) and not is_followup:
        return False, 'nicht gesendet: Ereignis bereits beantwortet'
    transport(text)
    st.setdefault('replied', {})[event_id] = (now or datetime.now()).isoformat(timespec='seconds')
    st.setdefault('sent_fingerprints', {})[outbound_fingerprint(text)] = st['replied'][event_id]
    record_outbound(st, event_id, now=now, followup=is_followup)
    return True, 'gesendet'
