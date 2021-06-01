#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 11:18
# @Author  : Eiya_ming
# @Email   : eiyaming@163.com
# @File    : v09_delete_pdf_watermark.py

import PyPDF2
import fitz
import time
import re
import os
import sys
import os
from PIL import Image
import xml.dom.minidom

import cv2
import numpy as np
import gc
import img2pdf


# input_filepath = 'assets/v09/高等数学 第7版 上册 同济大学.pdf'
# input_filepath = 'assets/v09/高等数学 第7版 下册 同济大学.pdf'
# input_filepath = 'assets/v09/高等数学 同济第7版 上册 习题全解指南 课后习题答案解析.pdf'
input_filepath = 'assets/v09/高等数学 同济第7版 下册 习题全解指南 课后习题答案解析.pdf'



class MingPdfTools(object):
    def __init__(self, input_filepath:str):
        # 输入文件名，分割出名字
        self.input_filepath = input_filepath
        self.project_name = input_filepath.split('/')[-1].replace('.pdf','')
        self.assets_path = input_filepath.replace(self.project_name+'.pdf','')
        self.doc = fitz.open(self.input_filepath)
        self.page_total = len(self.doc)
        self.output_filepath = self.assets_path+self.project_name+'(去水印).pdf'
        self.img_list = []

    def dewatermark(self):
        # 建立文件夹放处理后的图片
        if not os.path.exists(self.assets_path+self.project_name):
            os.mkdir(self.assets_path+self.project_name)
        for i in range(self.page_total):
            self.page_handler(i)
        # 图片写入文件
        with open(self.output_filepath, "wb") as f:
            f.write(img2pdf.convert(self.img_list))
            # for img in self.img_list:
            #     f.write(img2pdf.convert(img))
            #     print(img,'turn to pdf')

    def sharpen(self, input_img, output_img):
        # im = Image.open('assets/v09/10781.png')
        # print(im.getbands() == ('L',))
        im = Image.open(input_img)
        print(im.getbands() == ('L',))

        image = cv2.imread(input_img)
        # print(image.shape[2])
        dst = image
        # 滤波
        # 双边滤波 就是太慢了
        # dst = cv2.bilateralFilter(src=dst, d=0, sigmaColor=100, sigmaSpace=15)
        dst = cv2.blur(dst, (3, 3))
        # 锐化
        # kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], np.float32)
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
        # kernel = np.array([[-0.5, -1, -0.5], [-1, 7, -1], [-0.5, -1, -0.5]], np.float32)
        dst = cv2.filter2D(dst, -1, kernel=kernel)
        # print(dst.shape[2])

        # kernel = np.ones((3, 3), np.uint8)
        # 膨胀
        # dst = cv2.dilate(dst, kernel)
        # 腐蚀
        # dst = cv2.erode(dst, kernel)
        # 闭运算
        # dst = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel)
        # 开运算
        # dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel)
        if im.getbands() == ('L',):
            dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        im.close()
        del im,image
        cv2.imwrite(output_img, dst)
        gc.collect()

    def page_handler(self, p_num):
        page = self.doc[p_num]
        pix = fitz.Pixmap(self.doc, page.getImageList()[0][0])
        # pix.shrink(1)
        # pix.writePNG(assets_path + '/test.png')
        # self.sharpen(assets_path + '/test.png', assets_path + '/images/'+str(p_num)+'.png')
        pix.writePNG(self.assets_path + self.project_name+'/'+str(p_num)+'.png')
        del pix
        self.img_list.append(self.assets_path + self.project_name+'/'+str(p_num)+'.png')
        print(p_num,'图片搞定')
        gc.collect()

    def test(self, p_num):
        # 挑选一页，做一页的相同处理，查看处理结果
        self.page_handler(p_num)
        # self.new_doc.save('assets/v09/test1.pdf')


pdf_tool = MingPdfTools(input_filepath)
pdf_tool.dewatermark()

