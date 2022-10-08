import hashlib
import random


def hash(data) -> str:
    h = hashlib.sha3_256()
    h.update(bytearray(str(data), encoding="utf8"))
    return h.hexdigest()


def encode_commitment(message: str, r: str) -> str:
    return hash(f"{r}{message}")


if __name__ == "__main__":
    k = 256
    r = random.randint(0, 2 ** k - 1)
    message = 3
    commitment = encode_commitment(message, str(r))

    print("Message:", message)
    print(f"Random r ({k} bits):", r)
    print("Commitment H(r|m):", commitment)

    other_message = 4

    # Only care about 3 bits. If we received more, we just ignore them.
    final_value = message ^ other_message & 0b111
    # Write about how its random enough. Maybe plot it to show that it is.
    rolled_number = (final_value + r) % 6 + 1
    print("Received message:", other_message)
    print("Final value:", final_value)
    print("Die roll:", rolled_number)
