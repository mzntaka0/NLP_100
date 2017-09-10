# -*- coding: utf-8 -*-
"""
NLP100 06/99
"""

def n_gram(seq, n=2):
    n_gram_list = list()
    for i in range(len(seq)-n+1):
        n_gram_list.append(
                seq[i:i+n]
                )
    return n_gram_list


if __name__ == '__main__':
    seq1 = "paraparaparadise"
    seq2 = "paragraph"

    X = set(n_gram(seq1))
    Y = set(n_gram(seq2))

    sum_set = X | Y
    sub_set = X - Y
    inter_set = X & Y
    print(sum_set)
    print(sub_set)
    print(inter_set)
    if 'se' in X:
        print('"se" is in X')
    else:
        print('"se" is not in X')
    if 'se' in Y:
        print('"se" is in Y')
    else:
        print('"se" is not in Y')

