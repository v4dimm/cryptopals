#!/usr/bin/env python3

def xor_hex_strings(s1, s2):
    if len(s1) == len(s2):
        hex_s1 = int(s1, 16)
        hex_s2 = int(s2, 16)
        xor = hex_s1 ^ hex_s2

        return hex(xor)[2:]

if __name__ == '__main__':
    s1 = b'1c0111001f010100061a024b53535009181c'
    s2 = b'686974207468652062756c6c277320657965'

    result = xor_hex_strings(s1, s2)
    if result == '746865206b696420646f6e277420706c6179':
        print('Result: {}'.format(result))