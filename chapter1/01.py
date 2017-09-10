# -*- coding: utf-8 -*-
"""
NLP100 01/99
"""

def skip_strings(strings, skip_num):
    return strings[::skip_num]


if __name__ == '__main__':
    strings = 'パタトクカシーー'
    skipped_strings = skip_strings(strings, 2)
    print(skipped_strings)

