#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

#********************************************线程的调用方式*************************************************************

# 方法一：直接调用

'''
import threading
import time

def sayhi(num):  # 定义每个线程要运行的函数
	print("running on number:%s" % num)
	time.sleep(2)


if __name__ == '__main__':
	# args参数后面必须加上逗号，否则会被当做元组传入
	# 没有传入args时，target后面的逗号也必须加上逗号
	t1 = threading.Thread(target=sayhi, args=(1,))  # 生成一个线程实例
	t2 = threading.Thread(target=sayhi, args=(2,))  # 生成另一个线程实例

	t1.start()  # 启动线程
	t2.start()  # 启动另一个线程

	#print(t1.getName())  # 获取线程名
	#print(t2.getName())
'''

# 方法二：类继承调用

'''
import threading
import time

class MyThread(threading.Thread):
	def __init__(self, num):
		super(MyThread,self).__init__()
		self.num = num

	def run(self):  # 定义每个线程要运行的函数，该处的函数名必须是run()
		print("running on number:%s" % self.num)
		time.sleep(3)

if __name__ == '__main__':
	t1 = MyThread(1)
	t2 = MyThread(2)
	t1.start()
	t2.start()
'''

#********************************************多线程并发*************************************************************
# 此处实现的功能是：执行程序启动主线程，由主线程启动子线程，子线程执行完毕后再执行主线程，主线程执行完后退出程序
'''
import threading
import time

t_obj = []

class MyThread(threading.Thread):
	def __init__(self, num):
		super(MyThread,self).__init__()
		self.num = num

	def run(self):  # 定义每个线程要运行的函数，该处的函数名必须是run()
		print("running on number:%s" % self.num, threading.current_thread())  # current_thread()是用来获取当前线程的类型
		print("%s has done" %self.num)
		time.sleep(2)

time_start = time.time()

for i in range(50):   # 该部分是主线程的一部分，用来启动子线程，启动后的子线程和主线程是各自独立执行的,处于并行关系
	t = MyThread(i)
	t.start()
	t_obj.append(t)

for t in t_obj:
	t.join()         # 阻塞子线程，每个join只能阻塞自己对应的子线程；此处join的作用是阻塞所有的子线程，待所有子线程执行完后，再执行主线程
	                 # 此时主线程和子线程是串行关系，只有子线程执行完后才执行主线程


# 以下是主线程的一部分，和子线程是独立的
# 主线程就是程序本身
print("all threading has done", threading.current_thread())   # current_thread()是用来获取当前线程的类型
print("current active threading is:",threading.active_count()) # 获取当前的线程数
print("cost time is:", time.time()-time_start)
'''


#********************************************守护线程*************************************************************、

# 此处的功能是：执行程序启动主线程，由主线程启动守护线程(子线程)，主线程等非守护进程执行完后就退出程序，不管守护线程是否执行完

'''
import threading
import time

t_obj = []

class MyThread(threading.Thread):
	def __init__(self, num):
		super(MyThread,self).__init__()
		self.num = num

	def run(self):  # 定义每个线程要运行的函数，该处的函数名必须是run()
		print("running on number:%s" % self.num, threading.current_thread())  # current_thread()是用来获取当前线程的类型
		time.sleep(2)
		print("%s has done" %self.num)

time_start = time.time()

for i in range(50):   # 该部分是主线程的一部分，用来启动子线程，启动后的子线程和主线程是各自独立执行的,处于并行关系
	t = MyThread(i)
	t.setDaemon(True) # 把当前线程设置为守护线程
	t.start()
	t_obj.append(t)

print("all threading has done", threading.current_thread())   # current_thread()是用来获取当前线程的类型
print("cost time is:", time.time()-time_start)
'''

#********************************************GIL & Lock*************************************************************
# 任何情况下，python同一时间只能执行一个线程
# 因为cpython解释器中对于线程的启动和执行时通过调用os中的c库系统调用实现的(系统原生线程)，无法控制c库中线程的执行逻辑
# 所以为了避免多线程执行结果紊乱，在设计时同一时间只能执行一个线程(同一时间可以启动多个线程)，实现该功能的机制就叫做GIL(Global Interpreter Lock)
# 只有cpython解释器才有这项特性；Jpython和PyPy就没有这种特性
# 参考文档：http://www.dabeaz.com/python/UnderstandingGIL.pdf

# 一个进程下可以启动多个线程，多个线程共享父进程的内存空间，也就意味着每个线程可以访问同一份数据，此时，如果多个线程同时要修改同一份数据
# 会出现：当一个线程没有修改完数据时，另外一个线程也开始修改数据。因为GIL同一时间只允许一个线程执行一定的时间，时间到了系统就好字典释放GIL，执行下一线程
# 为了避免上述情况的发生吗，我们可以给这个数据加一把锁， 这样其它线程想修改此数据时就必须等待前一线程修改完毕并把锁释放掉后才能再访问此数据，此机制就叫做Lock[线程锁或互斥锁Mutex]
# 注意：Lock在Python2中会产生效果；但是似乎python3中默认自动已经lock了，所以无法产生效果


'''
import time
import threading

def addNum():
	global num  # 在每个线程中都获取这个全局变量
	time.sleep(1)
	lock.acquire()  # 修改数据前加锁
	num -= 1  # 对此公共变量进行-1操作
	lock.release()  # 修改后释放锁


num = 100  # 设定一个共享变量
thread_list = []
lock = threading.Lock()  # 生成全局数据锁
for i in range(100):
	t = threading.Thread(target=addNum)
	t.start()
	thread_list.append(t)

for t in thread_list:  # 等待所有线程执行完毕
	t.join()           # 等待一个线程执行结束

print('final num:', num)
'''

#********************************************Semaphore(信号量)*************************************************************
# 互斥锁Lock同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据

import threading, time
def run(n):
	semaphore.acquire()
	time.sleep(1)
	print("run the thread: %s\n" % n)
	semaphore.release()


if __name__ == '__main__':
	num = 0
	semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
	for i in range(20):
		t = threading.Thread(target=run, args=(i,))
		t.start()

while threading.active_count() != 1:
	pass  # print threading.active_count()
else:
	print('----all threads done---')
	print(num)



#********************************************RLock*************************************************************

# 当Lock里面嵌套Lock时，为了避免Lock混乱造成程序死循环，可以使用RLock递归锁

'''
import threading, time
def run1():
	print("grab the first part data")
	lock.acquire()
	global num
	num += 1
	lock.release()
	return num


def run2():
	print("grab the second part data")
	lock.acquire()
	global num2
	num2 += 1
	lock.release()
	return num2


def run3():
	lock.acquire()
	res = run1()
	print('--------between run1 and run2-----')
	res2 = run2()
	lock.release()
	print(res, res2)


if __name__ == '__main__':

	num, num2 = 0, 0
	lock = threading.RLock()
	for i in range(10):
		t = threading.Thread(target=run3)
		t.start()

while threading.active_count() != 1:
	print(threading.active_count())
else:
	print('----all threads done---')
	print(num, num2)
'''
