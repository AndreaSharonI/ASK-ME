# Offline Smart Learning Assistant

**AI for Inclusive Education — software prototype**

This project demonstrates how an educational passage can be turned into:
- A short, student-friendly summary.
- Three multiple-choice quiz questions with answers.

## Learning barrier
Students in low-connectivity or underserved areas may not have reliable access to online study support.

## Target learners
School students in rural and low-connectivity communities.

## Current implementation status
This repository contains a **Windows software prototype**. It uses the small `google/flan-t5-small` model through Hugging Face Transformers. The model is downloaded the first time the app runs and is cached locally; subsequent generation can run offline if the model files are available.

**This is not yet the mandatory Raspberry Pi + ExecuTorch demonstration.** The final hackathon requirement must be completed on a Raspberry Pi using an approved ExecuTorch `.pte` model and runtime. See `docs/executorch_next_steps.md`.

## Run on Windows 11

1. Install Python 3.10 or later (64-bit).
2. Open this folder in VS Code.
3. Open Terminal → New Terminal.
4. Create a virtual environment:

   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

5. Install the packages:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Run the app:

   ```powershell
   python app/main.py
   ```

7. On the first run, keep internet available so the model can be downloaded. After it is cached, try the app offline.

## Project files

- `app/main.py` — graphical app, local model loading, summary and quiz generation.
- `data/sample_passage.txt` — sample educational passage.
- `docs/components.md` — hardware and software component list.
- `docs/executorch_next_steps.md` — path to the required ExecuTorch deployment.
- `requirements.txt` — Python dependencies.

## Suggested GitHub description
An offline-first educational assistant prototype that transforms study passages into simple summaries and quiz questions, designed for low-connectivity learning environments.
