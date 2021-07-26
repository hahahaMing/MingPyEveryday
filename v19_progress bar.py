'''
Author: your name
Date: 2021-06-26 14:04:07
LastEditTime: 2021-06-26 14:14:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \MingPyEveryday\v19_progress bar.py
'''
import sys
import time
	
strarrs = ['/','|','\\']
for i in range(15):
  sys.stdout.write(strarrs[i % 3]+'{}/{}:'.format(i+1,80)+'#' * i+'\r')
  sys.stdout.flush()
  time.sleep(1)