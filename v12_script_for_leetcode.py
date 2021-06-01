#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 15:02
# @Author  : Eiya_ming
# @Email   : eiyaming@163.com
# @File    : v12_script_for_leetcode.py
import requests
import os
import re
import time

class LEETCODE():
    def __init__(self,url:str):
        self.url = url

    def extract_data(self):
        r = requests.get(self.url)
        s = r.text
        with open("assets/v12/test.html",'w',encoding='utf-8')as f:
            f.write(s)

        tmp = re.findall('.*.js.*', s)
        for it in tmp:
            print(it)


if __name__ == '__main__':
    print("请输入力扣题目页面url：")
    # url = input()
    url = "https://leetcode-cn.com/problems/divide-two-integers/"
    lc = LEETCODE(url)
    lc.extract_data()
