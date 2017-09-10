# -*- coding: utf-8 -*-
"""
NLP100 19/99
"""
from collections import Counter
import subprocess


def sort_by_count(txt_file_path, col_num=1):
    with open(txt_file_path, 'r') as f:
        #line_list = map(lambda l: l.rstrip('\n').split('\t'), f.readlines())
        line_list = f.readlines()
    col1_list = [l.split()[0] for l in line_list]

    counted_dict = Counter(col1_list)
    for word, cnt in counted_dict.most_common():
        print(cnt, word)


if __name__ == '__main__':
    txt_file_path = '../data/hightemp.txt'

    sort_by_count(txt_file_path, 1)

    check_cmd = 'cut -f 1 < {}|sort| uniq -c| sort -k1 -r'.format(txt_file_path)
    subprocess.call(check_cmd, shell=True)
