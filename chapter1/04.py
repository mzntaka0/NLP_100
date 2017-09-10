# -*- coding: utf-8 -*-
"""
NLP100 04/99
"""
import re

def _split_sentence(sentence):
    splited_sentence =  re.split('\W', sentence)
    return list(filter(lambda s: s != '', splited_sentence))

def _extract_literals(word, ext_num):
    return word[:ext_num]

def extract_element_symbol(sentence):
    extract_one_idx = [0, 4, 5, 6, 7, 8, 14, 15, 18]
    splited_sentence = _split_sentence(sentence)
    extract_num_list = [2] * len(splited_sentence)
    for i in extract_one_idx:
        extract_num_list[i] = 1
    return {_extract_literals(word, ext_num): i
            for (i, word), ext_num in zip(enumerate(splited_sentence), extract_num_list)}




if __name__ == '__main__':
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

    element_list = extract_element_symbol(sentence)
    print(element_list)
