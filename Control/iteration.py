#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

'''
可迭代对象：可直接用作for循环的对象
迭代器：有__next__()方法，同时能够被__next__()方法调用返回下一个值的对象

'''

'''
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterable))          # isinstance是内置的方法，用来判断某对象是否是某一具体类的实例
                                        # 判断该对象是否为可迭代对象
print(isinstance("abe",Iterator))       # 判断该对象是否为迭代器

print(isinstance((iter("abe")),Iterator)) # 将字符串转换成迭代器

'''
'''在python3中：for循环的本质就是一个使用__next__()方法调用迭代器
for x in [1,2,3,4,5]:
	pass
	
# 上述for循环等价于以下
it = iter([1,2,3,4,5])
while True:
	try:
		x = it.__next__()
		pass
	except StopIteration:
		break
    
'''