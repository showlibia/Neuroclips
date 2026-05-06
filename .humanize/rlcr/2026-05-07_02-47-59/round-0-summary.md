# Round 0 Summary

## What was implemented
- Updated `src/train_SR.py` defaults for 4x RTX 4090: `--batch_size` now defaults to global batch 8, which resolves to 2 samples per GPU under 4-process distributed training.
- Added memory controls:
  - `--test_batch_size` default 40, replacing the previous hard-coded evaluation batch of 300.
  - `--clip_microbatch_size` default 4, used to chunk OpenCLIP ViT-bigG image embedding calls during training and evaluation.
  - `--eval_max_samples` default 0, allowing optional evaluation truncation while preserving full evaluation by default.
- Added validation for invalid memory-control arguments.
- Added a conservative CUDA allocator default with `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` only when the user has not set it externally.
- Fixed evaluation loss averaging to use the configured number of test batches instead of the old hard-coded `/4` divisor.
- Restricted best-checkpoint selection to rank 0, matching the existing rank-0-only evaluation behavior.
- Made small-batch blurry reconstruction sampling safe by ensuring at least one sample is selected.

## Files created/modified
- Modified: `src/train_SR.py`
- Created/tracked plan: `.humanize/plans/train_sr_4x4090_plan.md`
- Updated RLCR tracker: `.humanize/rlcr/2026-05-07_02-47-59/goal-tracker.md`
- Added summary: `.humanize/rlcr/2026-05-07_02-47-59/round-0-summary.md`

## Tests added/passed
- Passed: `python -m py_compile src/train_SR.py`

## Commands intentionally not run
- Did not run training, reconstruction, or inference commands because AGENTS.md says not to run them unless checkpoint and GPU prerequisites are already prepared.

## Remaining items
- No known remaining implementation items. Runtime validation on the target 4x4090 machine is still required to choose final values if `--use_prior` or `--blurry_recon` still needs smaller microbatches.
