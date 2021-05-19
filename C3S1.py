#!/usr/bin/env python3

from math import sqrt
from collections import Counter

FREQUENCY_TABLE = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.360,
    "x": 0.150,
    "y": 1.974,
    "z": 0.074,
    ' ': 19.18182
}


def check_english(_string):
    text = Counter(_string.lower())
    coefficient = sum(
        sqrt(FREQUENCY_TABLE.get(chr(char), 0) * y/len(_string))
        for char, y in text.items()
    )
    return coefficient


def xor_single_byte(byte, string):
    res = b''
    for char in string:
        res += bytes([char ^ byte])
    return res


def bruteforce_binary_string(_string):
    emap = []
    for byte in range(256):
        res = xor_single_byte(byte, _string)
        emap.append({
            'key': byte,
            'score': check_english(res),
            'plaintext': res
        })
    emap.sort(key=lambda x: x['score'], reverse=True)
    res = emap[0] if len(emap) > 0 else None
    return res


if __name__ == "__main__":
    text = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    print('Result: {}'.format(bruteforce_binary_string(text)['plaintext']))