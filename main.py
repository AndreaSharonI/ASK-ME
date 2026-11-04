"""
Offline Smart Learning Assistant — Windows prototype
Uses a small local Hugging Face model. The model downloads once on first run;
after it is cached, inference can run without internet.
This is NOT the Raspberry Pi + ExecuTorch deployment build.
"""
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_ID = "google/flan-t5-small"
tokenizer = None
model = None

SAMPLE_PASSAGE = """The water cycle is the continuous movement of water on, above,
and below the Earth's surface. The Sun heats water in oceans, lakes, and rivers,
causing some of it to evaporate into water vapour. As the vapour rises, it cools
and condenses into tiny droplets that form clouds. When the droplets become
heavy, water falls back to Earth as precipitation, such as rain. Water then
collects in rivers, lakes, and oceans, and the cycle begins again. This natural
process helps distribute fresh water and supports plants, animals, and people."""

def load_model():
    global tokenizer, model
    if model is None:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID)
        model.eval()

def generate_text(prompt, max_new_tokens):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    with torch.inference_mode():
        output = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            num_beams=2
        )
    return tokenizer.decode(output[0], skip_special_tokens=True).strip()

def create_study_aid(passage):
    summary_prompt = (
        "Explain the following educational passage in simple language for a school student. "
        "Write a short summary in 3 to 5 sentences:\n\n" + passage
    )
    quiz_prompt = (
        "Create exactly 3 short multiple-choice quiz questions based only on this passage. "
        "Give four options (A, B, C, D) and show the correct answer after each question. "
        "Use simple language:\n\n" + passage
    )
    summary = generate_text(summary_prompt, 120)
    quiz = generate_text(quiz_prompt, 240)
    return summary, quiz

def start_generation():
    passage = passage_box.get("1.0", tk.END).strip()
    word_count = len(passage.split())
    if not passage:
        messagebox.showwarning("Passage needed", "Please enter an educational passage.")
        return
    if not 150 <= word_count <= 300:
        messagebox.showwarning(
            "Passage length",
            f"The hackathon asks for approximately 150–300 words. Your passage has {word_count} words."
        )
        return

    generate_button.config(state=tk.DISABLED)
    status_label.config(text="Loading the local AI model / generating study aids...")
    result_box.delete("1.0", tk.END)

    def worker():
        try:
            load_model()
            summary, quiz = create_study_aid(passage)
            result = f"SUMMARY\n{'-'*55}\n{summary}\n\nQUIZ QUESTIONS\n{'-'*55}\n{quiz}"
            root.after(0, lambda: show_result(result))
        except Exception as exc:
            root.after(0, lambda: show_error(str(exc)))

    threading.Thread(target=worker, daemon=True).start()

def show_result(result):
    result_box.insert(tk.END, result)
    status_label.config(text="Finished. Model inference ran locally on this computer.")
    generate_button.config(state=tk.NORMAL)

def show_error(error):
    status_label.config(text="Could not generate the study aids.")
    generate_button.config(state=tk.NORMAL)
    messagebox.showerror(
        "Model error",
        f"{error}\n\nCheck the installation and internet connection for the first model download."
    )

root = tk.Tk()
root.title("Offline Smart Learning Assistant — Windows Prototype")
root.geometry("950x760")
root.minsize(760, 600)

title = tk.Label(root, text="Offline Smart Learning Assistant",
                 font=("Segoe UI", 20, "bold"), fg="#173B70")
title.pack(pady=(14, 2))
subtitle = tk.Label(root, text="Simple summaries • Quiz questions • Local AI prototype",
                    font=("Segoe UI", 10), fg="#555555")
subtitle.pack(pady=(0, 12))

tk.Label(root, text="Enter an educational passage (150–300 words):",
         font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=18)
passage_box = scrolledtext.ScrolledText(root, height=12, wrap=tk.WORD,
                                        font=("Segoe UI", 10))
passage_box.pack(fill=tk.BOTH, expand=False, padx=18, pady=8)
passage_box.insert("1.0", SAMPLE_PASSAGE)

generate_button = tk.Button(
    root, text="Generate Summary & Quiz", command=start_generation,
    bg="#1769D2", fg="white", activebackground="#0F55B0",
    font=("Segoe UI", 11, "bold"), padx=16, pady=8
)
generate_button.pack(pady=8)

status_label = tk.Label(root, text="Ready. First run needs internet to download the model.",
                        font=("Segoe UI", 9), fg="#555555")
status_label.pack(pady=4)

tk.Label(root, text="Generated study aids:",
         font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=18)
result_box = scrolledtext.ScrolledText(root, height=15, wrap=tk.WORD,
                                       font=("Consolas", 10))
result_box.pack(fill=tk.BOTH, expand=True, padx=18, pady=(6, 16))

root.mainloop()
