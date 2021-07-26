'''
Author: your name
Date: 2021-06-18 10:16:11
LastEditTime: 2021-06-18 11:04:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \MingPyEveryday\v16_photo_process.py
'''
import cv2

input_image = r'assets\v16\2.jpg'


def access_pixels(frame):
    print(frame.shape)  #shape内包含三个元素：按顺序为高、宽、通道数
    height = frame.shape[0]
    weight = frame.shape[1]
    channels = frame.shape[2]
    print("weight : %s, height : %s, channel : %s" %
          (weight, height, channels))

    for row in range(height):  #遍历高
        for col in range(weight):  #遍历宽
            total = 0
            a, b, c = frame[row, col]

            # for c in range(channels):  #便利通道
            #     pv = frame[row, col, c]
            #     # print(pv)
            #     # frame[row, col, c] = 255 - pv     #全部像素取反，实现一个反向效果
            #     total += pv
            if abs(int(a) - int(b)) + abs(int(b) -
                                          int(c)) + abs(int(a) - int(c)) < 70:
                frame[row, col] = [255, 255, 255]
    cv2.imwrite(r'assets\v16\3.jpg', frame)
    cv2.imshow("fanxiang", frame)


im = cv2.imread(input_image)
cv2.imshow("img", im)

access_pixels(im)

cv2.waitKey(0)
