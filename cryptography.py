import random

from utils import hash, random_coprime

p = 6661  # the order of the group
g = 666  # generator of the group


def generate_key_pair():
    sk = random.randint(1, p - 1)
    vk = pow(g, sk, p)
    return sk, vk


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


if __name__ == "__main__":
    m = "hello"
    sk, vk = generate_key_pair()
    r, s = create_signature(m, sk)
    verified = verify_signature(m, r, s, vk)

    print("message", m)
    print("key pair", sk, vk)
    print("signature", r, s)
    print("verified", verified)
