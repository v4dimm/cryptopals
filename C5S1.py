#!/usr/bin/env python3

def repeating_xor_key(plaintext, key):
    ciphertext = b''
    i = 0
    for byte in plaintext:
        ciphertext += bytes([byte ^ key[i]])
        i = i + 1 if i < len(key) - 1 else 0
    return ciphertext


if __name__ == "__main__":

    text = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    key = b"ICE"

    print(repeating_xor_key(text, key).hex())