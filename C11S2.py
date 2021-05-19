from os import urandom
from random import randint
from Crypto.Cipher import AES
from C7S1 import encrypt_ecb
from C8S1 import get_repeating_chunk
from C10S2 import encrypt_cbc


def generate_AES_key():
    key = urandom(AES.block_size)
    return key


def generate_random_bytes(count):
    random_bytes = urandom(count)
    return random_bytes


def encrypt_AES_CBC_with_random_key(plaintext, key=generate_AES_key()):
    IV = generate_AES_key() # same thing
    modified_plaintext = generate_random_bytes(randint(5, 10)) + plaintext + generate_random_bytes(randint(5, 10))

    ciphertext = encrypt_cbc(
        modified_plaintext, 
        AES.block_size,
        key,
        IV
    )
    return ciphertext


def get_cipher_block_mode(plaintext):
    mode = randint(1, 2)
    key = generate_AES_key()
    if mode == 1:
        print('Use ECB')
        return encrypt_ecb(plaintext, key)
    elif mode == 2:
        print('Use CBC')
        return encrypt_AES_CBC_with_random_key(plaintext, key)


def detect_cipher_block_mode(ciphertext):
    if get_repeating_chunk(ciphertext, AES.block_size)['repeating'] > 0:
        print("That's ECB")
    else:
        print("That's CBC")


def main():
    plaintext = b'q' * 16 + b'w'*16 + b'q'*16
    ciphertext = get_cipher_block_mode(plaintext)

    print('Plaintext: {0}\nCiphertext: {1}'.format(plaintext, ciphertext))

    detect_cipher_block_mode(ciphertext)


if __name__ == "__main__":
    main()