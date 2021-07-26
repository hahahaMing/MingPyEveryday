'''
Author: your name
Date: 2021-06-26 11:01:28
LastEditTime: 2021-07-26 16:46:26
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
    for file in os.listdir(path):
        if file.endswith('.jpg'):
            file_list.append(file)
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
    print("获取图片" + folder_path + "/" + img_list[0] + "的尺寸作为视频尺寸。")
    img = cv2.imread(folder_path + "/" + img_list[0])
    img_size = (img.shape[1], img.shape[0])
    #保存视频的路径
    save_path = folder_path + '.mp4'
    # 编码器
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    video_writer = cv2.VideoWriter(save_path, fourcc, fps, img_size)
    # 命令行显示进度条
    strarrs = ['/', '|', '\\']
    for i, file in enumerate(img_list):
        sys.stdout.write(strarrs[i % 3] +
                         '{}/{}:'.format(i + 1, len(img_list)) +
                         '#' * int(i / (len(img_list) / 50)) + '\r')
        img = cv2.imread(folder_path + "/" + file)
        video_writer.write(img)
        sys.stdout.flush()

    video_writer.release()
    print("create video done.")


def recurtion_create_videos(root_path):
    folders = os.listdir(root_path)
    print("find flies in :" + root_path)
    print(folders)
    for folder in folders:
        folder = root_path + '/' + folder
        if os.path.isdir(folder):
            if len(get_images(folder)) == 0:
                recurtion_create_videos(folder)
            else:
                create_video(folder)


def main():
    recurtion_create_videos(os.getcwd())
    os.system("pause")


if __name__ == "__main__":
    main()
