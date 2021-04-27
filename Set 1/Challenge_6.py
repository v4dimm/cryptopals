#!/usr/bin/env python3

from itertools import zip_longest
from collections import Counter

def hamming_distance(string_1, string_2):
    assert len(string_1) == len(string_2)
    result = sum(hamming_bits(c1, c2) for c1, c2 in zip(string_1, string_2))
    return result

def hamming_bits(char_1, char_2):
    c_1 = ord(char_1)
    c_2 = ord(char_2)
    result = Counter(bin(c_1 ^ c_2)).get('1')
    return result


if __name__ == '__main__':
    test1 = 'this is a test'
    test2 = 'wokka wokka!!!'

    print("That's work!") if hamming_distance(test1, test2) == 37 else Exception