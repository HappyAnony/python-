#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 参考文档：http://www.cnblogs.com/alex3714/articles/5213184.html


#***********************************************反射===匹配字串调用方法********************************************************

# 实现动态的内存装配
# 与用户交互的都是字串，通过反射（映射）就可以将与用户交互的字串转换为内存对象，实现动态内存装配

def Add(self):
	print("%s in the Add" %self.name)

class Foo(object):
	def __init__(self):
		self.name = 'anony'

	def func(self):
		print("in the func")
		return 'func'


obj = Foo()


# #### 检查obj对象里是否含有字串对应的属性或方法 ####
# print(hasattr(obj, 'name'))
# print(hasattr(obj, 'func'))

# #### 获取obj对象里字串对应属性的值；对应方法的内存地址 ####
# print(getattr(obj, 'name'))   # 非callable
# print(getattr(obj, 'func'))   # callable
# getattr(obj,'func')()

# #### 设置成员 ####
# 第一个参数为作用对象
# 第二个参数为属性名或方法名
# 第三个为属性值或方法对象
     # 当传入的是一个内存对象地址【方法名，lambda表达式等】，表示前面第二个参数是方法名，是callable的，即可被（）调用
     # 当传入的是一个基本数据类型，或者print语句等时，表示前面第二个参数是属性名，是不能被（）调用的
# setattr(obj, 'age', 18)
# print(obj.age)
# setattr(obj, 'ptr', print("in the show "))
# obj.ptr
# setattr(obj, 'show', lambda num: num + 1)
# obj.show(2)
# setattr(obj,'add',Add)
# obj.add(obj)              # 此时不会将obj和self进行关联，需要手动传入对象obj

# #### 删除成员 ####
# delattr(obj, 'name')
# delattr(obj, 'func')






#***********************************************定制化类********************************************************

# 参考文档：http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

'''
class MyType(type):
    def __init__(self,*args,**kwargs):

        print("Mytype __init__",*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ",obj,*args, **kwargs)
        print(self)
        self.__init__(obj,*args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__",*args,**kwargs)
        return type.__new__(cls, *args, **kwargs)

print('here...')
class Foo(object,metaclass=MyType):


    def __init__(self,name):
        self.name = name

        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__",cls, *args, **kwargs)
        return object.__new__(cls)

f = Foo("Alex")
print("f",f)
print("fname",f.name)


# 属性 __metaclass__：其用来表示该类由谁来实例化创建
# 类的生成调用顺序依次是： __new__ --> __init__ --> __call__

'''