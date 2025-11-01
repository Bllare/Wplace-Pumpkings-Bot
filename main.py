"""
https://github.com/Bllare/Wplace-Pumpkings-Bot

Project Name: Wplace-Pumpkings-Bot
Description: A brief description of what this project does.

Author: Bllare
License: MIT License

Copyright (c) 2025 Bllare

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
print("Github: @Bllare | linktr.ee/Bllare")

import json
import os
import time
import threading
from typing import List, Tuple
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.extract_urls import extract
import queue
from pathlib import Path

# --- Config / Data Paths ---
CONFIG_PATH = Path("config/config.json")
ACCOUNTS_PATH = Path("config/accounts.txt")
URLS_PATH = Path("data/URLS.txt")
CLAIMED_PATH = Path("data/claimed.json")

CLAIMED_PATH.parent.mkdir(parents=True, exist_ok=True)  # ensure data/ exists


class Config:
    """Loads configuration values."""
    def __init__(self, path=CONFIG_PATH):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.repeat_delay = data.get("repeat_delay", 300)
        self.max_threads = data.get("max_threads", 3)
        self.claim_delay = data.get("claim_delay", 2)
        self.headless = data.get("headless", False)


class AccountManager:
    """Manages account tokens."""
    def __init__(self, file_path=ACCOUNTS_PATH):
        self.tokens = self._load_accounts(file_path)

    @staticmethod
    def _load_accounts(file_path: Path) -> List[str]:
        if not file_path.exists():
            raise FileNotFoundError(f"{file_path} not found.")
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]


class URLManager:
    """Handles URL reading and claimed tracking."""
    def __init__(self, urls_file=URLS_PATH, claimed_file=CLAIMED_PATH):
        self.urls_file = urls_file
        self.claimed_file = claimed_file
        self.lock = threading.RLock()
        self.urls = self._load_urls()
        self.claimed = self._load_claimed()

    def _load_urls(self) -> List[Tuple[str, str]]:
        if not os.path.exists(self.urls_file):
            print(f"{self.urls_file} not found. Extracting URLs...")
            extract()
        urls = []
        with open(self.urls_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if " - " in line:
                    number, url = line.split(" - ", 1)
                else:
                    number, url = None, line
                urls.append((number, url))
        return urls

    def _load_claimed(self) -> dict:
        if os.path.exists(self.claimed_file):
            with open(self.claimed_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_claimed(self):
        with self.lock:
            with open(self.claimed_file, "w", encoding="utf-8") as f:
                json.dump(self.claimed, f, indent=2)

    def mark_claimed(self, token: str, number: str):
        if not number:
            return
        with self.lock:
            if token not in self.claimed:
                self.claimed[token] = []
            if number not in self.claimed[token]:
                self.claimed[token].append(number)
                self.save_claimed()

    def is_claimed(self, token: str, number: str) -> bool:
        if not number:
            return False
        return number in self.claimed.get(token, [])


class ClaimBot:
    """Handles automation for a single account."""
    def __init__(self, token: str, url_manager: URLManager, config: Config):
        self.token = token
        self.url_manager = url_manager
        self.config = config
        self.driver = None
        self.wait = None

    def setup_driver(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        if self.config.headless:
            options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(300, 600)
        self.wait = WebDriverWait(self.driver, 2)

    def inject_token(self):
        self.driver.get("https://backend.wplace.live")
        cookie = {
            "name": "j",
            "value": self.token,
            "domain": ".backend.wplace.live",
            "path": "/",
            "secure": True,
            "httpOnly": False,
        }
        self.driver.add_cookie(cookie)
        self.driver.get("https://wplace.live")

    def close_modals(self):
        modals = [
            '/html/body/div/dialog[18]/div/form/button',
            '/html/body/div/dialog[7]/div/form/button'
        ]
        for xpath in modals:
            try:
                WebDriverWait(self.driver, 0.5).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                ).click()
            except:
                pass

    def process_urls(self):
        for number, url in self.url_manager.urls:
            if number and self.url_manager.is_claimed(self.token, number):
                print(f"[{self.token[-10:]}...] Skipping {url} (claimed #{number})")
                continue

            try:
                self.driver.get(url)
                self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[6]/button"))
                )

                for _ in range(60):
                    self.driver.execute_script("""
                        var evt = new MouseEvent('click', {
                            clientX: arguments[0],
                            clientY: arguments[1],
                            bubbles: true,
                            cancelable: true
                        });
                        document.elementFromPoint(arguments[0], arguments[1]).dispatchEvent(evt);
                    """, 250, 320)
                    try:
                        self.wait.until(
                            EC.presence_of_element_located(
                                (By.XPATH, "//div[contains(@class, 'modal') or //button[contains(text(), 'Claim')]]")
                            )
                        )
                        break
                    except:
                        time.sleep(1)

                # Already claimed?
                try:
                    self.wait.until(
                        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Claimed')]"))
                    )
                    print(f"[{self.token[-10:]}...] Already claimed (#{number})")
                    self.url_manager.mark_claimed(self.token, number)
                    continue
                except:
                    pass

                # Try to claim
                try:
                    claim_btn = self.wait.until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//button[contains(text(), 'Claim') and not(@disabled)]")
                        )
                    )
                    claim_btn.click()
                    print(f"[{self.token[-10:]}...] Claimed successfully (#{number})")

                    #Some times it gives an error from server and wont claim the pumpkings, comment for now
                    #self.url_manager.mark_claimed(self.token, number)                    

                    time.sleep(2)  # wait 2 seconds for processing
                except:
                    print(f"[{self.token[-10:]}...] No Claim button available (#{number})")

                time.sleep(self.config.claim_delay)

            except Exception as e:
                print(f"[{self.token[-10:]}...] Error on {url}: {e}")
                time.sleep(2)

    def run(self):
        print(f"[{self.token[-10:]}...] Starting bot...")
        self.setup_driver()
        self.inject_token()
        self.close_modals()
        self.process_urls()
        self.driver.quit()
        print(f"[{self.token[-10:]}...] Finished session.")


class Runner:
    """Controls threading and main execution loop."""
    def __init__(self, config: Config, accounts: AccountManager, urls: URLManager):
        self.config = config
        self.accounts = accounts
        self.urls = urls

    def run_once(self):
        """Run all accounts with a fixed number of concurrent threads."""
        account_queue = queue.Queue()
        for token in self.accounts.tokens:
            account_queue.put(token)

        active_threads = []

        while not account_queue.empty() or active_threads:
            # Clean finished threads
            active_threads = [t for t in active_threads if t.is_alive()]

            # Launch new ones if we have room
            while len(active_threads) < self.config.max_threads and not account_queue.empty():

                token = account_queue.get()

                for number, url in self.urls.urls:
                    if not (number and self.urls.is_claimed(token, number)):
                        bot = ClaimBot(token, self.urls, self.config)
                        t = threading.Thread(target=bot.run, name=f"Bot-{token[:8]}")
                        t.start()
                        active_threads.append(t)
                        print(f"[Runner] Started new session ({len(active_threads)}/{self.config.max_threads})")
                        break

            time.sleep(1)  # small delay to prevent busy loop

        print("[Runner] All accounts processed.")

    def loop(self):
        """Main continuous loop: refresh URLs, then process all accounts."""
        while True:
            extract()  # update URL list each loop
            self.urls.urls = self.urls._load_urls()
            print("\n--- New Loop Started ---")
            self.run_once()
            print(f"Sleeping {self.config.repeat_delay}s before next loop...")
            time.sleep(self.config.repeat_delay)


if __name__ == "__main__":
    cfg = Config()
    accounts = AccountManager()
    urls = URLManager()
    runner = Runner(cfg, accounts, urls)
    runner.loop()
