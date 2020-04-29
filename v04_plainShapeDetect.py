#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 8:48
# @Author  : Eiya_ming
# @Email   : eiyaming@163.com
# @File    : v04_plainShapeDetect.py

'''
作业

步骤：
1. 拍一张照片
2. 找到其中的形状，标示出来
3. 写几个函数，判断几个角点出来是不是：三角形、正方形、长方形、梯形，(并给出相似度，再说)
4. 将结果显示在图片上
5. 统计运行时间（ms为单位）
6. 将其中几个函数弄明白
7. 写 csdn
8. 如果时间效果还可以，视频试试
'''
# 找抽风椭圆原因  轮廓提取结果分散，fitEllipse会抽风（没包住轮廓点，只是和轮廓挨着）


import cv2
import numpy as np
import math
import datetime

# 内参矩阵
mtx = np.array([[846.70828588, 0., 320.85163712],
                [0., 846.78709765, 238.07367989],
                [0., 0., 1.]])
# 畸变参数
dist = np.array([[-4.13382958e-01, 3.23373302e+00, 1.75643221e-03, 8.44365091e-04,
                  -1.15037692e+01]])


# 形状判断函数组： 暂不考虑角点数量判断错误
def parallelism(A: np.ndarray, B: np.ndarray, C: np.ndarray, D: np.ndarray) -> float:
    """
    :param A, B, C, D: points' coordinates.shape(1,2)
    :return: probability of AB parallel to CD.
    """
    eps = 0.000001
    ab = (B - A)[0]
    cd = (D - C)[0]
    k1 = ab[1] / (ab[0] + eps)
    k2 = cd[1] / (cd[0] + eps)
    a1 = math.atan(k1)
    a2 = math.atan(k2)
    if a1 > a2: a1, a2 = a2, a1
    differ = a2 - a1 if a2 - a1 < math.pi / 2 else a1 - a2 + math.pi
    return 1. - 2 * differ / math.pi
    # print(differ)


def verticality(A: np.ndarray, B: np.ndarray, C: np.ndarray, D: np.ndarray) -> float:
    """
        :param A, B, C, D: points' coordinates.shape(1,2)
        :return: probability of AC perpendicular to BD.!!!!!!!  AC  BD !!!!!!
    """
    eps = 0.000001
    ac = (C - A)[0]
    bd = (D - B)[0]
    k1 = ac[1] / (ac[0] + eps)
    k2 = bd[1] / (bd[0] + eps)
    a1 = math.atan(k1)
    a2 = math.atan(k2)
    if a1 > a2: a1, a2 = a2, a1
    differ = math.fabs(a2 - a1 - math.pi / 2)
    return 1. - 2 * differ / math.pi


def shape4points(approx: np.ndarray) -> [str, float]:
    """
    todo :
    :param approx: shape(4,1,2)
    :return: shape type , similarity:0~1
    """
    p_ts = 0.8  # threshold value

    A, B, C, D = approx
    # print(A,B,C,D)
    p1 = parallelism(A, B, C, D)
    p2 = parallelism(B, C, D, A)
    if p1 > p_ts or p2 > p_ts:
        if p1 > p_ts and p2 > p_ts:
            v = verticality(A, B, C, D)
            if v > p_ts:
                return 'square', p1 * p2 * v
            else:
                return 'rectangle', p1 * p2
        else:
            return 'trapezoid', max(p1, p2)
    else:
        return 'unknown', 1.


def find_shapes(img):
    # old = img.copy()  #  error test
    # blank = np.zeros(img.shape)
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化
    dst = cv2.filter2D(img, -1, kernel=kernel)
    # img = cv2.blur(img, (3, 3))
    rows, cols, channel = img.shape
    '''**********************参数设置**********************'''
    # 定义检测面积范围
    min_area = rows * cols * 0.001
    max_area = rows * cols * 0.6
    # 椭圆检测阈值
    th_ell = 0.98
    # 字体大小
    fort_size = 0.5
    # 二值化阈值系数
    p_thresh = 0.4
    # 多边形拟合相似度系数
    smlt = 0.03
    '''**********************开始操作**********************'''
    # img = cv2.undistort(img, mtx, dist)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)  # 使用锐化
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 不使用锐化

    pixel_thresh = cv2.mean(gray)[0] * p_thresh  # 均值寻找阈值
    ret, thresh = cv2.threshold(gray, pixel_thresh, 255, cv2.THRESH_BINARY)  # 二值化

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 轮廓检测

    for i in contours:  # 轮廓筛选
        S = cv2.contourArea(i)
        if min_area < S < max_area:  # 面积筛选
            shape = 'unknown'
            p_shp = 1.
            # 圆形与椭圆检测
            ell = cv2.fitEllipse(i)
            '''这里应对一种cv2椭圆包错地方的自带bug'''
            a, b = ell[1][0], ell[1][1]
            if a < b: a, b = b, a
            S2 = math.pi * a * b / 4
            M = cv2.moments(i)
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])
            if (S / S2) > th_ell and 1 - (pow(center_x - ell[0][0], 2) + pow(center_y - ell[0][1], 2)) / a / b > th_ell:
                # print((pow(center_x - ell[0][0], 2) + pow(center_y - ell[0][1], 2)) / a / b)
                if b / a > 0.9:
                    # todo 圆
                    shape = 'circle'
                    p_shp = b / a
                else:
                    # todo 椭圆
                    shape = 'ellipse'
                    p_shp = th_ell
                    # 抽风椭圆检测
                    # count += 1
                    # if count > 1:
                    # #     cv2.imwrite('assets/v04/error.jpg', old)
                    # if count ==1:
                    #     rect = cv2.minAreaRect(i)  # 最小外接矩形
                    #     box = np.int0(cv2.boxPoints(rect))  # 矩形的四个角点取整
                    #     cv2.drawContours(blank, [box], 0, (255, 0, 0), 2)
                    # print(cv2.arcLength(i, True))
                    # print(math.pi*(1.5*(a+b)-math.sqrt(a*b)))
                    # blank= cv2.drawContours(blank, i, -1, (255, 0, 100), 3)
                    # blank = cv2.ellipse(blank, ell, (0, 255, 0), 2)
                img = cv2.ellipse(img, ell, (0, 255, 0), 2)
            # 非圆形检测
            else:
                # 多边形拟合
                epsilon = smlt * cv2.arcLength(i, True)  # 拟合精度--点到拟合线的最大距离
                approx = cv2.approxPolyDP(i, epsilon, True)
                # print(approx)
                # print(approx.shape)
                # print('---------------------------------')
                img = cv2.drawContours(img, [approx], -1, (255, 0, 100), 3)  # 如果“approx”不加上“[ ]”画出来的是拟合后的点
                # 如果点数为3 为三角形
                if approx.shape[0] == 3:
                    # todo  三角形操作
                    shape = 'triangle'
                    p_shp = 1.
                elif approx.shape[0] == 4:
                    # todo 四边形
                    shape, p_shp = shape4points(approx)
                else:
                    shape = 'polygon'
                    pass
            p_shp = round(p_shp, 3)
            cv2.putText(img, shape + ' ' + str(p_shp), (i[0][0][0], i[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, fort_size,
                        (255, 255, 0), 2)
            # cv2.imshow('blank',blank)
            # cv2.imshow('thresh', thresh)


def camera_shape_dtct():
    cap = cv2.VideoCapture(0)
    while (True):
        # 获取摄像头拍摄到的画面
        ret, frame = cap.read()
        img = frame
        find_shapes(img)
        # 实时展示效果画面
        cv2.imshow('frame2', img)
        # 每5毫秒监听一次键盘动作
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break


'''时长测试 需要注释掉cv2.waitKey()'''
##0:00:00.015382
# start = datetime.datetime.now()
# # test_path = 'assets/v04/WIN_20200429_17_13_48_Pro.jpg'
# test_path = 'assets/v04/error.jpg'
# img = cv2.imread(test_path)
# find_shapes(img)
# end = datetime.datetime.now()
# print(end - start)
# cv2.imshow('img', img)
# cv2.waitKey()
# todo 视频测试
camera_shape_dtct()
