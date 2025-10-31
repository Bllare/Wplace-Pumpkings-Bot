# 🎃 WPlace Auto Claimer Bot

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)]()
[![Selenium](https://img.shields.io/badge/Automation-Selenium-orange.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

> 🧩 Automatically claims **pumpkins** on [wplace.live](https://wplace.live)  
> Supports multiple accounts, threading, and live pumpkin fetching.

---

## ⚡ Features
- 🔁 Auto-updates pumpkin URLs  
- 🧑‍🤝‍🧑 Multi-account support (`accounts.txt`)  
- 🧠 Skips claimed tiles (`claimed.json`)  
- ⚙️ Configurable delays (`config.json`)  
- 🧵 Threaded for speed  

---

## 🚀 Quick Start

```bash
git clone https://github.com/Bllare/Wplace-Pumpkings-Bot.git
cd Wplace-Pumpkings-Bot
pip install selenium requests
````

Add your tokens in:

```
accounts.txt
```

Then run:

```bash
python main.py
```

---

## 📂 Files

| File              | Description                    |
| ----------------- | ------------------------------ |
| `main.py`         | Main bot logic                 |
| `extract_urls.py` | Fetches & updates pumpkin URLs |
| `config.json`     | Config (threads, delay, etc.)  |
| `claimed.json`    | Saves claimed pumpkins         |
| `accounts.txt`    | Account tokens (one per line)  |

---

## 🪪 License & Credits

**© 2025 [Bllare](https://github.com/Bllare)** — MIT License
If you use or modify this code, **credit is required** in your README or source.

> Made with ☕ + 🎃 + 💻 — for research and educational purposes only.
