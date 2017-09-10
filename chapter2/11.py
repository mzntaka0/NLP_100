# -*- coding: utf-8 -*-
"""
NLP100 11/99
"""
import os
import subprocess

def replace_tab_to_space(txt_file_path):
    with open(txt_file_path, 'r') as f:
        line_list = f.readlines()
    line_list = map(lambda s: s.replace('\t', ' '), line_list)
    if not os.path.exists('../data/outputs/'):
        os.makedirs('../data/outputs/')
    with open('../data/outputs/output11.txt', 'w') as f:
        for line in line_list:
            f.write(line)
    subprocess.call('cat ../data/outputs/output11.txt', shell=True)
    print('-'*20)




if __name__ == '__main__':
    txt_file_path = '../data/hightemp.txt'
    replace_tab_to_space(txt_file_path)

    check_cmd = 'expand -t 1 {}'.format(txt_file_path)
    subprocess.call(check_cmd, shell=True)
