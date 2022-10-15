import random
import sys
import logging

from key_exchange import generate_key_pair, authenticated_key_exchange_client, authenticated_key_exchange_server
from network import NetworkChannel, init_client, init_server
import pki
import utils
from log import logger
from constants import COMMITMENT_RAND_BITS, NUM_ROUNDS

sys.setrecursionlimit(10000)

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


def handle_client(channel: NetworkChannel, private_key: int):
    who_am_i, who_are_they = 'client', 'server'
    shared_key = authenticated_key_exchange_client(
        channel, private_key, who_am_i, who_are_they)

    logging.debug(
        f"Authenticated key exchange completed with {who_are_they}. Shared key: {shared_key}")

    play_as_client(channel, NUM_ROUNDS)


def handle_server(channel: NetworkChannel, private_key: int):
    who_am_i, who_are_they = 'server', 'client'
    shared_key = authenticated_key_exchange_server(
        channel, private_key, who_am_i, who_are_they)

    logging.debug(
        f"Authenticated key exchange completed with {who_are_they}. Shared key: {shared_key}")

    play_as_server(channel, NUM_ROUNDS)


def init_client_or_server():
    private_key, public_key = generate_key_pair()

    logging.debug(f"My long-term private key: {private_key}")
    logging.debug(f"My long-term public key: {public_key}")

    channel = init_client()
    if channel:
        logging.info("Other player is hosting - I will start.")

        # Not part of the protocol - but we just need an easy way to know the
        # each others public keys. Having a solid PKI is an assumption we make.
        pki.set_public_key('client', public_key)

        with channel:
            handle_client(channel, private_key)
    else:
        logging.info("Other player is not hosting - I will be the server.")

        # Same as with the client
        pki.set_public_key('server', public_key)

        with init_server() as channel:
            try:
                handle_server(channel, private_key)
            except ConnectionResetError:
                pass

        logging.info("Player disconnected.")

    logging.info("Game is finished.")


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)

    init_client_or_server()

    logging.debug(f"Distribution of rolls: {distribution}")
