#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 14:03
# @Author  : Eiya_ming
# @Email   : eiyaming@163.com
# @File    : v14_split_leecode_text.py

"""
这波拆分力扣文档到单独的文件
重点是题目文件

首先题目去除链接，作为文件名
整体文本直接写入

更改新生成的文件，统一格式为中文文件名，图片统一放在assets文件夹中

"""
import re
import os

# 读原始文件
with open('assets/v14/leetcode.md', 'r', encoding='utf-8')as f:
    origin_str = f.read()
# 分割题目部分
# ques_str = origin_str.split('# 刷 leetcode 记录')[1].split('# 竞赛')[0]
ques_str = origin_str.split('# 竞赛')[1]
ques_str = ques_str.replace('# **还没做出来。。。**','')
# 更改图片文件位置
ques_str = ques_str.replace('leetcode.assets','assets')
# 分割为单个题目
ques_list = ques_str.split('\n## ')

# 单个写入文件
for text in ques_list:
    if len(text) > 100:
        title = text.split('\n')[0]

        # 对于title：
        # 去空格
        title = title.replace(' ', '')
        # 去链接
        title = title.replace('[', '')
        title = title.replace(']', '')
        title = re.sub('\(.*\)', '', title)

        # 写入文件
        with open('assets/v14/'+title+'.md','w',encoding='utf-8')as f:
            f.write('# '+text)
        print(title)

# # 读入notes的.md文件
# file_list = os.listdir('assets/v14/notes')
# for file in file_list:
#     if file.find('md')!=-1:
#         with open('assets/v14/notes/'+file,'r',encoding='utf-8')as f:
#             file_text = f.read()
#         # 更改文件指向
#         file_text = re.sub('\(.*\.assets/','(assets/',file_text)
#
#
#         title = file_text.split('\n')[0]
#         title = title.replace('# ','')
#         title = title.replace(' ', '')
#         # 写入新文件
#         with open('assets/v14/'+title+'.md','w',encoding='utf-8')as f:
#             f.write(file_text)
#
#         print(title)


