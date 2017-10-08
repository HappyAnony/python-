#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 参考文档：http://www.cnblogs.com/alex3714/articles/5248247.html
# coroutine又叫做协程或微线程
# 协程的本质就是：一种用户态的轻量级线程
# 协程的功能就是：实现单线程高并发【例如：nginx默认是单线程，高并发】
# 协程功能实现的原理：协程的上下文切换
# 协程上下文切换的原理：服务器处理模型
'''
服务器处理模型：当前协程遇到IO操作时
（1）将该IO操作注册到事件队列中
（2）从当前协程切换到其它协程
（3）当事件循环机制从事件队列中取出IO操作并执行完时，通过调用回调函数触发通知IO操作已执行完，可以从其它协程切换到当前协程
'''
# 协程事件驱动模型实现的原理：IO操作模型

'''
协程的特点：协程是用户态线程，不同于内核态线程
（1）无需线程调度机制中上下文切换的开销；协程拥有自己的寄存器上下文和栈实现自己的调度机制
（2）无需原子操作锁定及同步的开销
（3）实现cpu密集型应用时需要和进程配合才能利用单个CPU的多核资源
（4）进行阻塞（Blocking）操作（如IO时）会阻塞掉整个程序·

协程的适用场景：
（1）高并发
（2）高扩展性
（3）低成本
'''

'''
协程的定义：[满足下列所有条件才算实现了一个协程]
（1）必须在只有一个单线程里实现并发
（2）修改共享数据不需加锁
（3）用户程序里自己保存多个控制流的上下文栈
（4）一个协程遇到IO操作自动切换到其它协程
'''



#******************************************************yield实现协程*****************************************************

# 实现功能：协程之间手动切换
# 该协程有一个问题：遇到IO操作无法自动切换到其它协程

'''
import time
import queue
def consumer(name):
	print("--->starting eating baozi...")
	while True:
		new_baozi = yield
		print("[%s] is eating baozi %s" % (name, new_baozi))
	# time.sleep(1)


def producer():
	r = con.__next__()
	r = con2.__next__()
	n = 0
	while n < 5:
		n += 1
		con.send(n)
		con2.send(n)
		print("\033[32;1m[producer]\033[0m is making baozi %s" % n)


if __name__ == '__main__':
	con = consumer("c1")
	con2 = consumer("c2")
	p = producer()

'''

#******************************************************Greenlet实现协程*****************************************************

# 实现功能：协程之间手动切换
# greenlet是一个用C实现的第三方协程模块[需要手动安装]，相比与python自带的yield，它可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator
# 该协程有一个问题：遇到IO操作无法自动切换到其它协程

'''
from greenlet import greenlet

def test1():
	print(12)
	gr2.switch()
	print(34)
	gr2.switch()

def test2():
	print(56)
	gr1.switch()
	print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()

'''

#******************************************************Gevent实现协程*****************************************************

# 实现功能：协程之间自动切换【遇到IO操作就自动切换到其它协程】
# Gevent是一个第三方库，需要手动安装
# gevent可以实现并发同步或异步编程
# 在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程实现对Greenlet的封装
# Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度
# 在linux中，gevent是基于libevent.so实现的


# 模拟操作
'''
import gevent

def func1():
	print('\033[31;1min the func1\033[0m')
	gevent.sleep(2) # 模拟IO操作
	print('\033[31;1mfunc1 again\033[0m')


def func2():
	print('\033[32;1min the func2\033[0m')
	gevent.sleep(1) # 模拟IO操作
	print('\033[32;1mfunc2 again\033[0m')

def func3():
	print('\033[32;1min the func3\033[0m')
	gevent.sleep(0) # 模拟IO操作
	print('\033[32;1mfunc3 again\033[0m')

gevent.joinall([
	gevent.spawn(func1),
	gevent.spawn(func2),
	gevent.spawn(func3),
])
'''

# 遇到IO阻塞时自动切换任务
from gevent import monkey
monkey.patch_all()   # 实现功能：使gevent能够捕获到当前程序中所有形式的IO操作

import gevent
from  urllib.request import urlopen


def f(url):
	print('GET: %s' % url)
	resp = urlopen(url)
	data = resp.read()
	print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
	gevent.spawn(f, 'https://www.python.org/'),
	gevent.spawn(f, 'https://www.yahoo.com/'),
	gevent.spawn(f, 'https://github.com/'),
])
