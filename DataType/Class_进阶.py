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

'''
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

'''

#***********************************************类的特殊方法**********************************************************

'''
class Foo:
	""" 描述类信息，这是用于看片的神奇 """

	def __init__(self,name):
		self.name = name

	def func(self):
		pass

	def __call__(self, *args, **kwargs):
		print("the param is ", args,kwargs)
	def __str__(self):
		return "<Obj:%s>" %self.name

f = Foo("baozi")
print(f.__doc__)
print(f.__module__)
print(f.__class__)
f.__call__(2,3,4,name="anony")  # 调用类中定义的__call__方法
print(Foo.__dict__)  # 打印类的所有属性，不包括实例属性
print(f.__dict__)    # 打印所有实例属性，不包括类属性
print(f)             # 一个类中定义了__str__方法，那么在打印对象时，默认输出该方法的返回值

'''
#***********************************************将类封装成字典********************************************************

'''

class Foo(object):
	def __init__(self):
		self.data = {}

	def __getitem__(self, key):
		print('__getitem__', key)
		return self.data.get(key)

	def __setitem__(self, key, value):
		print('__setitem__', key, value)
		self.data[key] = value
		print(self.data)

	def __delitem__(self, key):
		print('__delitem__', key)
		del(self.data[key])
		print(self.data)


obj = Foo()

obj['k1'] = 'jack'  # 自动触发执行 __setitem__方法，给字典添加键值【自己定义】
obj['k2'] = 'anony'
reval = obj['k1']  # 自动触发执行 __getitem__方法，获取指定键的值【自己定义】
print(reval)
del obj['k1']       # 自动触发执行__delitem__方法，删除指定键值对【自己定义】

# 注意：上述所有的操作只是触发并调用类中定义的相应方法【方法的具体实现功能可以自己设定】，实现将类转换为字典进行操作

'''

