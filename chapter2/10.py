# -*- coding: utf-8 -*-
"""
NLP100 10/99
"""
import subprocess

def count_line_num(txt_file_path):
    with open(txt_file_path, 'r') as f:
        line_list = f.readlines()
    print(len(line_list))


if __name__ == '__main__':
    txt_file_path = '../data/hightemp.txt'
    count_line_num(txt_file_path)

    subprocess.call('wc -l {}'.format(txt_file_path), shell=True)

