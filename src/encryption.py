import logging
import pyaes
from network import NetworkChannel
from utils import hash


def get_aes(symmetric_key: int):
    # AES library errors out if it doesn't receive a 32-byte key
    key = hash(symmetric_key)[:32]
    aes = pyaes.AESModeOfOperationCTR(bytes(key, encoding="ascii"))
    return aes


def encrypt(message: str, symmetric_key: int):
    ciphertext = get_aes(symmetric_key).encrypt(message)
    return ciphertext


def decrypt(ciphertext, symmetric_key: int):
    message = get_aes(symmetric_key).decrypt(ciphertext)
    return message.decode("utf-8")


class EncryptedChannel():
    def __init__(self, channel: NetworkChannel, symmetric_key: int):
        self.channel = channel
        self.symmetric_key = symmetric_key

    def send(self, message: str):
        logging.debug(f"[SEND + ENCRYPT] {message}")
        encrypted = encrypt(message, self.symmetric_key)
        return self.channel.send(encrypted)

    def receive(self) -> str:
        ciphertext = self.channel.receive_bytes()
        message = decrypt(ciphertext, self.symmetric_key)
        # check MAC
        logging.debug(f"[RECV + DECRYPT] {message}")
        return message
