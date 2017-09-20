#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

'''
json只支持简单的可序列化的数据类型，不能操作复杂的数据类型【函数等】
json在所有语言中都是通用的，用于不同语言之间的数据交互
json正在逐渐取代xml[标记性语言]

原则：一个文件只能dump一次，load一次
'''
import json
info = {
	"name":"anony",
	"age":22
}

# #''' 写入文件
# # 方法一：
# print(type(info))
# print(type(str(info)))
# f = open("json.txt",'w')
# f.write(str(info))               # info是字典，不能直接写入到文件中，需要将其转换成字符串才行
# f.close()

# 方法二：
# print(info)
# data = json.dumps(info)
# print(data)
# f = open("json.txt",'w')
# f.write(json.dumps(info))        # info是字典，不能直接写入到文件中，需要将其转换成字符串才行
# f.close()

# # 方法三：
# f = open("json.txt",'w')
# json.dump(info,f)
# f.close()





# #'''读取文件
# # 方法一：
# f1 = open("json.txt",'r',encoding="utf-8")
# data = f1.read()
# print(type(data))                 # 从文件中读取的数据是字符串，需要通过eval内置方法将其转换该字串去掉引号后的数据类型
# print(eval(data))
# f1.close()

# # 方法二：
# f1 = open("json.txt",'r',encoding="utf-8")
# data = f1.read()
# print(type(data))                 # 从文件中读取的数据是字符串
# print(json.loads(data))
# print(type(json.loads(data)))
# f1.close()

# 方法三：
f1 = open("json.txt",'r',encoding="utf-8")
print(json.load(f1))
f1.close()