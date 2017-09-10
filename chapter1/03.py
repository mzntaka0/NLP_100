# -*- coding: utf-8 -*-
"""
NLP100 03/99
"""
import re

def _split_sentence(sentence):
    splited_sentence =  re.split('\W', sentence)
    return list(filter(lambda s: s != '', splited_sentence))

def count_literals(sentence):
    splited_sentence = _split_sentence(sentence)
    return [len(word) for word in splited_sentence]


if __name__ == '__main__':
    sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics." 
    literal_counted_list = count_literals(sentence)
    print(literal_counted_list)

