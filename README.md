# 🎃 WPlace Auto Claimer Bot

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-3910)
[![Selenium](https://img.shields.io/badge/Automation-Selenium-orange.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/Bllare/Wplace-Pumpkings-Bot/blob/main/LICENSE)

> 🧩 Automatically claims **pumpkins** on [wplace.live](https://wplace.live)  
> Supports multiple accounts, threading, and live pumpkin fetching.

---

## ⚡ Features
- 🔁 Auto-updates pumpkin URLs (`extract_urls.py` → `data/URLS.txt`)  
- 🧑‍🤝‍🧑 Multi-account support (`config/accounts.txt`)  
- 🧠 Skips already claimed tiles (`data/claimed.json`)  
- ⚙️ Configurable delays and concurrency (`config/config.json`)  
- 🧵 Threaded execution for multiple accounts  

---

## 🚀 Quick Start

```bash
git clone https://github.com/Bllare/Wplace-Pumpkings-Bot.git
cd Wplace-Pumpkings-Bot
pip install -r requirements.txt
````

Add your account tokens in:

```
config/accounts.txt
```

Then run the bot:

```bash
python main.py
```

Or on Windows, use the included launcher:

```bat
start.bat
```

> The bot will automatically fetch pumpkin URLs, claim tiles, and save progress in `data/claimed.json`.

---

## 📂 Directory Structure

```
Wplace-Pumpkings-Bot/
│
├── main.py               # Main bot logic
├── start.bat             # Windows launcher
├── README.md             # This file
├── LICENSE               # Terms under which this project can be used
├── requirements.txt      # Python dependencies
│
├── config/
│   ├── accounts.txt      # Your JWT tokens (one per line)
│   └── config.json       # Config: threads, delays, headless
│
├── data/
│   ├── URLS.txt          # List of pumpkin coordinates (auto-generated)
│   └── claimed.json      # Tracks claimed tiles per account
│
└── utils/
    └── extract_urls.py   # Script to fetch pumpkin URLs
```

---

## ⚙️ Configuration (`config/config.json`)

```json
{
  "repeat_delay": 1200,
  "max_threads": 3,
  "claim_delay": 2,
  "headless": false
}
```

| Key            | Description                                             |
| -------------- | ------------------------------------------------------- |
| `repeat_delay` | Time in seconds to wait between full loops of accounts. |
| `max_threads`  | Number of accounts processed concurrently.              |
| `claim_delay`  | Delay (seconds) after each claim click.                 |
| `headless`     | Run Chrome in headless mode (`true`/`false`).           |

---

## 🪪 License & Credits

**© 2025 [Bllare](https://github.com/Bllare)** — MIT License
If you use or modify this code, **credit is required** in your README or source.

> Made with ☕ + 🎃 + 💻 — for research and educational purposes only.


## ❤️ Support This Project

If this bot helped you and you want to support future development, you can send a small tip 💛

| Coin | Network | Address |
|------|---------|---------|
| **BTC** | Bitcoin | `bc1qh7f9z5qh0c0ss6887034qhg9es8h4dc0exng95` |
| **ETH** | Ethereum (ERC-20) | `0xc7345f4688adC3bD07668eE151779B77137adb8A` |
| **USDT** | TRON (TRC-20) | `TRYZfe7Cm8kDYCejwbHY3CT156uFGFUN3c` |
| **TON** | TON | `UQCWnfQqZNIFGUytEdsMxFmAZxIsTh2YdGAcM8G1Qe7uHBoK` |
| **LTC** | LTC | `ltc1ql9yzy9qmappr6mmqa79yad7ga2p4m5vw5wkwp4` |

**Quick Pay (TrustWallet links):**

- [BTC](https://link.trustwallet.com/send?coin=0&address=bc1qh7f9z5qh0c0ss6887034qhg9es8h4dc0exng95)
- [ETH (ERC-20)](https://link.trustwallet.com/send?coin=60&address=0xc7345f4688adC3bD07668eE151779B77137adb8A)
- [USDT (TRC-20)](https://link.trustwallet.com/send?coin=195&address=TRYZfe7Cm8kDYCejwbHY3CT156uFGFUN3c&token_id=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t)
- [TON](https://link.trustwallet.com/send?coin=607&address=UQCWnfQqZNIFGUytEdsMxFmAZxIsTh2YdGAcM8G1Qe7uHBoK)
- [LTC](https://link.trustwallet.com/send?coin=2&address=ltc1ql9yzy9qmappr6mmqa79yad7ga2p4m5vw5wkwp4)

> Note: USDT is TRON (TRC20), not ERC20.

Thank you 🙏
