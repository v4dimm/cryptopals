#!/usr/bin/env python3

import re
import math
from collections import Counter
from Challenge_2 import xor_strings
import struct

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
        math.sqrt(FREQUENCY_TABLE.get(chr(char), 0) * y/len(_string))
        for char, y in text.items()
    )
    return coefficient


def xoring(byte, string):
    b_string = struct.pack('B', byte) * len(string)
    return xor_strings(b_string, string)


def bruteforce_string(_string):
    emap = []
    for byte in range(0, 255):
        res = xoring(byte, bytes.fromhex(_string))
        emap.append((check_english(res), res))
    emap.sort(key=lambda x: x[0], reverse=True)
    res = emap[0][1] if len(emap) > 0 else None
    return res


if __name__ == "__main__":
    # text = '0e3647e8592d35514a081243582536ed3de6734059001e3f535ce6271032'
    text = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print('Result: {}'.format(bruteforce_string(text)))