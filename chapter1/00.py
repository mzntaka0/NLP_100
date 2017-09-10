# -*- coding: utf-8 -*-
"""
NLP100 00/99
"""


def reverse_strings(strings):
    return strings[::-1]

if __name__ == '__main__':
    strings = 'stressed'
    inv_strings = reverse_strings(strings)
    print(inv_strings)
