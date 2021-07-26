'''
Author: your name
Date: 2021-06-26 15:07:01
LastEditTime: 2021-06-26 15:09:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \MingPyEveryday\v20_copy_struct.py
'''
import os


def copy_struct(dst_dir):
    folder_list = []
    for name in os.listdir():
        if os.path.isdir(name):
            folder_list.append(name)
            print(name)
    for folder in folder_list:
        new_folder = os.path.join(dst_dir, folder)
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
            print("mkdir:" + new_folder)


def main():
    dst_dir = r'F:\data\fluent\90\0\k0.26'
    copy_struct(dst_dir)
    os.system("pause")


if __name__ == "__main__":
    main()
