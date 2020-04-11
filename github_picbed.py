#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 16:45
# @Author  : Eiya_ming
# @Email   : eiyaming@163.com
# @File    : github_picbed.py

# github图床（码云）
# 1. github图床建立
# 2. 脚本实现现有文档转换（注意备份）（转换当前leetcode.md）
# 3. 建立gitee图床
# 4. 同2
# 5. 搞定了写CSDN
# 6. 有空把公式也变成图片上传，这样github可以看。


"""
以leetcode为例
1. 备份文档到图床文件夹
2. push
3. 获得url
4. 备份md文件
5. 将md文件中的本地图片更新为线上图片
6. ui制作（1选择源图片目录；2选择备份md文件）
"""
import os, shutil
from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.filedialog


class PicBed():

    def __init__(self):
        self.folder = ''
        self.file = ''
        self.asset = StringVar()
        self.localbed = StringVar()
        self.md = StringVar()
        self.bed_head = 'E:/self_study/git/MyImage/'
        self.url_head = 'https://raw.githubusercontent.com/hahahaMing/MyImage/master/'
        self.folder_name = ''

    def selectPath(self):
        self.folder = askdirectory()
        self.asset.set(self.folder)
        self.folder_name = self.folder.split('/')[-1]

    def select_localbed_Path(self):
        self.bed_head = askdirectory()
        self.localbed.set(self.bed_head)
        self.bed_head += '/'

    def selectFile(self):
        self.file = tkinter.filedialog.askopenfilename()
        self.md.set(self.file)

    def copy_upload(self):
        files = os.listdir(self.folder)
        for f in files:
            mymovefile(self.folder + '/' + f, self.bed_head + self.folder_name + '/' + f)
        print('move ok')
        # todo: push



def interface():
    root = Tk()
    bed = PicBed()
    # row0
    Label(root, text="asset目标路径:").grid(row=0, column=0)
    Entry(root, textvariable=bed.asset).grid(row=0, column=1)
    Button(root, text="路径选择", command=bed.selectPath).grid(row=0, column=2)
    # row1
    Label(root, text=".md目标位置:").grid(row=1, column=0)
    Entry(root, textvariable=bed.md).grid(row=1, column=1)
    Button(root, text="位置选择", command=bed.selectFile).grid(row=1, column=2)
    # row2
    # Label(root, text="bed仓库本地路径:").grid(row=2, column=0)
    # Entry(root, textvariable=bed.localbed).grid(row=2, column=1)
    # Button(root, text="路径选择", command=bed.select_localbed_Path).grid(row=2, column=2)
    # row2
    Button(root, text="复制&上传", command=bed.copy_upload).grid(row=2, column=0)

    root.mainloop()


def mymovefile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.move(srcfile, dstfile)  # 移动文件
        print("move %s -> %s" % (srcfile, dstfile))


# interface()
cmd = 'cd E:\self_study\git\MyImage'
os.system(cmd)
# os.system('mkdir test')
cmd = 'git push'
res = os.popen(cmd)
print(res.read())