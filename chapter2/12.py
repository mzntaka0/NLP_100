# -*- coding: utf-8 -*-
"""
NLP100 12/99
"""
import subprocess

def extract_col(txt_file_path, col):
    with open(txt_file_path, 'r') as f:
        line_list = f.readlines()
    with open('../data/outputs/col{}.txt'.format(col), 'w') as f:
        for line in line_list:
            f.write(line.split('\t')[col-1] + '\n')





if __name__ == '__main__':
    txt_file_path = '../data/hightemp.txt'
    extract_col(txt_file_path, 1)
    extract_col(txt_file_path, 2)

    subprocess.call('cut -f 1 < ../data/hightemp.txt', shell=True)
    subprocess.call('cut -f 2 < ../data/hightemp.txt', shell=True)

