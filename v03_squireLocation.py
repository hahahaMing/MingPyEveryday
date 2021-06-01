#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 19:49
# @Author  : Eiya_ming
# @Email   : eiyaming@163.com
# @File    : v03_squireLocation.py

import cv2
import numpy as np

# 内参矩阵
mtx = np.array([[846.70828588, 0., 320.85163712],
                [0., 846.78709765, 238.07367989],
                [0., 0., 1.]])
# 畸变参数
dist = np.array([[-4.13382958e-01, 3.23373302e+00, 1.75643221e-03, 8.44365091e-04,
                  -1.15037692e+01]])


## 内参矩阵与畸变参数使用
def test_undist():
    test_path = 'assets/v03/WIN_20200415_10_20_40_Pro.jpg'
    img = cv2.imread(test_path)
    dst = cv2.undistort(img, mtx, dist)
    cv2.imshow('image', img)
    cv2.imshow('dst', dst)
    cv2.waitKey()


## 找到角点
def find_corners():
    min_area = 640 * 480 * 0.001
    max_area = 640 * 480 * 0.8

    # 1. 读入图片并正畸
    test_path = 'assets/v03/WIN_20200422_13_02_30_Pro.jpg'
    img = cv2.imread(test_path)
    rows,cols,channel = img.shape

    dst = cv2.undistort(img, mtx, dist)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', gray)

    # 2. 找到角点
    ret, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 轮廓检测
    approx = []
    for i in contours:  # 轮廓筛选
        if min_area < cv2.contourArea(i) < max_area:
            # 多边形拟合
            epsilon = 0.02 * cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, epsilon, True)
            # print(approx)
            break
    # 绘制角点
    img = cv2.drawContours(img, approx, -1, (255, 0, 100), 3)  # 如果“approx”不加上“[ ]”画出来的是拟合后的点
    # 3.坐标变换
    # 求中点图像坐标
    center = np.mean(approx,axis=0)[0]
    cv2.circle(img, (int(center[0]), int(center[1])), 1, (0,0,255), 4)#绘制中点
    dst_points = np.array([[0,0],[20,0],[20,20],[0,20]])
    M,mask=cv2.findHomography(approx,dst_points)
    perspective = cv2.warpPerspective(img,M,(20,20))
    ## test
    # approx=np.reshape(approx,(4,2)).astype(np.float32)
    # dst_points = dst_points.astype(np.float32)
    # print(approx)
    # print(dst_points)
    # M_ = cv2.getPerspectiveTransform(approx,dst_points)
    # print(M)
    # # print(type(approx))
    # # print(np.float32([[1,2],[2,3],[3,4]]))
    # one = np.array([[1.],[1.],[1.],[1.]])
    # c = np.c_[approx,one]
    # c=c.T
    # c=np.matmul(M_,c)
    # print(c)
    #
    #
    ans = np.matmul(np.linalg.inv(mtx),np.linalg.inv(M))

    ret1, mtx1, dist1, rvecs1, tvecs1 = cv2.calibrateCamera(world_position, image_position, gray.shape[::-1], None, None)

    print(ans)
    cv2.imshow("img", img)
    cv2.imshow("perspective", perspective)
    cv2.waitKey()
    pass


find_corners()
