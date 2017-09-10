# -*- coding: utf-8 -*-
"""
NLP100 14/99
"""
import sys
import subprocess

def head(txt_file_path, N=5):
    with open(txt_file_path, 'r') as f:
        line_list = list(map(lambda l: l.rstrip('\n'), f.readlines()))
        for i in range(N):
            print(line_list[i])


if __name__ == '__main__':
    try:
        N = int(sys.argv[1])
    except IndexError:
        print('please set num to arg1')
        sys.exit(1)

    txt_file_path = '../data/hightemp.txt'
    head(txt_file_path, N)

    check_cmd = 'head -n {} {}'.format(N, txt_file_path)
    subprocess.call(check_cmd, shell=True)


