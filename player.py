import socket
from typing import Union

PORT = 42069
MESSAGE_SIZE = 1024


def play_as_client(sock: socket.socket):
    send_message("Hello, world!", sock)
    message = receive_message(sock)
    print(f"Received message {message}")


def play_as_server(conn: socket.socket):
    message = receive_message(conn)
    print(f"Received {message}")
    send_message(message, conn)


def init_client(port: int) -> Union[socket.socket, None]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(("127.0.0.1", port))
        return sock
    except ConnectionRefusedError:
        sock.close()
        return None


def init_server(port: int) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", port))
    sock.listen()

    print("Waiting for other player to connect...")

    conn, addr = sock.accept()

    print(f"Player connected from {addr[0]}:{addr[1]}.")

    return conn


def receive_message(sock: socket.socket) -> str:
    return sock.recv(MESSAGE_SIZE).decode("utf-8")


def send_message(message: str, sock: socket.socket):
    return sock.sendall(bytearray(message, encoding="utf-8"))


def main():
    sock = init_client(PORT)
    if sock:
        print("Other player is hosting - I will start.")
        print()
        with sock:
            play_as_client(sock)
    else:
        print("Other player is not hosting - I will be the server.")

        with init_server(PORT) as conn:
            print()
            try:
                play_as_server(conn)
            except ConnectionResetError:
                pass

        print()
        print("Player disconnected.")


if __name__ == "__main__":
    main()
