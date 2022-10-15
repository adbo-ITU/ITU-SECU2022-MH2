import socket
from typing import Union
import logging


PORT = 42069
MESSAGE_SIZE = 16 * 1024


class NetworkChannel:
    def __init__(self, sock: socket.socket):
        self.sock = sock

    def send(self, message: Union[str, bytes]):
        logging.debug(f"[NETWORK SEND] {message}")
        if type(message) is str:
            message = bytes(message, encoding="utf-8")
        return self.sock.sendall(message)

    def receive(self) -> str:
        message = self.sock.recv(MESSAGE_SIZE).decode("utf-8")
        logging.debug(f"[NETWORK RECV] {message}")
        return message

    def receive_bytes(self) -> bytes:
        message = self.sock.recv(MESSAGE_SIZE)
        logging.debug(f"[NETWORK RECV] {message}")
        return message

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.sock.close()


def init_client() -> Union[NetworkChannel, None]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(("127.0.0.1", PORT))
        return NetworkChannel(sock)
    except ConnectionRefusedError:
        sock.close()
        return None


def init_server() -> NetworkChannel:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", PORT))
    sock.listen()

    logging.info("Waiting for other player to connect...")

    conn, addr = sock.accept()

    logging.info(f"Player connected from {addr[0]}:{addr[1]}.")

    return NetworkChannel(conn)
