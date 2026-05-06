# Plan: make src/train_SR.py practical on 4x RTX 4090

1. Keep `--batch_size` as global batch size, but lower the default and add a clear per-device printout for distributed launch.
2. Add memory-oriented CLI controls for 24GB GPUs: test batch size, CLIP embedding microbatch size, and evaluation sample limits.
3. Avoid large one-shot evaluation batches by streaming test data in smaller batches and encoding CLIP targets in chunks.
4. Set a safer CUDA allocator default when the user has not configured one externally.
5. Preserve current A100-compatible behavior through overridable arguments, and avoid running training/inference locally because checkpoints/GPU prerequisites are not guaranteed.
6. Validate by static syntax checks only.
