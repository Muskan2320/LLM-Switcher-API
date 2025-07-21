import os
import json
from datetime import datetime

def log_to_file(entry: dict, filename: str = "logs/prompts.jsonl"):
    try:
        entry["timestamp"] = datetime.utcnow().isoformat()
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "a", encoding="utf-8") as f:
            json.dump(entry, f, ensure_ascii=False)
            f.write("\n")
    except Exception as e:
        print(f"Logger failed to log entry: {e}") 