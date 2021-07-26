'''
Author: your name
Date: 2021-06-26 09:55:23
LastEditTime: 2021-06-26 10:56:18
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \MingPyEveryday\v17_pdf_merge.py
这里先将所有文件打印为A4大小pdf
然后自行创建文件名进行排序合并
有修改PyPDF2的strict模式
'''
import os
import re
from PyPDF2 import PdfFileMerger

target_path = r'assets\v17\m1'
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]


# Chinese to English
def lm_find_unchinese(file):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    unchinese = re.sub(pattern, "", file)  #排除汉字
    print("unchinese:", unchinese)
    return unchinese

file_merger = PdfFileMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)  # 合并pdf文件

file_merger.write(os.path.join(target_path,"m1.pdf"))