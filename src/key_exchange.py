import logging
import random

import pki
from network import NetworkChannel
from signature import create_signature, verify_signature
from utils import from_json, to_json
from constants import p, g


def generate_key_pair():
    sk = random.randint(1, p - 1)
    vk = pow(g, sk, p)
    return sk, vk


def create_key_exchange_payload(dh_public, signing_key, sender, recipient):
    message = to_json({
        "recipient": recipient,
        "sender": sender,
        "dh_public": f"{dh_public}",
    })

    r, s = create_signature(message, signing_key)

    payload = to_json({
        'message': message,
        'signature': {
            'r': str(r),
            's': str(s),
        },
    })

    return payload


# Part of our PKI assumption is that the public key has been verified against a
# trusted certificate authority.
def verify_key_exchange_payload(sender_payload, expected_recipient):
    payload = from_json(sender_payload)

    message = from_json(payload['message'])
    if message['recipient'] != expected_recipient:
        logging.error("Message is not intended for me.")
        exit(1)

    sender_public_key = pki.get_public_key(message['sender'])

    signature = payload['signature']
    r, s = int(signature['r']), int(signature['s'])

    if not verify_signature(payload['message'], r, s, sender_public_key):
        logging.error("Signature does not match public key.")
        exit(1)

    db_public = int(message['dh_public'])

    return db_public


def authenticated_key_exchange_client(channel: NetworkChannel, signing_key: int, who_am_i: str, who_are_they: str):
    my_dh_secret, my_dh_public = generate_key_pair()
    payload = create_key_exchange_payload(
        my_dh_public, signing_key, sender=who_am_i, recipient=who_are_they)

    logging.debug(
        f"Diffie-Hellman key pair - Private: {my_dh_public}, Public: {my_dh_secret}")

    channel.send(payload)

    their_payload = channel.receive()
    their_dh_public = verify_key_exchange_payload(
        their_payload, expected_recipient=who_am_i)

    return generate_shared_diffie_hellman_secret(their_dh_public, my_dh_secret)


def authenticated_key_exchange_server(channel: NetworkChannel, signing_key: int, who_am_i: str, who_are_they: str):
    my_dh_secret, my_dh_public = generate_key_pair()
    payload = create_key_exchange_payload(
        my_dh_public, signing_key, sender=who_am_i, recipient=who_are_they)

    logging.debug(
        f"Diffie-Hellman key pair - Private: {my_dh_public}, Public: {my_dh_secret}")

    their_payload = channel.receive()
    their_dh_public = verify_key_exchange_payload(
        their_payload, expected_recipient=who_am_i)

    channel.send(payload)

    return generate_shared_diffie_hellman_secret(their_dh_public, my_dh_secret)


def generate_shared_diffie_hellman_secret(their_public_dh, my_secret_dh):
    return pow(their_public_dh, my_secret_dh, p)
