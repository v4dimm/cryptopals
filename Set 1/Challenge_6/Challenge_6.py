#!/usr/bin/env python3

from itertools import zip_longest
from collections import Counter
from requests import get
from base64 import b64decode
from Challenge_3 import bruteforce_binary_string, check_english
from Challenge_5 import repeating_xor_key
import numpy as np


def search_keysize(text):
    # text = bytes.fromhex(text)
    res = []
    for i in range(2, 41):
        res.append(
            (
                i,
                hamming_distance(
                    text[:i],
                    text[i:i*2]
                )
            )
        )
    res.sort(key=lambda x: x[1], reverse=True)
    key_size = res[:10]
    return key_size


def get_text():
    text = get('https://cryptopals.com/static/challenge-data/6.txt').text
    return b64decode(text)


def hamming_distance(string_1, string_2):
    assert len(string_1) == len(string_2)
    result = sum(hamming_bits(c1, c2) for c1, c2 in zip(string_1, string_2))
    return result


def hamming_bits(char_1, char_2):
    c_1 = ord(char_1) if type(char_1) == str else char_1
    c_2 = ord(char_2) if type(char_2) == str else char_2
    result = Counter(bin(c_1 ^ c_2)).get('1')
    if result is None:
        return 0
    else:
        return result


def main():
    possible_pt = []

    text = get_text()
    possible_key_sizes = [x[0] for x in search_keysize(text.hex())]

    for keysize in possible_key_sizes:
        key = b''

        for i in range(keysize):
            block = b''

            for j in range(i, len(text), keysize):
                block += bytes([text[j]])
            
            key += bytes([bruteforce_binary_string(block)['key']])
        possible_pt.append((repeating_xor_key(text, key), key))

    result = max(possible_pt, key=lambda k: check_english(k[0]))
    return result


if __name__ == '__main__':
    test1 = 'this is a test'
    test2 = 'wokka wokka!!!'

    print("That's work!") if hamming_distance(test1, test2) == 37 else Exception

    answer = main()
    print('key: {}\n=======\n{}'.format(
        answer[1], answer[0].decode()
    ))
