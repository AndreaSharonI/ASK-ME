# Components and what they do

## Hardware (only needed for the final physical Raspberry Pi demonstration)
| Component | What it does | Required? |
|---|---|---|
| Raspberry Pi 4 or 5 (64-bit) | Small computer that runs the local AI model and app | Required for the stated hardware deliverable |
| microSD card (16–32 GB or larger) | Stores Raspberry Pi OS, app files and model/runtime files | Required |
| Compatible USB-C power supply | Powers the Pi | Required |
| HDMI monitor or touchscreen | Displays the study assistant | Optional; a laptop/monitor can be used |
| Keyboard and mouse | Lets the user enter a passage and operate the app | Optional if using SSH/remote access |
| Cooling case/heatsink | Helps manage heat during sustained processing | Recommended |

## Software
| Name | What it does |
|---|---|
| Raspberry Pi OS 64-bit | Operating system for the Raspberry Pi |
| Python 3 | Runs the application logic |
| ExecuTorch | Runs an exported `.pte` AI model locally on supported hardware |
| PyTorch | Used in model preparation/export workflows |
| Git and GitHub | Version control and source-code hosting |
| VS Code | Code editor |

## Current Windows prototype
This starter project uses `google/flan-t5-small` through Hugging Face Transformers to demonstrate passage-to-summary/quiz functionality on Windows. It is a software prototype, not proof of ExecuTorch inference on a Raspberry Pi.
