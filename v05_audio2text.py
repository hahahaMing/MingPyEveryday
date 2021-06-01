#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 10:21
# @Author  : Eiya_ming
# @Email   : eiyaming@163.com
# @File    : v05_audio2text.py

import speech_recognition as sr #加载包

r = sr.Recognizer()
with sr.WavFile("assets/v05/录音.wav") as source:  #请把引号内改成你自己的音频文件路径
   audio = r.record(source)

IBM_USERNAME = 'Yuming Liu'
IBM_PASSWORD= 'Ibm326033'


text = r.recognize_ibm(audio, username = IBM_USERNAME, password = IBM_PASSWORD, language = 'zh-CN')
print(text)