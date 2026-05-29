# ⚙️ Automation

A collection of small **Python automation** projects — scripts that run on a schedule (or on demand) to handle repetitive tasks without manual work.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/focus-scheduled%20tasks-22C55E?style=flat" alt="Scheduled tasks"/>
  <img src="https://img.shields.io/badge/projects-1-8B5CF6?style=flat" alt="1 project"/>
</p>

---

## 📂 Folder structure

```
Automation/
├── README.md                 # You are here
└── Birthday-Wisher/          # Automated birthday emails
    ├── main.py
    ├── birthdays.csv
    ├── requirements.txt
    ├── letter_templates/
    └── README.md             # Full setup & usage guide
```

Each project lives in its own subfolder with its own `README.md`, dependencies, and config.

---

## 🚀 Projects

| Project | Description | Docs |
|---------|-------------|------|
| [**Birthday Wisher**](./Birthday-Wisher/) | Checks `birthdays.csv` daily and sends a personalized Gmail when someone has a birthday today | [README](./Birthday-Wisher/README.md) |

---

## 🏁 Getting started

1. Open the project folder you want (e.g. `Birthday-Wisher/`).
2. Follow that project’s **README** for install, `.env` setup, and how to run or schedule it.

**Example — Birthday Wisher:**

```bash
cd Birthday-Wisher
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
python main.py
```

See [Birthday-Wisher/README.md](./Birthday-Wisher/README.md) for Gmail App Password setup, CSV format, Task Scheduler / cron, and troubleshooting.

---

## ➕ Adding a new automation

1. Create a new folder under `Automation/` (e.g. `My-New-Script/`).
2. Add `main.py` (or your entry script), `requirements.txt`, and a project `README.md`.
3. Add a row to the **Projects** table above.

---

<p align="center">
  Small scripts, less busywork.
</p>
