# -*- coding: utf-8 -*-
"""
NLP100 18/99
"""
import subprocess

def sort_by(txt_file_path, col_num=3):
    with open(txt_file_path, 'r') as f:
        line_list = map(lambda l: l.rstrip('\n').split('\t'), f.readlines())
        line_list = sorted(line_list, key=lambda l: l[col_num-1], reverse=True)

    for line in line_list:
        print(' '.join(line))





if __name__ == '__main__':
    txt_file_path = '../data/hightemp.txt'

    sort_by(txt_file_path, 3)

    check_cmd = 'cat {}| sort -k3 -r '.format(txt_file_path)
    subprocess.call(check_cmd, shell=True)
