#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 参考文档：http://www.cnblogs.com/wupeiqi/articles/5017742.html

# try/except/else/finally为异常处理语句，捕获处理的对象为：导致程序运行中断的异常。【即不能导致程序运行中断的异常是无法捕获的】

# 特别注意：try语句无法捕获IndentationError、SyntaxError异常，因为这些异常会直接导致无法正确解释执行try语句

#****************************************** 标准[系统]异常 ****************************************************

'''
常用异常：
AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
'''

'''

s1 = 'hello'
try:
    int(s1)                  # 主代码块
except IndexError as e:      # 出现IndexError异常时，执行该块；通常用来处理特定异常
    print(e)
except (ValueError,KeyError) as e:  # 出现ValueError,KeyError异常时，执行该块；通常用来处理特定异常
    print(e)
except Exception as e:       # 出现上述异常以外的所有异常时，执行该块；通常用来处理未知异常
	print(e)
else:                        # 主代码块执行完，没有出现异常时，执行该块
	print("this test is ok")
finally:                     # 主代码无论异常与否，最终执行该块
	print("test is over")
	
'''

#****************************************** 自定义异常 ****************************************************

# 功能：将标准异常格式化为自定义异常

class AnonyError(Exception):   # 继承Exception所有异常类，定义自己的异常名，AnonyError即是类名，同时也是自己定义的异常名
	def __init__(self, msg):
		self.message = msg

	def __str__(self):           # 此处__str__方法可以省略，因为Exception基类中__str__方法也定义了返回该值
		return self.message


try:
	raise AnonyError('我的异常')         # 触发自定义异常
except AnonyError as e:                  # e接收的是类的返回值，即__str__方法的返回值
	                                     # 捕获的异常为对应的类名
	print(e)