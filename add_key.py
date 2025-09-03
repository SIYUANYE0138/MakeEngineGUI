import json
import sys
from pathlib import Path

KEYS_FILE = Path("keys.json")  # 你在仓库里的 keys 文件路径

def add_key(new_key: str):
    if not KEYS_FILE.exists():
        print("⚠️ keys.json 不存在，先创建一个。")
        data = {"version": "1.0", "keys": [], "hwid_lock": False, "note": "optional remark"}
    else:
        with open(KEYS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

    if "keys" not in data:
        data["keys"] = []

    if new_key in data["keys"]:
        print(f"⚠️ Key 已存在: {new_key}")
    else:
        data["keys"].append(new_key)
        print(f"✅ 已添加 key: {new_key}")

    with open(KEYS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python add_key.py NEW_KEY")
        sys.exit(1)

    new_key = sys.argv[1]
    add_key(new_key)