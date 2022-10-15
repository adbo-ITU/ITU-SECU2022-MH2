# Security 1, mandatory hand-in 2

By Adrian Borup (adbo@itu.dk).

## Dependencies

I use `pyaes` for AES encryption. Install it with `pip`:

```sh
pip install pyaes
```

## Instructions for running

### How to understand the logs?

- `[NETWORK SEND]` and `[NETWORK RECV]` represent information sent in plaintext over the network. Any eavesdropper can read this directly.
- `[SEND: TO ENCRYPT]` and `[RECV: DECRYPTED]` represent information that will be encrypted, have a MAC added, and then sent over the network.

### Running it

From one terminal:

```log
$ python player.py
[DEBUG] My long-term private key: 3202
[DEBUG] My long-term public key: 527
[INFO] Other player is not hosting - I will be the server.
[INFO] Waiting for other player to connect...
[INFO] Player connected from 127.0.0.1:50203.
[DEBUG] Diffie-Hellman key pair - Private: 5650, Public: 5000
[DEBUG] [NETWORK RECV] {"message":"{\"recipient\":\"server\",\"sender\":\"client\",\"dh_public\":\"2600\"}","signature":{"r":"2457","s":"3751"}}
[DEBUG] [NETWORK SEND] {"message":"{\"recipient\":\"client\",\"sender\":\"server\",\"dh_public\":\"5650\"}","signature":{"r":"2859","s":"934"}}
[DEBUG] Authenticated key exchange completed with client. Shared key: 3505
[DEBUG] [NETWORK RECV] b'\x93\xfa#\xd9%\x97\x1c\xd2\xf1,\x0e\'\x0f5\x7fb\xfd@ -\x8c\xa8\x07y\nJ}\x1d\xcbF\xc6\x07\xc4\xd9\xf8\\\x1c\xef\xbaMS\x85\x8a\xdfw\xe6=\x84\xeb{\xa2A\xa2\xb9!\xb8\xdd\xfe\x8chOa\xbd\x12\xd8 -\xc46\x18\xd3\xbf`\xd4&9|,\r\xae\x96y\xd0a\x84(,\x84"\xd3\xc3\xacG\\F5\x1f\xe3\x13b>9\xea\x84\n#M\xa1$\xa9\xc7>\xfa\x98y\xfev\xb3?\x95\x8b\xca\x80\x97V\xca\xe9\x9f'
[DEBUG] [RECV: DECRYPTED] Message: '542403dd57e984b5b4f82758a60fd7550bc7d5b6d499e5558d8c2aa27bc4330d', MAC: '525396f11cc0575ba4459cec4d0c0b29c5fd9bab9cd99bfee73580840695ff44'
[DEBUG] [SEND: TO ENCRYPT] Message: '3', MAC: '4d7285c0d0cd099efbc41c2ff903dede1ece28fd86d9fd13e1eaf233c38f62e7'
[DEBUG] [NETWORK SEND] b"\x95\xfau\xda'\x9cM\xd5\xf4\x7f[}S1$n\xfa\x12$v\x8a\xaeQs\r\x1atK\x9c\x15\x96V\x91\x8a\xfe\x08\x1d\xe8\xe0\x1dS\x89\x85\x82+\xb5l\x80\xe0z\xabG\xf1\xber\xb9\xd9\xff\xdcd\x1ad\xbf\x13\xda"
[DEBUG] [NETWORK RECV] b"\x90\xee(\xd5#\x93J\x87\xf2,Y'\x0f5-f\xa6L~ \x8b\xa8\nwXOtI\x96B\xc1\x03\xcd\x89\xa3XO\xe2\xe1J\x00\x88\x8b\xd1!\xea8\x89\xe0.\xa8\x13\xa1\xeep\xb2\xde\xac\xd6dLb\xbbE\xdf (\xc19\x1d\x81\xbff\x87w?p(\x0b\xfa\xc1~\x871\x89*p\xd7%\x80\xc1\xff\x15\t@nO\xb5M?a9\xba\xdfUuL\xf9\x7f\xfc\x90i\xfd\xcbx\xa9y\xe75\x97\x89\x9f\x80\xc4\x03\x9c\xeb\x9d\x17\x1c\xacV{\x1c\xb5\x9aR\x9c\xd1\x94,8\xb9"
[DEBUG] [RECV: DECRYPTED] Message: '6 98672167298401988557863392932192837891798739083121160840980063220663417026933', MAC: '663ce4a903720b74b3c89fb19f5eab712bd2b7d262c9f3066561caa821014252'
[INFO] Commitment matches roll.
[INFO] Roll result: 6
[DEBUG] [SEND: TO ENCRYPT] Message: '20b99afafe423bf1a8e474e21eab74ee3628b031f9fdd84ac5358553adb8e435', MAC: '9c8e55ead00e7d21d62044239cc89cd3363f864e02ab5101a397d4e5886b30e9'
[DEBUG] [NETWORK SEND] b'\x94\xfes\xd4,\xc5\x1e\xd7\xa2~_,\x04c{f\xfeL#!\x89\xabWsZ\x19,\x19\x98E\x96W\xc7\x8d\xa9S\x1a\xea\xebJQ\x88\xd5\x82v\xeb<\xd0\xb0*\xa9\x17\xa8\xedu\xb9\x8b\xf8\x8dd\x19f\xbeC\xd4q \x92:\x1b\xd0\xef5\x87ul~\x7f\n\xfd\x93{\xd6d\x89\x7f{\xd4/\xd4\x90\xf7N]\x10?O\xe0F`?m\xbf\x83\x03rH\xfa(\xfa\x91j\xfe\x9cs\xfc*\xb7b\x94\x83\xc4\x8f\xc0\x03\x9c\xb8\x92'
[DEBUG] [NETWORK RECV] b"\x95\xfau\xda'\x9cM\xd5\xf4\x7f[}S1$n\xfa\x12$v\x8a\xaeQs\r\x1atK\x9c\x15\x96V\x91\x8a\xfe\x08\x1d\xe8\xe0\x1dS\x89\x85\x82+\xb5l\x80\xe0z\xabG\xf1\xber\xb9\xd9\xff\xdcd\x1ad\xbf\x13\xda"
[DEBUG] [RECV: DECRYPTED] Message: '3', MAC: '4d7285c0d0cd099efbc41c2ff903dede1ece28fd86d9fd13e1eaf233c38f62e7'
[DEBUG] [SEND: TO ENCRYPT] Message: '4 111830250815309484304363362494622882058705163042921030329216776413649332647343', MAC: '7214b3e3d54a030bd8e364e036817a63b06f821447654faf99a19d2c15e5d188'
[DEBUG] [NETWORK SEND] b'\x92\xee \xdc$\x9cK\x86\xf6.[&\x064.g\xa6@~!\x8d\xaf\x06r]O~M\x9dE\xca\x06\xc2\x89\xa9S@\xe8\xe8N\x0f\x86\x83\xd3#\xe5;\x81\xe7-\xa3\x10\xa1\xe8s\xba\xd9\xae\xd6nMd\xbaA\xdb&)\xc49\x1a\x8c\xbdb\x85s=~(\x0c\xff\xc0\x7f\xd5`\xdfx,\xd4r\x82\xc7\xaeG\rDn\x18\xee\x1051o\xee\xd6\x00v\x11\xa9*\xaa\x97h\xfd\x9f|\xadv\xb16\x95\x8f\xcb\x8f\x97\x04\xca\xbc\xcd\x1b\x13\xfc\x04#\x19\xbf\xcbR\x99\x85\x95z<\xb3-'
[INFO] Roll result: 2
[INFO] Player disconnected.
[INFO] Game is finished.
[DEBUG] Distribution of rolls: [0, 1, 0, 0, 0, 1]
```

From another terminal:

```log
$ python player.py
[DEBUG] My long-term private key: 3613
[DEBUG] My long-term public key: 5496
[INFO] Other player is hosting - I will start.
[DEBUG] Diffie-Hellman key pair - Private: 2600, Public: 5640
[DEBUG] [NETWORK SEND] {"message":"{\"recipient\":\"server\",\"sender\":\"client\",\"dh_public\":\"2600\"}","signature":{"r":"2457","s":"3751"}}
[DEBUG] [NETWORK RECV] {"message":"{\"recipient\":\"client\",\"sender\":\"server\",\"dh_public\":\"5650\"}","signature":{"r":"2859","s":"934"}}
[DEBUG] Authenticated key exchange completed with server. Shared key: 3505
[DEBUG] [SEND: TO ENCRYPT] Message: '542403dd57e984b5b4f82758a60fd7550bc7d5b6d499e5558d8c2aa27bc4330d', MAC: '525396f11cc0575ba4459cec4d0c0b29c5fd9bab9cd99bfee73580840695ff44'
[DEBUG] [NETWORK SEND] b'\x93\xfa#\xd9%\x97\x1c\xd2\xf1,\x0e\'\x0f5\x7fb\xfd@ -\x8c\xa8\x07y\nJ}\x1d\xcbF\xc6\x07\xc4\xd9\xf8\\\x1c\xef\xbaMS\x85\x8a\xdfw\xe6=\x84\xeb{\xa2A\xa2\xb9!\xb8\xdd\xfe\x8chOa\xbd\x12\xd8 -\xc46\x18\xd3\xbf`\xd4&9|,\r\xae\x96y\xd0a\x84(,\x84"\xd3\xc3\xacG\\F5\x1f\xe3\x13b>9\xea\x84\n#M\xa1$\xa9\xc7>\xfa\x98y\xfev\xb3?\x95\x8b\xca\x80\x97V\xca\xe9\x9f'
[DEBUG] [NETWORK RECV] b"\x95\xfau\xda'\x9cM\xd5\xf4\x7f[}S1$n\xfa\x12$v\x8a\xaeQs\r\x1atK\x9c\x15\x96V\x91\x8a\xfe\x08\x1d\xe8\xe0\x1dS\x89\x85\x82+\xb5l\x80\xe0z\xabG\xf1\xber\xb9\xd9\xff\xdcd\x1ad\xbf\x13\xda"
[DEBUG] [RECV: DECRYPTED] Message: '3', MAC: '4d7285c0d0cd099efbc41c2ff903dede1ece28fd86d9fd13e1eaf233c38f62e7'
[DEBUG] [SEND: TO ENCRYPT] Message: '6 98672167298401988557863392932192837891798739083121160840980063220663417026933', MAC: '663ce4a903720b74b3c89fb19f5eab712bd2b7d262c9f3066561caa821014252'
[DEBUG] [NETWORK SEND] b"\x90\xee(\xd5#\x93J\x87\xf2,Y'\x0f5-f\xa6L~ \x8b\xa8\nwXOtI\x96B\xc1\x03\xcd\x89\xa3XO\xe2\xe1J\x00\x88\x8b\xd1!\xea8\x89\xe0.\xa8\x13\xa1\xeep\xb2\xde\xac\xd6dLb\xbbE\xdf (\xc19\x1d\x81\xbff\x87w?p(\x0b\xfa\xc1~\x871\x89*p\xd7%\x80\xc1\xff\x15\t@nO\xb5M?a9\xba\xdfUuL\xf9\x7f\xfc\x90i\xfd\xcbx\xa9y\xe75\x97\x89\x9f\x80\xc4\x03\x9c\xeb\x9d\x17\x1c\xacV{\x1c\xb5\x9aR\x9c\xd1\x94,8\xb9"
[INFO] Roll result: 6
[DEBUG] [NETWORK RECV] b'\x94\xfes\xd4,\xc5\x1e\xd7\xa2~_,\x04c{f\xfeL#!\x89\xabWsZ\x19,\x19\x98E\x96W\xc7\x8d\xa9S\x1a\xea\xebJQ\x88\xd5\x82v\xeb<\xd0\xb0*\xa9\x17\xa8\xedu\xb9\x8b\xf8\x8dd\x19f\xbeC\xd4q \x92:\x1b\xd0\xef5\x87ul~\x7f\n\xfd\x93{\xd6d\x89\x7f{\xd4/\xd4\x90\xf7N]\x10?O\xe0F`?m\xbf\x83\x03rH\xfa(\xfa\x91j\xfe\x9cs\xfc*\xb7b\x94\x83\xc4\x8f\xc0\x03\x9c\xb8\x92'
[DEBUG] [RECV: DECRYPTED] Message: '20b99afafe423bf1a8e474e21eab74ee3628b031f9fdd84ac5358553adb8e435', MAC: '9c8e55ead00e7d21d62044239cc89cd3363f864e02ab5101a397d4e5886b30e9'
[DEBUG] [SEND: TO ENCRYPT] Message: '3', MAC: '4d7285c0d0cd099efbc41c2ff903dede1ece28fd86d9fd13e1eaf233c38f62e7'
[DEBUG] [NETWORK SEND] b"\x95\xfau\xda'\x9cM\xd5\xf4\x7f[}S1$n\xfa\x12$v\x8a\xaeQs\r\x1atK\x9c\x15\x96V\x91\x8a\xfe\x08\x1d\xe8\xe0\x1dS\x89\x85\x82+\xb5l\x80\xe0z\xabG\xf1\xber\xb9\xd9\xff\xdcd\x1ad\xbf\x13\xda"
[DEBUG] [NETWORK RECV] b'\x92\xee \xdc$\x9cK\x86\xf6.[&\x064.g\xa6@~!\x8d\xaf\x06r]O~M\x9dE\xca\x06\xc2\x89\xa9S@\xe8\xe8N\x0f\x86\x83\xd3#\xe5;\x81\xe7-\xa3\x10\xa1\xe8s\xba\xd9\xae\xd6nMd\xbaA\xdb&)\xc49\x1a\x8c\xbdb\x85s=~(\x0c\xff\xc0\x7f\xd5`\xdfx,\xd4r\x82\xc7\xaeG\rDn\x18\xee\x1051o\xee\xd6\x00v\x11\xa9*\xaa\x97h\xfd\x9f|\xadv\xb16\x95\x8f\xcb\x8f\x97\x04\xca\xbc\xcd\x1b\x13\xfc\x04#\x19\xbf\xcbR\x99\x85\x95z<\xb3-'
[DEBUG] [RECV: DECRYPTED] Message: '4 111830250815309484304363362494622882058705163042921030329216776413649332647343', MAC: '7214b3e3d54a030bd8e364e036817a63b06f821447654faf99a19d2c15e5d188'
[INFO] Commitment matches roll.
[INFO] Roll result: 2
[INFO] Game is finished.
[DEBUG] Distribution of rolls: [0, 1, 0, 0, 0, 1]
```

## Assignment text

Alice and Bob are playing an online dice game where they must roll virtual dice representing the 6 sides of a physical dice. However, they do not trust each other and suspect that, if they can just roll dice locally on their computers, they will choose the outcome of the dice dishonestly, choosing the outcomes they need in order to win the game. In order to solve this, they want to execute a protocol among themselves to roll a dice while ensuring that they obtain an honest dice rolling outcome. Unfortunately, Alice and Bob are also using an insecure network, where they have no authenticity, confidentiality and integrity guarantees.

How can Alice and Bob play an online dice game over their insecure network when they do not trust each other?

Luckily Alice and Bob are security savvy and just had lectures on advanced cryptography and secure channels. Moreover, they have access to a Public Key Infrastructure, meaning that they know each other's public keys for a digital signature scheme.

Your assignment is to do the following steps help Alice and Bob:

1. Design a protocol that allows Alice an Bob to throw a virtual 6 sided dice over the insecure network even though they do not trust each other.

2. Explain why your protocol is secure using concepts from the lectures.

3. Implement your virtual dice protocol in a programming language of your choosing. The implementation must consist of a program representing Alice and another program representing Bob that communicate over a network (two processes running on localhost is ok). You can use any libraries or programming languages of your choosing.

You must hand in a report explaining your protocol and why it is secure as well as the code implementing your protocol.

You can choose the digital signature scheme used by Alice and Bob, meaning you can choose how their public and secret keys for the digital signature scheme looks like.

HINT: Rolling dice is just sampling a random number from 1 to 6.
