# agent-skills

A collection of [Hermes Agent](https://hermes-agent.nousresearch.com) skills — procedural
playbooks an agent loads when a matching task comes up.

Written for real use, mostly in German: consumer rights, self-hosting, buying and selling on
classifieds, and a lot of "make an API do what the UI would have done".

## Layout

```
skills/<category>/<skill-name>/
├── SKILL.md            # frontmatter (name, description, tags) + when-to-use + steps + pitfalls
├── references/         # deep-dive notes, address/API tables, schemas
├── templates/          # fill-in-the-blank files (HTML letters, configs, scripts)
└── scripts/            # helper scripts the skill calls
```

One directory per skill, directory name = skill name. Everything a skill needs lives inside
its own folder so it can be copied into a Hermes profile as-is.

## Install

Hermes loads skills from `~/.hermes/skills/`. Clone and link (or copy) a skill:

```bash
git clone https://github.com/kaiffeetasse/agent-skills.git
mkdir -p ~/.hermes/skills/<category>
cp -r agent-skills/skills/<category>/<skill-name> ~/.hermes/skills/<category>/
```

Or use the helper, which symlinks instead of copying (so `git pull` updates the skill):

```bash
./scripts/install-skill.sh legal/dsgvo-werbewiderspruch
```

Then check that Hermes sees it — the skill shows up in `skills_list`. A session that is already
running may need a new one before a freshly linked directory is picked up.

## Skills

**Consumer rights & German law**

| Skill | What it does |
|---|---|
| [`legal/dsgvo-werbewiderspruch`](skills/legal/dsgvo-werbewiderspruch/SKILL.md) | Photo of an advertising letter in, GDPR objection out (Art. 21/17/16/15 DSGVO): reads sender and every reference number, verifies the sender address against the imprint, renders a one-page PDF, mails it to both the data-protection officer and customer service, then verifies the send in the IMAP "Sent" folder. |
| [`legal/immobilien-uebertragung-erbfolge`](skills/legal/immobilien-uebertragung-erbfolge/SKILL.md) | Gifting German real estate to heirs: ErbStG/GrEStG numbers, Pflichtteil, Wohnungsrecht, Pflegeregress (§ 528 BGB), SGB XI — with verified norm values and a checklist for reviewing a draft from the other side's notary. |

**Agent engineering**

| Skill | What it does |
|---|---|
| [`software-development/outbound-automation-guardrails`](skills/software-development/outbound-automation-guardrails/SKILL.md) | Rules for agents that send messages or commit: turn-taking, idempotency, "no promise without a confirmed amount", cost guards, send verification without a response body. |
| [`software-development/delegated-coding-verification`](skills/software-development/delegated-coding-verification/SKILL.md) | Delegating repo changes to coding agents and verifying the result independently instead of trusting the agent's self-report. |
| [`autonomous-ai-agents/opencode-delegation-lessons`](skills/autonomous-ai-agents/opencode-delegation-lessons/SKILL.md) | Delegating coding to the OpenCode CLI via Hermes — what breaks, what to check. |
| [`autonomous-ai-agents/merge-reconciler`](skills/autonomous-ai-agents/merge-reconciler/SKILL.md) | Neutral third-party resolution of conflicting changes from parallel agents. |
| [`productivity/session-librarian`](skills/productivity/session-librarian/SKILL.md) | Organizing an agent's session history: find by prompt, rename, archive, prune. |

**Research & price work**

| Skill | What it does |
|---|---|
| [`ecommerce/marketplace-price-research`](skills/ecommerce/marketplace-price-research/SKILL.md) | Price research with evidence labels — asking vs. sold prices, scam-risk assessment, platform variants. |
| [`ecommerce/secondhand-bulk-lot-sourcing`](skills/ecommerce/secondhand-bulk-lot-sourcing/SKILL.md) | Sourcing cheap bulk/Konvolut lots on classifieds: scan mechanics, per-lot pricing, what kills a deal. |
| [`devops/discount-code-validation`](skills/devops/discount-code-validation/SKILL.md) | Validating shop voucher codes instead of trusting the landing page. |
| [`research/company-registry-research`](skills/research/company-registry-research/SKILL.md) | Who is behind a German company — Handelsregister, Unternehmensregister, imprint chains. |
| [`research/scholarly-publication-verification`](skills/research/scholarly-publication-verification/SKILL.md) | Verifying citations that may not exist: DOI/ISSN checks, predatory-journal detection, full-text retrieval, appraisal. |
| [`research/software-version-archaeology`](skills/research/software-version-archaeology/SKILL.md) | Which version of a program first did X — with explicit evidence levels so dates are never presented as verified when they are guesswork. |

**Everyday chores**

| Skill | What it does |
|---|---|
| [`productivity/shipment-tracking`](skills/productivity/shipment-tracking/SKILL.md) | Track parcels across carriers and answer "where is my package" with real event data. |
| [`productivity/photo-text-extraction`](skills/productivity/photo-text-extraction/SKILL.md) | Exact text from photos of signs/posters via tesseract, including preprocessing that actually helps. |
| [`smart-home/stromzaehler-ablesen-melden`](skills/smart-home/stromzaehler-ablesen-melden/SKILL.md) | Reading a meter from a photo and reporting the value to the German grid operator. |
| [`media/retro-console-tv-connection`](skills/media/retro-console-tv-connection/SKILL.md) | Connecting PS1/PS2/N64/SNES/GameCube/Dreamcast/Xbox to a modern TV — cable classes, scalers, what is worth money. |
| [`automotive/banger-rally-participation`](skills/automotive/banger-rally-participation/SKILL.md) | Checking banger-rally / Carbage-Run eligibility: age, value, TÜV, insurance, required equipment. |

**Datasets & models**

| Skill | What it does |
|---|---|
| [`mlops/image-dataset-classifier-training`](skills/mlops/image-dataset-classifier-training/SKILL.md) | Building an image dataset from web sources and training a small classifier on it. |
| [`mlops/lego-image-recognition`](skills/mlops/lego-image-recognition/SKILL.md) | The same pipeline for LEGO parts, keyless: dataset from a parts catalogue, per-part recognizer. |
| [`data-science/osm-poi-aggregation`](skills/data-science/osm-poi-aggregation/SKILL.md) | Bulk OpenStreetMap/Overpass POI counting and name grouping — chain analysis with spelling/prefix normalization. |

## Conventions

- **No personal data, no credentials, no hostnames.** Anything user-specific goes into a
  `references/*.example.md` template and the real file is git-ignored.
- **Pitfalls are the point.** A skill earns its place by the mistakes it prevents, not by
  restating what the tool documentation already says.
- **No invented results.** Where a step could not be verified live, the skill says so explicitly
  instead of describing a plausible outcome.

## Contributing

Issues and PRs are welcome. Keep the shape: one folder per skill, frontmatter with `name` and
`description`, English or German both fine.

## License

MIT — see [LICENSE](LICENSE).
