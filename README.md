# 🎃 WPlace Auto Claimer Bot

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-3910)
[![Selenium](https://img.shields.io/badge/Automation-Selenium-orange.svg)](https://www.selenium.dev)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/Bllare/Wplace-Pumpkings-Bot/blob/main/LICENSE)

> 🧩 Automatically claims **pumpkins** on [wplace.live](https://wplace.live)  
> Supports multiple accounts, threading, and live pumpkin fetching.

---

## ⚡ Features
- 🔁 Auto-updates pumpkin URLs  
- 🧑‍🤝‍🧑 Multi-account support (`accounts.txt`)  
- 🧠 Skips already claimed tiles (`claimed.json`)  
- ⚙️ Configurable delays and concurrency (`config.json`)  
- 🧵 Threaded for speed  

---

## ⚙️ Configuration (`config.json`)

Example:

```json
{
  "repeat_delay": 300,
  "max_threads": 3,
  "claim_delay": 2,
  "headless": true
}
````

| Option         | Description                                           |
| -------------- | ----------------------------------------------------- |
| `repeat_delay` | Time (seconds) between full runs of all accounts      |
| `max_threads`  | Maximum number of accounts running simultaneously     |
| `claim_delay`  | Wait time (seconds) after each claim before moving on |
| `headless`     | Run browser invisibly (`true`/`false`)                |

---

## 🚀 Quick Start

```bash
git clone https://github.com/Bllare/Wplace-Pumpkings-Bot.git
cd Wplace-Pumpkings-Bot
pip install -r requirements.txt
```

1. Add your **JWT tokens** to `accounts.txt` (one per line)
2. Run the bot:

```bash
python main.py
```

---

## 📂 Files

| File              | Description                    |
| ----------------- | ------------------------------ |
| `main.py`         | Main bot logic                 |
| `extract_urls.py` | Fetches & updates pumpkin URLs |
| `config.json`     | Config (threads, delays, etc.) |
| `claimed.json`    | Tracks claimed pumpkins        |
| `accounts.txt`    | Account tokens (one per line)  |

---

## 🪪 License & Credits

**© 2025 [Bllare](https://github.com/Bllare)** — MIT License
If you use or modify this code, **credit is required** in your README or source.

> Made with ☕ + 🎃 + 💻 — for research and educational purposes only.
