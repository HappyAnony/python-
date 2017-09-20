#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 继承的作用：扩展已经存在的代码模块，从而实现代码重用
# 传入的参数可以是任意对象，即任何实例化的类，此时可以间接实现不同类之间关联

'''
（1）继承父类的属性和方法
（2）定义自己的属性和方法
（3）重构父类的属性和方法

注意：同一父类下的两个字类
（1）共享父类的属性和方法，修改属性时可能会影响另一子类
（2）自定义或重构的属性和方法是相互独立的，彼此之间无影响
'''


#************************************************单继承**********************************************************
'''
#class parent():   # 经典类的写法
class parent(object):  # 新式类的写法
	n_list = []
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def study(self):
		print("studying........")

	def sleep(self):
		print("in the sleeping...")


class son(parent):   #

	#继承了parent类的所有属性和方法,调用方式：
	#（1）使用类名[parent.属性/方法]===经典类的写法
	#（2）使用内置方法[super(son,self).属性/方法],此时属性和方法中的self参数不用添加，被supert中的self参数取代===新式类的写法
	#建议采用方法2：避免重构时繁琐修改造成的错误

	def __init__(self,name,age,height):  # 重构了parent父类的实例变量
		#parent.__init__(self,name,age)   # 方法一：继承父类的属性；经典类的写法
		super(son,self).__init__(name,age)# 方法二：继承父类的属性；新式类的写法
		self.height = height             # 添加自己的属性

	def school(self):   # 定义自己的属性和方法
		print("go to school")

	def study(self):   # 重构了parent类的study方法，为其添加了新功能
		super(son,self).study()  # 调用parent类的study方法
		print("studying in school")


class daughter(parent):
	def sing(self):
		print("sing well")


s = son("anony",14,179)
s.sleep()
s.study()
s.school()
s.n_list.append("from s")
print(s.n_list)

d = daughter("marry",16)
d.sleep()
d.study()
d.sing()
d.n_list.append("from d")
print(d.n_list)
print(s.n_list)

'''

#************************************************多继承**********************************************************
'''
class parent(object):  # 新式类的写法
	n_list = []
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.friends = []

	def study(self):
		print("studying........")

	def sleep(self):
		print("in the sleeping...")

class make(object):
	def __init__(self):
		self.money = 1000
	def makefriends(self,obj):   # self用来接收自身对象，obj用来接收传入对象
		print("%s make friends with %s" %(self.name,obj.name))  # son在继承该类之前，就继承了parent类，定义了self.name
		self.friends.append(obj)


class son(parent,make):   # 多继承。
	#
	def __init__(self,name,age,height):  # 调用本地构造函数，父类的构造函数就不调用
		super(son,self).__init__(name,age)  # 单继承或多继承时都是按照广度优先法则继承一次
		#parent.__init__(self,name,age)     # 多继承时，该种方法有多少个就继承多少个，不符合继承规则
		#make.__init__(self)
		self.height = height

	def school(self):
		print("go to school")

	def study(self):
		super(son,self).study()
		print("studying in school")


class daughter(parent,make):  # 多继承
	                          # 此处没有构造函数，于是先调用parent类的构造函数，make构造函数就不调用了；如果parent没有，就调用make
	                          # 此处就出现一个问题，当parent类有构造函数时，make类的构造函数就不会调用，于是无法继承make类的属性
	def sing(self):
		print("sing well")


s = son("anony",14,179)
# 上述类实例化的过程是：
# （1）查找__init__构造函数实例化【继承属性】：查找优先级，本地>左边父类>右边父类。本地有调用本地；本地没有调用父类；只调用一次【取优先级高的方法调用】
# （2）继承方法：继承优先级，本地>左边父类>右边父类。本地有调用本地；本地没有调用父类;只调用一次【取优先级高的方法调用】
# 终上所述：优先级高的属性或方法会覆盖优先级低的属性和方法，即只继承优先级高的属性和方法，不继承优先级低的

d = daughter("marry",16)
s.makefriends(d)
d.makefriends(s)
print(s.friends[0].name)
d.name = "tom"
print(s.friends[0].name)
print(s.friends[0].name)
print(s.money)
# print(d.money)
'''
#************************************************经典类和新式类**********************************************************
'''


# 经典类：class Class_Name():
# 新式类：class Class_Name(object):
# python2中：
# （1）类的定义可以加括号，可以不加括号
# （2）经典类按照深度优先法则继承属性和方法
# （3）新式类按照广度优先法则继承属性和方法
# 
# python3中：
# （1）类的定义必须加上括号
# （2）经典类和新式类都是按照广度优先法则继承属性和方法


class A():
	def __init__(self):
		print("a")

class B(A):
	def __init__(self):
		print("b")

class C(A):
	def __init__(self):
		print("c")

class D(B,C):
	def __init__(self):
		print("d")

obj = D()


# 广度优先:构造函数的查找路径===D->B->C->A
# 深度优先:构造函数的查找路径===D->B->A->C


'''


#************************************************实例**********************************************************


class SchoolMember(object):
	members = 0  # 初始学校人数为0

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def tell(self):
		pass

	def enroll(self):
		'''注册'''
		SchoolMember.members += 1
		print("\033[32;1mnew member [%s] is enrolled,now there are [%s] members.\033[0m " % (
		self.name, SchoolMember.members))

	def __del__(self):
		'''析构方法'''
		print("\033[31;1mmember [%s] is dead!\033[0m" % self.name)


class Teacher(SchoolMember):
	def __init__(self, name, age, course, salary):
		super(Teacher, self).__init__(name, age)
		self.course = course
		self.salary = salary
		self.enroll()

	def teaching(self):
		'''讲课方法'''
		print("Teacher [%s] is teaching [%s] for class [%s]" % (self.name, self.course, 's12'))

	def tell(self):
		'''自我介绍方法'''
		msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher !''' % (self.name, 'Oldboy', self.course)
		print(msg)


class Student(SchoolMember):
	def __init__(self, name, age, grade, sid):
		super(Student, self).__init__(name, age)
		self.grade = grade
		self.sid = sid
		self.enroll()

	def tell(self):
		'''自我介绍方法'''
		msg = '''Hi, my name is [%s], I'm studying [%s] in [%s]!''' % (self.name, self.grade, 'Oldboy')
		print(msg)


if __name__ == '__main__':
	t1 = Teacher("Alex", 22, 'Python', 20000)
	t2 = Teacher("TengLan", 29, 'Linux', 3000)

	s1 = Student("Qinghua", 24, "Python S12", 1483)
	s2 = Student("SanJiang", 26, "Python S12", 1484)

	t1.teaching()
	t2.teaching()
	t1.tell()


