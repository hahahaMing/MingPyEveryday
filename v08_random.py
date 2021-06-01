#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/7 19:02
# @Author  : Eiya_ming
# @Email   : eiyaming@163.com
# @File    : v08_random.py

# 迭代取中法


s = 2
xn = 12345


def r1():
    global xn
    xn = xn ** 2 / 10 ** s % (10 ** (2 * s))
    return xn / (10 ** (2 * s))


for i in range(100):
    print(r1())
