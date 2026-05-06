# Goal Tracker

<!--
This file tracks the ultimate goal, acceptance criteria, and plan evolution.
It prevents goal drift by maintaining a persistent anchor across all rounds.

RULES:
- IMMUTABLE SECTION: Do not modify after initialization
- MUTABLE SECTION: Update each round, but document all changes
- Every task must be in one of: Active, Completed, or Deferred
- Deferred items require explicit justification
-->

## IMMUTABLE SECTION
<!-- Do not modify after initialization -->

### Ultimate Goal
Make `src/train_SR.py` practical to launch on 4x RTX 4090 without the CUDA OOM behavior seen when moving from a single A100, while preserving overridable settings for larger-memory GPUs.

Source plan: .humanize/plans/train_sr_4x4090_plan.md

### Acceptance Criteria
<!-- Each criterion must be independently verifiable -->

AC1. `--batch_size` is treated and documented as a global batch size, with a conservative 4x4090-friendly default and clear per-device logging.
AC2. The script exposes CLI controls for memory-sensitive training/evaluation behavior: test batch size, CLIP embedding microbatch size, and optional evaluation sample limits.
AC3. Evaluation no longer processes hundreds of images through OpenCLIP in one CUDA pass by default.
AC4. CUDA allocator behavior is configured conservatively only when the user has not already set `PYTORCH_CUDA_ALLOC_CONF`.
AC5. Existing A100-style behavior remains available through CLI overrides rather than hard-coded removal.
AC6. Changes are validated with static syntax checks only; no training, reconstruction, or inference commands are run.

---

## MUTABLE SECTION
<!-- Update each round with justification for changes -->

### Plan Version: 1 (Updated: Round 0)

#### Plan Evolution Log
<!-- Document any changes to the plan with justification -->
| Round | Change | Reason | Impact on AC |
|-------|--------|--------|--------------|
| 0 | Initial plan | - | - |

#### Active Tasks
<!-- Map each task to its target Acceptance Criterion -->
| Task | Target AC | Status | Notes |
|------|-----------|--------|-------|

### Completed and Verified
<!-- Only move tasks here after Codex verification -->
| AC | Task | Completed Round | Verified Round | Evidence |
|----|------|-----------------|----------------|----------|
| AC1-AC6 | Initialize RLCR goal tracker | 0 | pending | Goal, acceptance criteria, and task mapping initialized in this file. |
| AC1, AC5 | Lower/default global batch and improve distributed logging | 0 | pending | `src/train_SR.py` default `--batch_size` is 8 and logs global/per-device/test/CLIP microbatch settings. |
| AC2, AC5 | Add memory-control CLI flags | 0 | pending | Added `--test_batch_size`, `--clip_microbatch_size`, and `--eval_max_samples`. |
| AC3 | Chunk CLIP evaluation and reduce default test batch | 0 | pending | Replaced one-shot OpenCLIP calls with `embed_clip_images()` chunking and changed test DataLoader default from 300 to 40. |
| AC4 | Add conservative allocator default | 0 | pending | Added `os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")` before torch import. |
| AC6 | Run static verification only | 0 | pending | `python -m py_compile src/train_SR.py` passed; no training/inference commands run. |

### Explicitly Deferred
<!-- Items here require strong justification -->
| Task | Original AC | Deferred Since | Justification | When to Reconsider |
|------|-------------|----------------|---------------|-------------------|

### Open Issues
<!-- Issues discovered during implementation -->
| Issue | Discovered Round | Blocking AC | Resolution Path |
|-------|-----------------|-------------|-----------------|
