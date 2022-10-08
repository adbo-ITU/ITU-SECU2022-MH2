import hashlib


def hash(data) -> str:
    h = hashlib.sha3_256()
    h.update(bytearray(str(data), encoding="utf8"))
    return h.hexdigest()
