#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 多态：同一接口，多种实现，从而实现接口重用
# 传入的参数可以是任意对象，即任何实例化的类，此时可以间接实现不同类之间关联

class Animal(object):
	def __init__(self,name):  # Constructor of the class
		self.name =name

	def talk(self):  # Abstract method, defined by convention only
		raise NotImplementedError("Subclass must implement abstract method")

	@staticmethod   # 装饰器,可以实现不用实例化Animal类，就可以Animal.func()调用该方法
	def func(obj):  # 一个接口，多种形态
		obj.talk()


class Cat(Animal):
	def talk(self):
		print('%s: 喵喵喵!' % self.name)


class Dog(Animal):
	def talk(self):
		print('%s: 汪！汪！汪！' % self.name)





c1 = Cat('小晴')
d1 = Dog('李磊')

Animal.func(c1)
Animal.func(d1)