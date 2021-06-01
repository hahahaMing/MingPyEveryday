#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 9:33
# @Author  : Eiya_ming
# @Email   : eiyaming@163.com
# @File    : v11_script_for_vector.py

def change_vector_str(s):
    s = s.replace('[', '{')
    s = s.replace(']', '}')
    print(s)


if __name__ == '__main__':
    while (1):
        s = ''
        s = input(s)
        if s == '': break
        change_vector_str(s)
