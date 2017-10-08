#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

class Test(object):
	def __init__(self):
		self.name = "anony"


obj = Test()

try:
	assert type(obj.name) is int   # 判断obj.name是不是int型，如果是就继续执行，如果不是就中断程序，报AssertionError
except AssertionError:
	print("error")
else:
	print("ok")