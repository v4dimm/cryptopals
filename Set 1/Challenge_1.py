#!/usr/bin/env python3

from base64 import b64encode

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

print('Result: {}'.format(b64encode(bytes.fromhex(hex_string)).decode('utf-8')))