#!/usr/bin/env python3
import array
import operator

def xor_strings(s1, s2):
    if len(s1) == len(s2):
        _s1 = array.array('B', s1)
        _s2 = array.array('B', s2)
        result = array.array('B', map(operator.xor, _s1, _s2)).tobytes()
        return result
    else:
        return ''

if __name__ == '__main__':
    s1 = u'1c0111001f010100061a024b53535009181c'
    s2 = u'686974207468652062756c6c277320657965'

    _s1 = bytes.fromhex(s1)
    _s2 = bytes.fromhex(s2)

    result = xor_strings(_s1, _s2)
    print('Result: {}'.format(result))