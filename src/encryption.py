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


def create_message_authentication_code(message: str, symmetric_key: int):
    return hash(f"{message}{str(symmetric_key)}")


class EncryptedChannel():
    def __init__(self, channel: NetworkChannel, symmetric_key: int):
        self.channel = channel
        self.symmetric_key = symmetric_key

    def send(self, message: str):
        mac = create_message_authentication_code(message, self.symmetric_key)
        logging.debug(f"[SEND: TO ENCRYPT] Message: '{message}', MAC: '{mac}'")
        message_with_mac = f"{message}{mac}"
        encrypted = encrypt(message_with_mac, self.symmetric_key)
        return self.channel.send(encrypted)

    def receive(self) -> str:
        ciphertext = self.channel.receive_bytes()
        message_with_mac = decrypt(ciphertext, self.symmetric_key)
        message, mac = message_with_mac[:-64], message_with_mac[-64:]

        logging.debug(f"[RECV: DECRYPTED] Message: '{message}', MAC: '{mac}'")

        if mac != create_message_authentication_code(message, self.symmetric_key):
            logging.error(f"MAC did not match message")
            exit(1)

        return message
