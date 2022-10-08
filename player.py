import socket
from typing import Union

PORT = 42069
MESSAGE_SIZE = 1024


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


def main():
    sock = init_client(PORT)
    if sock:
        print("Other player is hosting - I will start.")
        print()

        with sock:
            sock.sendall(b"Hello, world!")
            data = sock.recv(MESSAGE_SIZE)
            print(f"Received {data!r}")
    else:
        print("Other player is not hosting - I will be the server.")

        with init_server(PORT) as conn:
            print()
            try:
                while True:
                    data = conn.recv(MESSAGE_SIZE)

                    if not data:
                        break

                    print(f"Received {data!r}")
                    conn.sendall(data)
            except ConnectionResetError:
                pass

        print()
        print("Player disconnected.")


if __name__ == "__main__":
    main()
