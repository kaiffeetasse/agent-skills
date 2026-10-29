# Portable GPU handoff workflow (LEGO dataset project)

This is a reusable handoff pattern based on a local image dataset/classifier project of roughly 147k manifest rows and 12.5 GB. It is not a guarantee that a new GPU run will match prior metrics.

## 1. Audit before documenting

Check the actual tree and sizes; manifest path conventions; checkpoint fields/model architecture; CLI help; imports/dependencies; developer-specific paths; and actual GPU availability. Search all scripts for home/workspace literals. Make roots relative to `__file__`, then compile and invoke help before giving target-machine commands.

## 2. Keep code and data boundaries clear

If large images, manifests, caches and weights are ignored by Git, state prominently that a Git checkout does not include them. For a local-only handoff, copy the entire working directory, including ignored files, and do not configure a remote or push. Keep third-party notices separate from the original-code licence; public CDN access does not grant bulk redistribution permission.

## 3. Inventory and checksums

Generate `BUNDLE_INVENTORY.json` and `SHA256SUMS.txt` on the source using a deterministic local filesystem walk, streaming SHA256 in bounded chunks. Exclude `.git`, virtual environments, bytecode, transient logs and the inventory files themselves. Copy those source inventory files alongside the complete directory. On the destination run comparison mode against the copied source inventory; do not regenerate it on the destination first, or the reference is overwritten. Compare relative path set, byte lengths and hashes. Git cleanliness and asset integrity are separate checks.

## 4. Target-GPU setup

1. Install/check the NVIDIA driver (`nvidia-smi`).
2. Create and activate a fresh Python virtual environment.
3. Install torch/torchvision using the official PyTorch selector for OS, Python, driver and supported CUDA runtime. Do not guess wheel URLs.
4. Install other pinned/project dependencies.
5. Verify `torch.cuda.is_available()`, `torch.version.cuda`, and the device name.
6. Run a tiny one-epoch smoke test, then load that exact checkpoint through the real inference CLI.
7. Only after that, scale resolution, batch size and workers while watching VRAM/throughput.

CPU smoke tests demonstrate CPU plumbing only. Mark CUDA as unverified until it has run on a CUDA device.

## 5. Fine-tuning safeguards

- Keep views/near-duplicates of the same part-colour group out of separate validation/test splits; for domain generalization, hold out an actual source/domain.
- Freeze a test set that is not used for model selection. Record seed, vocabulary, preprocessing, source composition, split IDs, library/CUDA versions and GPU model.
- With very sparse part-colour labels, evaluate separate part and colour heads as well as any joint head. Report exact joint top-k separately from marginal task scores.
- Use AMP as appropriate; CUDA batch size depends on resolution, architecture and VRAM. On OOM, reduce batch size or use gradient accumulation/checkpointing rather than silently dropping data.
- Save validation-best weights separately from a last/recovery checkpoint and write metrics/config beside the weights.
- Keep tasks restartable and log unbuffered progress. Batch validation and kNN operations: a full validation×training similarity matrix can exceed GPU/host RAM.
- Handle smoke runs with no validation rows explicitly: fail fast or mark and save a train-loss fallback. Always test checkpoint reload through inference.

## 6. End-to-end handoff checks

- `python -m py_compile scripts/*.py`
- run new training script `--help` and inference `--help`;
- tiny training run creates expected checkpoint and metrics;
- inference CLI loads that exact checkpoint on an included sample image;
- transfer SHA256 inventory passes;
- Git status reviewed and `git remote -v` empty if local-only was requested;
- report what was and was not verified, especially CUDA execution and data terms.

Never tell a user to transfer only a Git clone if ignored data is required.

## Example commands

```bash
nvidia-smi
python - <<'PY'
import torch
print(torch.__version__, torch.version.cuda, torch.cuda.is_available())
if torch.cuda.is_available(): print(torch.cuda.get_device_name(0))
PY

python scripts/finetune_multitask.py --device cuda --backbone resnet18 \
  --size 160 --epochs 1 --batch-size 16 --workers 2 \
  --max-images 256 --min-class-images 1 --run-name smoke_cuda
python scripts/recognize_multitask.py --image samples/elements_3020_15.jpg \
  --checkpoint models/finetuned/smoke_cuda.best.pt --device cuda --topk 3
python scripts/make_inventory.py --check
```

A capped smoke dataset may have no validation rows. Treat it as a plumbing test only; check that the checkpoint and metrics exist, and do not use it to report accuracy.
