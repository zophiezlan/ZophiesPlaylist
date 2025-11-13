import json
import sys
import requests

# Updated endpoint path
SERVER_PATH = "http://localhost:5000/SmarterPlaylists/run"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        with open(path, "r", encoding="utf-8") as f:
            payload = json.load(f)
        response = requests.post(SERVER_PATH, json=payload)
        results = response.json()
        if results.get("status") == "ok":
            for i, track in enumerate(results.get("tracks", []), start=1):
                print(f"{i} {track.get('title')} {track.get('artist')}")
        else:
            print(results.get("status", "error"))
    else:
        print("Usage: python test/run.py <program.json>")
