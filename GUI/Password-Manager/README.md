# Password Manager

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-2C3E50?style=flat-square)](https://docs.python.org/3/library/tkinter.html)
[![pyperclip](https://img.shields.io/badge/pyperclip-1.11+-4B8BBE?style=flat-square)](https://pypi.org/project/pyperclip/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-0078D4?style=flat-square)]()


A lightweight desktop app for generating strong passwords and saving login details locally. Built with **Python** and **Tkinter** as part of [100 Days of Code](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu.

---

## About

Password Manager gives you a small GUI to:

- Create random passwords (letters, numbers, symbols)
- Copy them to the clipboard in one click
- Store website, email, and password entries in a text file

It is meant for practice with GUI programming, file I/O, and user input—not as a replacement for a real password vault.

---

## Features

| Feature | Description |
|--------|-------------|
| Password generator | 8–10 letters, 2–4 numbers, 2–4 symbols, shuffled (~12–18 chars) |
| Clipboard integration | New password copied via `pyperclip` after each generate |
| Credential storage | Entries appended to `data.txt` as `website \| email \| password` |
| Input validation | Error dialog if any field is empty |
| Save confirmation | OK/Cancel dialog shows values before writing to disk |
| Field reset | Website and password cleared after a successful save |

---

## Tech stack

- **Python 3**
- **Tkinter** — window, labels, entries, buttons, canvas
- **pyperclip** — clipboard access
- **random** — `choice`, `randint`, `shuffle` for password generation

---

## Installation

### Prerequisites

- Python 3.8+ recommended
- Tkinter (usually bundled with Python on Windows)
- `pyperclip`

### Steps

1. **Get the project** — clone or download this folder.

2. **Open a terminal** in the project directory:

   ```text
   Password-Manager/
   ```

3. **(Recommended) Virtual environment**

   ```bash
   python -m venv .venv
   ```

   Activate it:

   | OS | Command |
   |----|---------|
   | Windows (PowerShell) | `.\.venv\Scripts\Activate.ps1` |
   | Windows (CMD) | `.venv\Scripts\activate.bat` |
   | macOS / Linux | `source .venv/bin/activate` |

4. **Install dependency**

   ```bash
   pip install pyperclip
   ```

5. **Run the app** — must be started from the project folder so `logo.png` and `data.txt` resolve correctly:

   ```bash
   python main.py
   ```

---

## Usage

1. Launch with `python main.py`.
2. Enter a **website** (e.g. `github.com`) and **email**.
3. Either:
   - Click **Generate Password** — fills the password field and copies to clipboard (replaces any previous password in the field), or
   - Type your own password manually.
4. Click **Add**.
5. Review the confirmation dialog; click **OK** to save or **Cancel** to abort.
6. On save, website and password fields clear; email stays for the next entry.

### Example `data.txt` line

```text
github.com | you@example.com | aB3!xK9mP2vLq
```

---

## Project structure

```text
Password-Manager/
├── main.py       # UI, password generator, save logic
├── logo.png      # Logo shown in the window (required)
├── data.txt      # Saved credentials (plain text, append-only)
├── README.md
└── .venv/        # Optional local virtual environment
```

---

## How it works (brief)

- **`gen_pass()`** — Builds character lists, shuffles them, updates the password entry, copies to clipboard.
- **`save()`** — Reads the three fields, validates, asks for confirmation, appends one line to `data.txt`, then clears website and password fields.
- **UI** — `Tk()` window with `grid` layout: logo canvas, three labeled entries, Generate and Add buttons.

---

## Troubleshooting

| Problem | What to try |
|--------|-------------|
| `logo.png` not found | Run `python main.py` from the `Password-Manager` folder, not a parent directory. |
| Clipboard does not work | Install `pyperclip`: `pip install pyperclip`. On Linux you may need `xclip` or `xsel`. |
| Empty or missing `data.txt` | Normal on first run; the file is created/updated when you save an entry. |
| Tkinter missing | Reinstall Python with Tcl/Tk enabled, or install `python3-tk` on Linux. |

---

## Security notice

Credentials are stored in **plain text** in `data.txt` on your machine. There is no encryption, master password, or search/load UI in this version.

**Do not** rely on this app for real high-value accounts. Treat `data.txt` as sensitive and avoid committing it to public Git repositories.

---

## Possible next steps

Ideas if you extend the project beyond the course baseline:

- Search by website and auto-fill fields
- JSON or encrypted storage (`cryptography` / Fernet)
- Mask password input with `show="*"`
- `requirements.txt` and paths relative to the script file

---

## Acknowledgments

Project structure and concepts from **Dr. Angela Yu's** [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/).
