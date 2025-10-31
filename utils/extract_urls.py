import json
import requests
from typing import Dict, List, Tuple

PUMPKIN_URL = "https://wplace.samuelscheit.com/tiles/pumpkin.json"
BASE_URL = "https://wplace.live/?lat={lat}&lng={lng}&zoom=14"
URLS_FILE = "data/URLS.txt"


def extract() -> List[Tuple[str, str]]:
    """
    Fetch the pumpkin map data and rebuild URLS.txt with formatted links.

    Returns:
        List of (number, url) tuples that were written.
    """
    print("[extract_urls] Fetching pumpkin.json...")

    try:
        response = requests.get(PUMPKIN_URL, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[extract_urls] ❌ Failed to fetch pumpkin.json: {e}")
        return []

    try:
        data: Dict[str, Dict[str, float]] = response.json()
    except json.JSONDecodeError:
        print("[extract_urls] ❌ Invalid JSON received.")
        return []

    entries: List[Tuple[str, str]] = []
    for number, info in data.items():
        lat, lng = info.get("lat"), info.get("lng")
        if lat is None or lng is None:
            continue
        url = BASE_URL.format(lat=lat, lng=lng)
        entries.append((number, url))

    if not entries:
        print("[extract_urls] ⚠️ No valid entries found in data.")
        return []

    try:
        with open(URLS_FILE, "w", encoding="utf-8") as f:
            for number, url in entries:
                f.write(f"{number} - {url}\n")
    except OSError as e:
        print(f"[extract_urls] ❌ Failed to write {URLS_FILE}: {e}")
        return []

    print(f"[extract_urls] ✅ Wrote {len(entries)} URLs to {URLS_FILE}")
    return entries


if __name__ == "__main__":
    extract()
