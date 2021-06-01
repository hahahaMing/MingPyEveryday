#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 19:34
# @Author  : Eiya_ming
# @Email   : eiyaming@163.com
# @File    : v06_parser_test.py
'''start'''

# 1引入模块
import argparse

# 2建立解析对象
parser = argparse.ArgumentParser()

# 3增加属性：给xx实例增加一个aa属性 # xx.add_argument("aa")
parser.add_argument("--e_ho")
parser.add_argument("ec_ho")
# 4属性给与args实例： 把parser中设置的所有"add_argument"给返回到args子类实例当中， 那么parser中增加的属性内容都会在args实例中，使用即可。
args = parser.parse_args()
parser.parse_args()

# 打印定位参数echo
print(args)
