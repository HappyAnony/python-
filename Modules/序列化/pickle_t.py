#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony
'''
pickle的功能和用法和json一样，区别在于：
（1）pickle可用来将函数、类等复杂的数据类型进行序列化，不过有时反序列后时不能直接调用的
（2）pickle是以二进制格式的形式写入和读取文件信息的
（3）pickle只用于python，不能用作其它语言

原则：一个文件只能dump一次，load一次。避免一个文件多次dump后，load时由于次序导致出错
'''

import pickle

def test():
	print("this is a test")

info = {
	"name":"anony",
	"age":22,
	"func":test
}

# #''' 写入文件
# #方法一：
# print(info)
# data = pickle.dumps(info)
# print(data)
# f = open("json.txt",'wb')
# f.write(pickle.dumps(info))
# f.close()

# 方法二：
# f = open("json.txt",'wb')
# pickle.dump(info,f)
# f.close()





#'''读取文件
# 方法一：
# f1 = open("json.txt",'rb')
# data = f1.read()
# print(type(data))   # 从文件中读取的数据是二进制
# print(data)
# fun = pickle.loads(data)    # 注意：进行反序列化时，当前文件一定要有进行序列化时函数的定义，要不然就会序列化失败
# print(fun)
# print(type(pickle.loads(data)))
# fun["func"]()               # 反序列化成功后，可直接调用函数
# f1.close()

# 方法二：
f1 = open("json.txt",'rb')
print(pickle.load(f1))
f1.close()