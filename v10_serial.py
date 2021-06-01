#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 12:50
# @Author  : Eiya_ming
# @Email   : eiyaming@163.com
# @File    : v10_serial.py

import serial #导入模块

import serial.tools.list_ports
port_list = list(serial.tools.list_ports.comports())
print(port_list)
if len(port_list) == 0:
   print('无可用串口')
else:
    for i in range(0,len(port_list)):
        print(port_list[i])

try:
    portx = port_list[0].name
    bps = 115200
    # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
    timex = None
    ser = serial.Serial(portx, bps, timeout=timex)
    print("串口详情参数：", ser)

    # 十六进制的读取
    print(ser.read().hex())  # 读一个字节

    print("---------------")
    ser.close()  # 关闭串口

except Exception as e:
    print("---异常---：", e)