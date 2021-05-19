from sys import platform
from requests import get
from base64 import b64decode
from Crypto.Cipher import AES
from C7S1 import encrypt_ecb, decrypt_ecb
from C9S2 import pad_block


def get_text():
    text = get('https://cryptopals.com/static/challenge-data/10.txt').text
    return b64decode(text)


def xor_data(data_1, data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(data_1, data_2)])


def encrypt_cbc(plaintext, block_size, key, IV):

    blocks = [plaintext[i:i+block_size] for i in range(0, len(plaintext), block_size)]
    ciphertext = b''
    prev = IV

    for block in blocks:
        block = pad_block(block, block_size)
        xored_text = xor_data(block, prev)
        cipherblock = encrypt_ecb(xored_text, key)
        ciphertext += cipherblock
        prev = cipherblock
 
    return ciphertext


def decrypt_cbc(ciphertext, block_size, key, IV):

    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
    plaintext = b''
    prev = IV

    for block in blocks:
        decrypt_text = decrypt_ecb(block, key)
        plaintext += xor_data(decrypt_text, prev)
        prev = block

    return plaintext


def main():
    key = b"YELLOW SUBMARINE"
    block_size = AES.block_size
    IV = bytes(block_size)
    ciphertext = get_text()
    plaintext = decrypt_cbc(ciphertext, block_size, key, IV)

    checktext = b'Check correct AES CBC work'
    decrypted_ciphertext = decrypt_cbc(
        encrypt_cbc(checktext, block_size, key, IV), AES.block_size, key, IV
    ) 
    
    print('Check AES CBC work\nPlaintext: {0}\nDecrypt ciphertext: {1}\n\n'.format(checktext, decrypted_ciphertext))

    return plaintext


if __name__ == "__main__":
    plaintext = main()
    print(plaintext)