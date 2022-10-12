import hashlib
from math import gcd
import random


def hash(data) -> str:
    h = hashlib.sha3_256()
    h.update(bytearray(str(data), encoding="utf8"))
    return h.hexdigest()


def random_coprime(n):
    while True:
        x = random.randint(1, n)
        if gcd(x, n) == 1:
            return x
