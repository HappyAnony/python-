#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony
# 官方文档：https://docs.python.org/3/library/functions.html

print(dir(__builtins__))        # 打印出所有的内置方法；dir是以列表的形式返回指定模块中所有的方法

'''将字符串转换成字典
arg = "{\
            'bakend': 'www.oldboy.org',\
            'record':{\
                'server': '100.1.7.9',\
                'weight': 20,\
                'maxconn': 30\
            }\
        }"
arg_new = eval(arg)
print(arg_new)

'''
'''
print(all([1,5,-5,0]))     # 可迭代对象的每一个元素为True时返回True；为空也返回True
print(any([1,5,-4,0]))     # 可迭代对象的一个元素为True时就返回True；为空返回False
print(bin(10))             # 将整数转换成一个以0b开头的二进制字符串

a = bytes("abcd",encoding="utf-8")   # 将字串转换成bytes类型
print(a.capitalize(),a)              # 字串是不可变的

b = bytearray("abcd",encoding="utf-8")
b[0] = 100
print(b)                             # bytearray可以将字串转换成可变的

print(chr(897))       # 返回ASCII码中897对应的字符
print(ord("&"))       # 返回ASCII码中字符&对应的整数

#'''实现动态import
code = '''
print("this is a test")
'''
 #方法一：直接使用exec,eval方法
exec(code)             # 适用于执行python代码块字串
eval(code)             # 即可用于执行python代码块字串；又可以用来将字典、列表等字串转换成对应的类型
 #方法二：先编译后执行
py_obj = compile(code,'error.log',"exec")    #将code代码段编程成可被exec方法执行的python对象，编译时的出错信息保存到error.log中
exec(py_obj)
#'''

print(divmod(8,5))   # 返回8除以5的商和余数组成的元组

l = ["anony",'name','jack']
print(enumerate(l))
#print(list(enumerate(l)))                 # 此时enumerate生成的是一个迭代器；需要用list方法将其转换成列表打印出来
#print(list(enumerate(l,start=1)))
for i in enumerate(l):                     # 以二维元组列表的形式返回一个可迭代对象的元素及其对应的索引;此时enumrate生成的是一个迭代器
	print(i)


rev = filter(lambda n:n>7,range(10))       # 将一个可迭代对象中的所有元素按照前面函数(例如lambda表达式)的要求进行过滤
print(rev)                                 # 此时的filter是一个可迭代对象
for i in rev:
	print(i)

rev1 = map(lambda n:n*n,range(3))          # 将一个可迭代对象中的所有元素按照前面函数的要求进行处理
print(rev1)
for i in rev1:
	print(i)

import functools                            # python2中reduce为内置方法；python3中被封装到functools模块中
rev2 = functools.reduce( lambda x,y:x*y , range(1,10))   # 实现阶乘
print(rev2)

#print(globals())          # 以字典的形式返回当前文件中所有定义的全局变量以及对应的变量值
def test1():
	var = 345
	print(locals())           # 以字典的形式返回当前文件中所有定义的局部变量以及对应的变量值;j局部变量只有函数被调用时才会生成
test1()

print(hash("anony"))      # 为指定对象生成唯一的映射

print(hex(345))           # 将指定整数转换成16进账

print(id(rev2))           # 返回某一指定对象的内存地址

print(pow(2,5))           # 返回2的5次方

print(round(3.235,1))     # 保留小数点后1位

dict1 = {4:3,-3:5,0:1,9:-6}
print(sorted(dict1))          # 取出字典的key，从小到大进行排序，以列表的形式返回
print(sorted(dict1.items()))  # 将字典转换成列表进行排序，默认是以字典的key进行排序
print(sorted(dict1.items(),key=lambda x:x[1]))  # key指定排序的对应，此处是以字典的value进行排序

a = [1,2,3,4,5,6]
b = ['q','w','e']
c = zip(a,b)
print(c)
for i in c:
	print(i)

__import__('sys')                 # 以字符串的格式导入模块


# del函数的本质：删除变量名，即内存的对象引用，代表该块内存没有被引用，其内存可以被回收


#****************************类************************************
type(dict1)            # python中一切对象类型都是由type产生的

