# Repository Guidelines

## Project Structure & Module Organization
Core NeuroClips code lives in `src/` (training, reconstruction, captioning, utilities). The main entry scripts are `src/train_SR.py`, `src/train_PR.py`, `src/recon_keyframe.py`, and `src/recon_blurry.py`.  
The video generation backend is vendored in `Animatediff/` (configs, pipelines, training/inference scripts).  
Data preprocessing assets and MATLAB pipelines are under `preprocess/`.  
Static figures and demo outputs are under `assets/` and `Animatediff/__assets__/`.

## Build, Test, and Development Commands
- `bash src/setup.sh`: creates and installs the `neuroclips` Python environment.
- `bash model_download.sh`: downloads required checkpoints.
- `python src/train_SR.py --subj 1 ...`: train Semantic Reconstructor (backbone/prior variants).
- `python src/train_PR.py --subj 1 ...`: train Perception Reconstructor.
- `python src/recon_keyframe.py --subj 1`: reconstruct keyframes.
- `python src/recon_blurry.py --subj 1`: reconstruct blurry video guidance.
- `cd Animatediff && python -m scripts.neuroclips --config configs/NeuroClips/control.yaml`: run final video reconstruction.
- `cd src/generative_models && pytest -v tests/inference/test_inference.py`: run packaged inference tests.

## Coding Style & Naming Conventions
Use Python 3.10+ style with 4-space indentation, `snake_case` for functions/files, and `PascalCase` for classes (for example, `Perception.py`, `Semantic.py`). Keep CLI scripts thin and move reusable logic into modules.  
No repo-wide formatter config is committed at root; follow PEP 8 and keep imports grouped consistently. If introducing formatting/lint tooling, scope it per submodule and document it in that submodule README.

## Testing Guidelines
Primary automated tests currently exist in `src/generative_models/tests/` and run with `pytest`. Use `test_*.py` naming and keep inference-heavy tests marked appropriately (see `pytest.ini` marker `inference`).  
For `src/` training/reconstruction scripts, add lightweight smoke checks when possible (argument parsing, single-batch dry runs) and document required data paths in PRs.

## Environment Constraints (Important)
Do not run training, reconstruction, or inference commands in this repository unless the required model weights and GPU environment are already prepared. This project depends on large checkpoint downloads and CUDA-capable hardware.  
For contributors without these prerequisites, code changes can be reviewed statically only; local execution and test runs are not required.

## Commit & Pull Request Guidelines
Recent history uses short, imperative commits (`Update README.md`, `Update train_PR.py`). Prefer: `<area>: <imperative summary>` (example: `src: fix subject ID handling in recon_keyframe`).  
PRs should include:
- What changed and why.
- Exact commands run (train/test/inference).
- Data/checkpoint assumptions.
- Before/after artifacts for reconstruction changes (GIFs or keyframes).
- Linked issue or experiment note when applicable.
