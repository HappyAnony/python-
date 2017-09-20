#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

import sys
print(sys.argv)      # 输出命令行参数列表，第一个元素为脚本文件名
# print(sys.argv[1])   #打印当前文件接收的参数
print(sys.version)   # 获取python解释器的版本信息
print(sys.maxsize)   # 获取int的最大值
print(sys.path)     # 获取python的path环境变量，即python的搜索路径
print(sys.platform) # 获取操作系统平台的名称
sys.stdout.write("plz:")
#print(sys.stdin.readline()[:-1])

print(sys.getdefaultencoding())   #获取系统的默认编码

