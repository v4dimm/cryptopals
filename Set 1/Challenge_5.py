#!/usr/bin/env python3

from Challenge_2 import xor_strings

def convert_key(string, key):
    string_length = len(string)
    key_length = len(key)
    key = key * round(
        string_length/key_length
    )
    return key[:string_length]


def xor_with_key(string, key):
    b_convert_key = convert_key(string, key).encode()
    b_string = string.encode()

    result = xor_strings(b_convert_key, b_string)
    return bytes.hex(result)


if __name__ == "__main__":

    text = '''Burning 'em, if you ain't quick and nimble
    I go crazy when I hear a cymbal'''

    key = 'ICE'

    print(xor_with_key(text, key))