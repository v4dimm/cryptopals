from requests import get
from base64 import b64decode
from C9S2 import pad_text
from Crypto.Cipher import AES


def decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


def encrypt_ecb(plaintext, key):
    plaintext = pad_text(plaintext, AES.block_size)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


def get_text():
    text = get('https://cryptopals.com/static/challenge-data/7.txt').text
    return b64decode(text)


def main():
    key = b"YELLOW SUBMARINE"
    b64_decode_text = get_text()
    message = decrypt_ecb(b64_decode_text, key)
    return message


def check_encrypt():
    key = b"YELLOW SUBMARINE"
    plaintext = main()
    ciphertext = encrypt_ecb(plaintext, key)
    if ciphertext == get_text():
        print("That's work")



if __name__ == "__main__":
    plaintext = main()
    print(plaintext)
    
    check_encrypt()