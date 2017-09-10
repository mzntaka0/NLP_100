# -*- coding: utf-8 -*-
"""
NLP100 09/99
"""
import re
import random

def _split_sentence(sentence):
    splited_sentence =  sentence.replace(',', '').replace('.', '').split(' ')
    return list(filter(lambda s: s != '', splited_sentence))


def randomize_inner_literals(sentence):
    splited_sentence = _split_sentence(sentence)
    randomized_words_list = []
    for word in splited_sentence:
        if len(word) > 4:
            literal_list = list(word[1:-1])
            random.shuffle(literal_list)
            randomized_words_list.append(
                    word.replace(word[1:-1], ''.join(literal_list))
                    )
        else:
            randomized_words_list.append(word)
    return ' '.join(randomized_words_list)




if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(randomize_inner_literals(sentence))

