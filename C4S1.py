#!/usr/bin/env python3

from C3S1 import bruteforce_string
from requests import get

strings = get('https://cryptopals.com/static/challenge-data/4.txt').text.split('\n')
res = []
for text in strings:
    b_string = bruteforce_string(text)
    if (b_string is not None):
        res.append(b_string)

[print('=>', result, '\n') for result in res]