---
title: 'Security 1: Mandatory Hand-in 2'
author:
- Adrian Borup (adbo@itu.dk)
date: Oct 25 2022
geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
---

## Protocol overview

From the assignment text, it is given that Alice and Bob

1. Do not trust each other to roll randomly if they know the other person's outcome
2. Do not want anyone else to be able to learn anything about the dice game, with communication happening on an insecure network

To solve the first part, we will assume that we have a secure communication channel, which we will get to later.

### Rolling a die

The problem with just Alice and Bob simply rolling a die each and sending the result to each other is as follows: if Alice rolls a die, Bob may look at Alice's die and change what he rolls according to her roll. Therefore we need a way for Alice and Bob to roll a die each without them being able to use the other person's roll to influence their own roll. For this, we will use the Coin Tossing algorithm.

Coin Tossing works as follows:

1. Alice initiates the communication by performing these steps:
   1. She rolls a die, with the outcome being denoted $a$.
   2. Before she shares the outcome with Bob, she generates a random number $r$. Why we need this will be explained afterwards.
   3. She computes a *commitment* - a way for her to bind herself to the outcome of the roll without sharing the actual roll.
   4. The commitment $c$ is computed as the hash of the concatenation of $r$ and $a$. That is $c = H(r | a)$.
   5. Alice sends the commitment to Bob
2. Bob receives a commitment $c$ from Alice and performs the following steps:
   1. He rolls a die, with the outcome being denoted $b$. Because Bob doesn't know $a$, he can't use it to influence $b$.
   2. He sends $b$ to Alice.
3. Alice receives Bob's roll $b$:
   1. She sends the values she used to make her commitment $(r, a)$ to Bob
4. Bob receives $(r, a)$ from Alice:
   1. He computes the commitment himself as $H(r | a)$ and checks if indeed $c = H(r | a)$. If it is, Alice can't have lied about rolling $a$.
5. Both parties combine their respective rolls into a "final" outcome as such: $(a \oplus b)\ \text{mod}\ 6 + 1$ (with $\oplus$ denoting a bitwise XOR).

This is secure under the assumption that finding another input to the hash function that produces the same hash is infeasible. However, this assumption relies on the fact that the input space is large enough. This is why we need a (sufficiently large) $r$ for the commitment. For a die roll, there can be a grand total of 6 different outcomes: $1\ldots 6$. If we were to calculate the commitment as the hash of the roll alone, it would take at most 6 attempts to reverse the commitment. But if we use a large, random $r$ to encode the commitment, it becomes infeasible to reverse it.

### Secure communication

In order for Alice and Bob to perform the protocol, they need a safe means of communication. To fulfil their paranoid requirements, we need to obtain the following three properties:

1. Confidentiality: Nobody else can read and understand the messages sent
2. Authenticity: We must be able to know that a message came from a specific party
3. Integrity: We must be able to determine if a message has been modified since it was sent

In short, I will be using the following to obtain the above properties:

1. Confidentiality
   - AES (symmetric encryption)
2. Authenticity
   - Authenticated Diffie-Hellman key exchange
   - ElGamal digital signatures
   - Asymmetric private/public key pairs
3. Integrity
   - Message authentication codes (MAC)

Why these make the communication secure will be explained soon.

### Issues with the protocol

One issue with the protocol is that it results in a biased die roll, which is a rather large issue because the game is all about rolling random dice. The issue occurs when combining the two rolls into a final roll, where an XOR is used. If we send 3 bits over the network (which is the least we need to represent 6 numbers), we can represent 8 different numbers: 0 through 7. But only 1-6 are valid rolls. If two valid rolls are sent over the network, the XOR of them can become a number that is outside the range of 1-6. With our protocol, given the XOR result on the left, the final outcome is the number on the right:

- $0\ \text{mod}\ 6 + 1 = 1$
- $1\ \text{mod}\ 6 + 1 = 2$
- $2\ \text{mod}\ 6 + 1 = 3$
- $3\ \text{mod}\ 6 + 1 = 4$
- $4\ \text{mod}\ 6 + 1 = 5$
- $5\ \text{mod}\ 6 + 1 = 6$
- $6\ \text{mod}\ 6 + 1 = 1$
- $7\ \text{mod}\ 6 + 1 = 2$

As shown, the inputs 6 and 7 result in a roll of 1 and 2, which makes 1 and 2 double as likely to be the outcome compared to 3-6. However, as has been mentioned by the lecturer, this is not really important for the sake of this project. It's more about the trust and security in communication.

## Why is the protocol secure?

TBA..

## Implementing the protocol

TBA..
