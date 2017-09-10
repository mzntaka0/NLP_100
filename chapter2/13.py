# -*- coding: utf-8 -*-
"""
NLP100 13/99
"""
import subprocess

def merge_cols(txt1_path, txt2_path):
    with open(txt1_path, 'r') as f1, open(txt2_path, 'r') as f2:
        line_list1 = f1.readlines()
        line_list2 = f2.readlines()
        line_list1 = map(lambda l: l.rstrip('\n'), line_list1)
        line_list2 = map(lambda l: l.rstrip('\n'), line_list2)

    with open('../data/outputs/merged13.txt', 'w') as f:
        for l1, l2 in zip(line_list1, line_list2):
            f.write(l1+'\t'+l2+'\n')



if __name__ == '__main__':
    txt1_path = '../data/outputs/col1.txt'
    txt2_path = '../data/outputs/col2.txt'

    merge_cols(txt1_path, txt2_path)

    check_cmd = 'paste {} {} > ../data/outputs/merged_paste.txt'.format(txt1_path, txt2_path)
    subprocess.call(check_cmd, shell=True)

