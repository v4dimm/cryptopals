from C11S2 import generate_AES_key, detect_cipher_block_mode
from C7S1 import encrypt_ecb
from Crypto.Cipher import AES
from base64 import b64decode

KEY = b'T\xb6\x16\x08\xd9\xcc\xf7\x92\x1e\xaaK\x1c \x11\n\xb2'


def encrypt_AES_ECB(plaintext, key=generate_AES_key()):
    string = b'''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
    aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
    dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
    YnkK'''
    _s = b64decode(string)

    modified_plaintext = plaintext + _s

    ciphertext = encrypt_ecb(
        modified_plaintext, 
        key,
    )
    return ciphertext


def detect_block_size():
    plaintext = b'A'
    ciphertext = encrypt_AES_ECB(plaintext, KEY)
    prev_len = len(ciphertext)
    
    for i in range(1, 17):
        plaintext = b'A'*i
        ciphertext = encrypt_AES_ECB(plaintext, KEY)
        if len(ciphertext) != prev_len:
            return len(ciphertext) - prev_len


def is_ECB_mode(block_size):
    plaintext = b'A' * 64
    ciphertext = encrypt_AES_ECB(plaintext, KEY)
    if detect_cipher_block_mode(ciphertext, block_size) == "ECB":
        return True


def oracle_byte(block_size=AES.block_size, _byte=1, guess_pt=b''):
    plaintext = b'A' * (block_size - _byte)
    source_ciphertext = encrypt_AES_ECB(plaintext)[:block_size]

    guessed_ciphertexts = []

    for byte in range(256):
        modified_plaintext = plaintext + guess_pt + bytes([byte])
        guessed_ciphertexts.append({
            'byte': byte,
            'plaintext': modified_plaintext,
            'block': encrypt_AES_ECB(modified_plaintext)[:block_size]
        })

    for block in guessed_ciphertexts:
        if block['block'] == source_ciphertext:
            return bytes([block['byte']])


def main():
    block_size = detect_block_size()

    if is_ECB_mode(block_size) == True:
        guess_pt = b''

        block_size = 256
        for byte in range(1, block_size):
            o_byte = oracle_byte(block_size, byte, guess_pt)
            if o_byte is None:
                pass
            else:
                guess_pt += o_byte
        print(guess_pt)


if __name__ == "__main__":
    main()