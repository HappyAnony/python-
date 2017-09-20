#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 参考文档：http://www.cnblogs.com/alex3714/articles/5213184.html

#***********************************************静态方法**********************************************************

# 适用场景：构建工具包，类似于os模块。只是名义上的归类管理，实际上在静态方法里访问不了类或实例的任何属性和方法

'''
class Dog(object):
	def __init__(self,name):
		self.name = name

	@staticmethod         # 使用@staticmethod装饰器将eat方法变为一个静态方法
	                      # 静态方法的定义和使用和def定义的普通函数一样，只不过需要通过类名或者实例名进行调用
	                      # 因为它依然属于类的一个方法，只是不需要使用self来接收对象实例
	                      # 因此可以将静态方法理解为一个普通的def函数，和类没有任何关系，即不能调用类的属性和方法，又不能使用self接收对象
	def eat():
		print(" is eating")


d = Dog("anony")
d.eat()                # 只能通过类名或者实例名进行调用

'''
#***********************************************类方法**********************************************************
# 类方法：
# 只能访问调用类属性，不能访问调用对象属性
# 定义时需要添加self来接收对象

'''
class Dog(object):
	name = "anony"
	def __init__(self,name):
		self.name = name

	@classmethod
	def eat(self):
		print(" %s is eating" %self.name)


d = Dog("jack")
d.eat()
'''

#***********************************************属性方法**********************************************************

# 属性方法：把一个方法转换成一个静态属性【不用()即可调用】，而不是动态属性【函数=必须使用()调用】
# 适用场景：隐藏业务的实现细节，提供单一的用户访问接口


class Dog(object):
	def __init__(self,name):
		self.name = name
		self.__food = None

	@property
	def eat(self):
		print(" %s is eating %s" %(self.name,self.__food))

	@eat.setter         # 给属性方法赋值
	def eat(self,food):
		self.__food = food

	@eat.deleter        # 删除属性方法
	def eat(self):
		del(self.__food)
		print("删除属性方法")



d = Dog("jack")
d.eat = "baozi"  # 给属性赋值
d.eat
del(d.eat)      # 删除属性方法
