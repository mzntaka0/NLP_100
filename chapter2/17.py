# -*- coding: utf-8 -*-
"""
NLP100 17/99
"""
import subprocess

def uniq_col_set(txt_file_path):
    with open(txt_file_path, 'r') as f:
        line_list = f.readlines()
    col1_list = [col1.split('\t')[0] for col1 in line_list]
    print(set(col1_list))


if __name__ == '__main__':
    txt_file_path = '../data/hightemp.txt'
    uniq_col_set(txt_file_path)

    check_cmd = 'cut -f 1 < {}| sort| uniq'.format(txt_file_path)
    subprocess.call(check_cmd, shell=True)
