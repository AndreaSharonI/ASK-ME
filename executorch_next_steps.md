# ExecuTorch deployment: next steps

The current `app/main.py` is a Windows prototype using Hugging Face Transformers. Do not describe it as an ExecuTorch build.

For the actual hackathon hardware requirement, follow the current official ExecuTorch Raspberry Pi tutorial:
https://docs.pytorch.org/executorch/stable/raspberry_pi_llama_tutorial.html

The official tutorial currently describes:
- A Linux x86-64 development host.
- Python 3.10–3.14.
- Raspberry Pi 4 or Raspberry Pi 5 with a 64-bit OS.
- Exporting a supported Llama-family model to `.pte`.
- Deploying the runner, runtime libraries, tokenizer and `.pte` model to the Pi.

ExecuTorch supports a documented list of LLM families; check the current official export documentation before choosing a model:
https://docs.pytorch.org/executorch/stable/llm/export-llm.html

Important:
1. The model and runtime must match the selected export/backend.
2. The Windows prototype's FLAN-T5 model is not the ExecuTorch model for the Pi deployment.
3. Do not report Raspberry Pi inference time, model memory use, or offline Pi operation until those have actually been measured on the device.
4. For the hackathon, process the organiser-provided passage and keep the result evidence, timing, model name and model size.
