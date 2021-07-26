'''
Author: your name
Date: 2021-06-26 11:01:28
LastEditTime: 2021-06-26 14:19:45
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \MingPyEveryday\v18_jpg2mp4.py
'''
'''
此脚本功能：
1.检测脚本所在文件夹内是否含有图片
2.以文件夹为名字，文件夹内图片为资源创建视频文件写到脚本所在文件夹
3.没了啦啦啦
'''

import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import cv2


def get_images(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        if not files:
            continue
        for file in files:
            if file.endswith('.jpg'):
                file_list.append(os.path.join(root, file))
                #file_list.append(file)
    return file_list


def create_video(folder_path):
    img_list = get_images(folder_path)
    if len(img_list) == 0:
        return
    print("creating video in: " + folder_path)
    img_list.sort()
    #一秒25帧，代表1秒视频由25张图片组成
    fps = 25
    #视频分辨率
    img = cv2.imread(img_list[0])
    img_size = (img.shape[1], img.shape[0])
    #保存视频的路径
    save_path = folder_path + '.mp4'
    # 编码器
    # fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
    # fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    # fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(save_path, fourcc, fps, img_size)
    strarrs = ['/', '|', '\\']
    for i, file in enumerate(img_list):
        sys.stdout.write(strarrs[i % 3] + '{}/{}:'.format(i+1,len(img_list)) +
                         '#' * int(i / (len(img_list) / 50)) + '\r')
        img = cv2.imread(file)
        video_writer.write(img)
        sys.stdout.flush()
    video_writer.release()
    print("create video done.")


def main():
    folders = os.listdir()
    print(folders)
    for folder in folders:
        if os.path.isdir(folder):
            create_video(folder)
    os.system("pause")


if __name__ == "__main__":
    main()
