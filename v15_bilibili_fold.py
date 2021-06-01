'''
Author: your name
Date: 2021-06-01 21:48:28
LastEditTime: 2021-06-01 21:49:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \MingPyEveryday\v15_bilibili_fold.py
'''
import os
import json
import shutil


def get_partName(filename: str) -> str:
    with open(filename, 'r', encoding='utf8') as f:
        json_text = f.read()
        # a = a.split("\"PartName\":\"")[1]
        json_dict = json.loads(json_text)
        # print(json_dict["PartNo"],end=' ')
        # print(json_dict["PartName"])
        return json_dict["PartNo"] + '_' + json_dict["PartName"]


def Rename_Move(fold: str, title: str):
    files = os.listdir(fold)
    for f in files:
        if '.info' in f:
            partname = get_partName(fold + '/' + f)
            print('get part name:' + partname)
            break
    for f in files:
        if '.mp4' in f:
            print('copying:' + title + '/' + partname + '.mp4')
            shutil.copy(fold + '/' + f, title + '/' + partname + '.mp4')
            print('done')
            break


if __name__ == "__main__":
    title = '新专辑'
    folds = os.listdir()
    for dvi in folds:
        if '.dvi' in dvi:
            with open(dvi, 'r', encoding='utf-8') as f:
                txt = f.read()
                title = json.loads(txt)["Description"]
                if not os.path.exists(title):
                    os.makedirs(title)

    for fold in folds:
        if '.' not in fold:
            print("working in:./" + fold)
            Rename_Move(fold, title)

    os.system('pause')