import random

from network import NetworkChannel, init_client, init_server


def play_as_client(channel: NetworkChannel):
    roll = random.randint(1, 6)
    channel.send(f"I rolled {roll}")
    message = channel.receive()


def play_as_server(channel: NetworkChannel):
    roll = random.randint(1, 6)
    message = channel.receive()
    channel.send(f"Ok, I rolled {roll}")


def main():
    channel = init_client()
    if channel:
        print("Other player is hosting - I will start.")
        print()
        with channel:
            play_as_client(channel)
        print()
    else:
        print("Other player is not hosting - I will be the server.")

        with init_server() as channel:
            print()
            try:
                play_as_server(channel)
            except ConnectionResetError:
                pass

        print()
        print("Player disconnected.")

    print("Game is finished.")


if __name__ == "__main__":
    main()
