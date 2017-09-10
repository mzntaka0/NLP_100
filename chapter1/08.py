# -*- coding: utf-8 -*-
"""
NLP100 08/99
"""

def cipher(literals):
    enc = ''
    for literal in literals:
        if 97 <= ord(literal) <= 122:
            enc += chr(219 - ord(literal))
        else:
            enc += literal
    return enc



if __name__ == '__main__':
    literals = input('input literals: ')
    print(cipher(literals))
    print(cipher(cipher(literals)))

