from requests import get
from base64 import b64decode
from Crypto.Cipher import AES


def decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


def get_text():
    text = get('https://cryptopals.com/static/challenge-data/7.txt').text
    return b64decode(text)


def main():
    key = b"YELLOW SUBMARINE"
    b64_decode_text = get_text()
    message = decrypt_ecb(b64_decode_text, key)
    return message


if __name__ == "__main__":
    print(main())