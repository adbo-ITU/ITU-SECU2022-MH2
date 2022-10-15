from utils import random_coprime, hash
from constants import p, g


def create_signature(m, sk):
    """Creates an ElGamal signature for a message m using a secret key."""
    k = random_coprime(p - 1)
    r = pow(g, k, p)

    h_m = int(hash(m), 16)
    s = (h_m - sk * r) * pow(k, -1, p - 1) % (p - 1)

    if s == 0:
        return create_signature(m, sk)

    return r, s


def verify_signature(m, r, s, vk):
    """Verifies an ElGamal signature for a message m using a public key."""
    if r <= 0 or r >= p or s <= 0 or s >= (p - 1):
        return False

    left = pow(g, int(hash(m), 16), p)
    right = pow(vk, r, p) * pow(r, s, p) % p

    return left == right
