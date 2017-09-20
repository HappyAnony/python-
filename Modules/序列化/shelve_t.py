#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony


'''
shelve模块是对pickle模块的进一步封装，弥补了pickle只dump一次，load一次的缺陷。它可以实现一个文件dump多次数据，load读取数据
时不会因为次序操作数据读取出错
shelve是一个简单的以key:value将内存数据通过文件存储进行持久化的模块，可以持久化任何pickle支持的python数据类型
可以将shelve理解为对字典的操作
'''
import shelve

'''格式化持久存储
d = shelve.open("shelve_test")    # 打开一个文件，可以理解为初始化一个字典
info = {"age":22,"name":"anony"}
name = ["jack","marry"]
d["name"] = name      # 持久化列表
d["info"] = info      # 持久化字典

d.close()

'''
#'''读取数据
d = shelve.open("shelve_test")    # 打开一个文件
print(d.get("name"))              # 以键获取值
print(d.get("info"))              # 以键获取值
it = d.items()
for i in it:
	print(i[1])

