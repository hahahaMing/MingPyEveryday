'''
Author: your name
Date: 2021-07-19 23:22:59
LastEditTime: 2021-07-19 23:33:11
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \MingPyEveryday\v21_binary_image.py
'''
# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


path = "1.jpg"


#图像二值化 0白色 1黑色
#全局阈值
def threshold_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("原来", gray)


    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)# 自定义阈值为150,大于150的是白色 小于的是黑色
    print("阈值：%s" % ret)
    cv.imshow("自定义", binary)

src = cv.imread(path)
cv.imshow("a",src)
threshold_image(src)
cv.waitKey(0)
cv.destroyAllWindows()