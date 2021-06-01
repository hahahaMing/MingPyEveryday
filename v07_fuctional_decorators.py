#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 10:38
# @Author  : Eiya_ming
# @Email   : eiyaming@163.com
# @File    : v07_fuctional_decorators.py

import time


def deco(f):
    start_time = time.time()
    f()
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("time is %d ms" % execution_time)


def f():
    print("hello")
    time.sleep(1)
    print("world")


def fake_change(a):
    a = 456


def main():
    a = 1

    @deco
    def change():
        global a
        time.sleep(1)
        a = 2

    change

    print(a)


if __name__ == '__main__':
    main()
