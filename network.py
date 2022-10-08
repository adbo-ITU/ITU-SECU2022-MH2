import socket
from typing import Union


PORT = 42069
MESSAGE_SIZE = 1024


class NetworkChannel:
    def __init__(self, sock: socket.socket):
        self.sock = sock

    def send(self, message: str):
        print(f"[SEND] {message}")
        return self.sock.sendall(bytearray(message, encoding="utf-8"))

    def receive(self) -> str:
        message = self.sock.recv(MESSAGE_SIZE).decode("utf-8")
        print(f"[RECV] {message}")
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

    print("Waiting for other player to connect...")

    conn, addr = sock.accept()

    print(f"Player connected from {addr[0]}:{addr[1]}.")

    return NetworkChannel(conn)
