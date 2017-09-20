#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony
'''
os模块提供了对操作系统进行调用的接口
'''
import os
print(os.getcwd())   # 获取当前目录
os.chdir("d:\\python")
print(os.getcwd())
os.chdir(r"d:\python\oldboy")
print(os.getcwd())
os.chdir("d:\\python")
print(os.curdir)       # 返回当前目录
print(os.pardir)       # 返回当前目录的父级目录
print(os.sep)          # 获取当前操作系统的路径分隔符
print("%s" %(os.linesep))      # 获取当前系统的行终止符
print(os.environ)              # 获取当前系统的环境变量
print(os.pathsep)      # 获取用于分隔文件路径的字符串（例如path环境变量中分隔文件路径的字符）
print(os.name)         # 获取当前使用的平台（win-->nt;linux-->posix）
os.system("dir")       # 执行系统命令

print(os.path.abspath(__file__))
print(os.path.split(__file__))
print(os.path.dirname(__file__))
print(os.path.basename(__file__))
print(os.path.exists(__file__))
print(os.path.isabs(__file__))
print(os.path.isfile(__file__))
print(os.path.isdir(__file__))
print(os.path.getatime(__file__))
print(os.path.getmtime(__file__))
# os.makedirs()         # 递归地创建多层目录
# os.removedirs()       # 递归删除空目录
# os.mkdir()
# os.rmdir()
# os.listdir("dirname")            # 列出指定目录下的内容
# os.remove()                      # 删除一个文件
# os.rename("oldname","newname")   # 修改文件名
# os.stat("/path/to/file")         # 获取文件或目录的信息

#cmd_res = os.popen("dir").read()
#print(cmd_res)













