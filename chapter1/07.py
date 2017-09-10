# -*- coding: utf-8 -*-
"""
NLP100 07/99
"""

def template(x, y, z):
    return '{}時の{}は{}'.format(x, y, z)


if __name__ == '__main__':
    x = 12
    y = "気温"
    z = 22.4

    print(template(x, y, z))

