import json
import time

PUBLIC_KEYS_FILE = "public_keys.json"


def set_public_key(name: str, public_key: int):
    with open(PUBLIC_KEYS_FILE, "r") as f:
        try:
            public_keys = json.load(f)
        except json.JSONDecodeError:
            public_keys = {}

    public_keys[name] = str(public_key)

    with open(PUBLIC_KEYS_FILE, "w") as f:
        json.dump(public_keys, f, indent=4)


def get_public_key(name: str) -> int:
    # TODO: remove
    time.sleep(0.5)

    with open(PUBLIC_KEYS_FILE, "r") as f:
        public_keys = json.load(f)

    return int(public_keys[name])
