# -*- coding: utf-8 -*-
"""
NLP100 02/99
"""

def alter_concat(str1, str2):
    return ''.join([s1+s2 for s1, s2 in zip(str1, str2)])


if __name__ == '__main__':
    str1 = 'パトカー'
    str2 = 'タクシー'

    altconcated_str = alter_concat(str1, str2)
    print(altconcated_str)

