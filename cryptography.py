import random

from utils import hash, random_coprime

# The order of the group. Some 2048-bit prime.
p = 0xeb628434bcc2b89bafb2fe3e64a932dc8be90c11e954589c1120c938882ee8bba786be21787305a9bcb63c9f7ac3c2838f0c8458acfc2b62e7cbf8c1598a6d8c0d9e343662e37e37aefbe49b3fce5caafb36f03aa154fd996f15d6cec4e8f8f163182ff7c533eb40140e36861cf38e592e45127e3e02a284fcf956b0d84efc6d000ecd9b6d089f122a84725478e2cf86fce5170960c9ce838a2d71703e4ba6bcdf4e303fff1fb1e8236e02484e87f1da1857a8dabdeb5eb045673b1a06c1ff08c5c21271a432c35c6c9b38137102d9929311903afbd1ae0573e72b4b381eb6bd154236073eaa422bc98be4f141bb722a51b68a287a896bf53a79c43646842eff
# The generator of the group. Some 256-bit prime.
g = 84996462885609463866711305483314064387877883084507604774672308990802667267509


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
