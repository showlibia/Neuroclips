Read and execute below with ultrathink

## Goal Tracker Setup (REQUIRED FIRST STEP)

Before starting implementation, you MUST initialize the Goal Tracker:

1. Read @/home/matrix/Neuroclips/.humanize/rlcr/2026-05-07_02-47-59/goal-tracker.md
2. If the "Ultimate Goal" section says "[To be extracted...]", extract a clear goal statement from the plan
3. If the "Acceptance Criteria" section says "[To be defined...]", define 3-7 specific, testable criteria
4. Populate the "Active Tasks" table with tasks from the plan, mapping each to an AC
5. Write the updated goal-tracker.md

**IMPORTANT**: The IMMUTABLE SECTION can only be modified in Round 0. After this round, it becomes read-only.

---

## Implementation Plan

For all tasks that need to be completed, please use the Task system (TaskCreate, TaskUpdate, TaskList) to track each item in order of importance.
You are strictly prohibited from only addressing the most important issues - you MUST create Tasks for ALL discovered issues and attempt to resolve each one.

# Plan: make src/train_SR.py practical on 4x RTX 4090

1. Keep `--batch_size` as global batch size, but lower the default and add a clear per-device printout for distributed launch.
2. Add memory-oriented CLI controls for 24GB GPUs: test batch size, CLIP embedding microbatch size, and evaluation sample limits.
3. Avoid large one-shot evaluation batches by streaming test data in smaller batches and encoding CLIP targets in chunks.
4. Set a safer CUDA allocator default when the user has not configured one externally.
5. Preserve current A100-compatible behavior through overridable arguments, and avoid running training/inference locally because checkpoints/GPU prerequisites are not guaranteed.
6. Validate by static syntax checks only.

---

## Goal Tracker Rules

Throughout your work, you MUST maintain the Goal Tracker:

1. **Before starting a task**: Mark it as "in_progress" in Active Tasks
2. **After completing a task**: Move it to "Completed and Verified" with evidence (but mark as "pending verification")
3. **If you discover the plan has errors**:
   - Do NOT silently change direction
   - Add entry to "Plan Evolution Log" with justification
   - Explain how the change still serves the Ultimate Goal
4. **If you need to defer a task**:
   - Move it to "Explicitly Deferred" section
   - Provide strong justification
   - Explain impact on Acceptance Criteria
5. **If you discover new issues**: Add to "Open Issues" table

---

Note: You MUST NOT try to exit `start-rlcr-loop` loop by lying or edit loop state file or try to execute `cancel-rlcr-loop`

After completing the work, please:
0. If you have access to the `code-simplifier` agent, use it to review and optimize the code you just wrote
1. Finalize @/home/matrix/Neuroclips/.humanize/rlcr/2026-05-07_02-47-59/goal-tracker.md (this is Round 0, so you are initializing it - see "Goal Tracker Setup" above)
2. Commit your changes with a descriptive commit message
3. Write your work summary into @/home/matrix/Neuroclips/.humanize/rlcr/2026-05-07_02-47-59/round-0-summary.md
