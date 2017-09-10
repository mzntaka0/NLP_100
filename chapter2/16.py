# -*- coding: utf-8 -*-
"""
NLP100 16/99
"""
import sys
import subprocess


def split(txt_file_path, N=5):
    with open(txt_file_path, 'r') as f:
        line_list = f.readlines()
        print(''.join(line_list[:N]))
        print(''.join(line_list[N:]))


if __name__ == '__main__':
    try:
        N = int(sys.argv[1])
    except IndexError:
        N = 5
        print('default N=5 has been set')


    txt_file_path = '../data/hightemp.txt'
    split(txt_file_path, N)

    check_cmd = 'split -l {} {}'.format(N, txt_file_path)
    subprocess.call(check_cmd, shell=True)

