import random
import sys
from cryptography import generate_key_pair
import logging

from network import NetworkChannel, init_client, init_server
import utils
from log import logger

sys.setrecursionlimit(10000)

COMMITMENT_RAND_BITS = 256


distribution = [0] * 6


def play_as_client(channel: NetworkChannel, num_rounds: int, round=1):
    my_roll = random.randint(1, 6)

    r = random.randint(0, 2 ** COMMITMENT_RAND_BITS - 1)
    commitment = encode_commitment(my_roll, r)

    channel.send(commitment)
    their_roll = int(channel.receive())
    channel.send(f"{my_roll} {r}")

    roll = combine_rolls(my_roll, their_roll)

    logging.info(f"Roll result: {roll}")
    distribution[roll - 1] += 1

    if round < num_rounds:
        play_as_server(channel, num_rounds, round + 1)


def play_as_server(channel: NetworkChannel, num_rounds: int, round=1):
    my_roll = random.randint(1, 6)

    commitment = channel.receive()
    channel.send(f"{my_roll}")
    their_roll, r = (int(x) for x in channel.receive().split())

    if commitment == encode_commitment(their_roll, r):
        logging.info("Commitment matches roll.")
    else:
        logging.error("Commitment does not match roll.")
        exit(1)

    roll = combine_rolls(my_roll, their_roll)

    logging.info(f"Roll result: {roll}")
    distribution[roll - 1] += 1

    if round < num_rounds:
        play_as_client(channel, num_rounds, round + 1)


def combine_rolls(a: int, b: int) -> int:
    return (a ^ b) % 6 + 1


def encode_commitment(message, r: int) -> str:
    return utils.hash(f"{r}{message}")


def main():
    private_key, public_key = generate_key_pair()

    logging.debug(f"Private key: 0x{private_key:x}")
    logging.debug(f"Public key: 0x{public_key:x}")

    num_rounds = 1
    channel = init_client()
    if channel:
        logging.info("Other player is hosting - I will start.")
        with channel:
            play_as_client(channel, num_rounds)
    else:
        logging.info("Other player is not hosting - I will be the server.")

        with init_server() as channel:
            try:
                play_as_server(channel, num_rounds)
            except ConnectionResetError:
                pass

        logging.info("Player disconnected.")

    logging.info("Game is finished.")


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)

    main()

    logging.debug(f"Distribution of rolls: {distribution}")
