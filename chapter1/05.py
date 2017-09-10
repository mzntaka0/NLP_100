# -*- coding: utf-8 -*-
"""
NLP100 05/99
"""
import re

def _split_sentence(sentence):
    splited_sentence =  re.split('\W', sentence)
    return list(filter(lambda s: s != '', splited_sentence))


def n_gram(seq, n=2):
    n_gram_list = list()
    for i in range(len(seq)-n+1):
        n_gram_list.append(
                seq[i:i+n]
                )
    return n_gram_list


if __name__ == '__main__':
    seq = "I am an NLPer"
    literal_bi_gram = n_gram(seq)

    splited_sentence = _split_sentence(seq)
    word_bi_gram = n_gram(splited_sentence)

    print(literal_bi_gram)
    print(word_bi_gram)

