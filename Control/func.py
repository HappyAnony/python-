#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

#参考文档：http://www.cnblogs.com/alex3714/articles/5740985.html

'''
编程范式：
（1）面向对象编程-->类-->class
（2）面向过程编程-->过程-->def【过程可以理解为一个没有返回值的函数】
（3）函数式编程--->函数-->def

函数的好处：
（1）代码复用
（2）保持一致性
（3）可扩展性
'''
'''
# 函数
def func1(argc1,agrc2):          #argc1和argc2为形参，只有当函数调用时才会声明定义引用该变量
	"函数说明"
	print("this is a function")  #函数体
	return 0                     #return语句会终止函数运行，同时返回一个值
# 过程
def proc1():
	"过程说明"
	print("this is a procession")
# 调用
x = func1()
y = proc1()
print("from function return %s" %x)
print("from procession return %s" %y)
'''
'''日志打印
import time

def logger(log):
	time_format = "%Y-%m-%d %X"
	time_current = time.strftime(time_format)
	with open("log.txt",'a+',encoding="utf-8") as f:
		f.write("[%s] %s" %(time_current,log))
def test1():
	log = "from test1\n"
	logger(log)

def test2():
	log = "from test2\n"
	logger(log)
	return 0

def test3():
	log = "from test3\n"
	logger(log)
	return 'this', 'is', ['a','test']   #以元组的形式返回

def main():
	rev1 = test1()
	time.sleep(1)
	rev2 = test2()
	time.sleep(1)
	rev3 = test3()
	print(rev1)
	print(rev2)
	print(rev3)
	return test1,test2,test3         #返回函数的内存对象；函数名就是函数的指针变量
	#return test1(),test2(),test3()   #返回函数的返回值
rev4 = main()
print(rev4)
'''

'''高阶函数
def add(a,b,f):
	return f(a)+f(b)
res = add(3,-7,abs)
print(res)
'''
#'''匿名函数
# 匿名函数的本质就是一个lambda语句；第一个是变量，第二个是对变量的处理动作
# 匿名函数只能处理比较简单的逻辑，例如三元运算
calc = lambda n:3 if n < 4 else n-1
print(calc(5))
#'''

'''装饰器：原函数不传入参数
import time
def decorator(func):
	def timer():      
		start_time = time.time()
		rev = func()
		stop_time = time.time()
		print("the func running time is %s" %(stop_time-start_time))
		print(rev)
	return timer
@decorator            #test = decorator(test)
def test():
	time.sleep(3)
	print("in the test")
	return0
test()                     

'''

'''装饰器：原函数传入参数
import time
def decorator(func):
	def timer(*args,**kwargs):      #*args和*kwargs用来接收不固定参数。因为该装饰器可以修改任何函数，但是每个函数
		                            #传入的参数的个数和方式不一样
		                            #wrapper包装
		start_time = time.time()
		rev = func(*args,*kwargs)
		stop_time = time.time()
		print("the func running time is %s" %(stop_time-start_time))
		print(rev)
	return timer
@decorator            #test = decorator(test)
def test(name):
	time.sleep(3)
	print("the name is %s" %name)
	return 0
test(name = "anony")                      #相当于timer(name = "anony")
'''


'''装饰器：装饰器传入参数

import time
def decorator(age):
	def out_wrapper(func):
		def timer(*args,**kwargs):      #*args和*kwargs用来接收不固定参数。因为该装饰器可以修改任何函数，但是每个函数
			                            #传入的参数的个数和方式不一样
			                            #wrapper包装
			start_time = time.time()
			rev = func(*args,*kwargs)
			print("the age is %s" %age)
			stop_time = time.time()
			print("the func running time is %s" %(stop_time-start_time))
			print(rev)
		return timer
	return out_wrapper
@decorator(age = 22)
def test(name):
	time.sleep(3)
	print("the name is %s" %name)
	return 'success'
test(name = "anony")                      #相当于timer(name = "anony")
'''
