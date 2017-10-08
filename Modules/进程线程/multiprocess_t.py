#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

'''
python的线程是使用操作系统的原生线程
python的进程也是使用操作系统的原生进程

IO操作不占用CPU
计算操作占用CPU

python多线程不适用于CPU密集操作型的任务；适用于IO密集操作型的任务
CPU密集操作型任务可以通过python多进程实现
'''

#****************************************************启动进程************************************************************
'''
from multiprocessing import Process
import time

def f(name):
	time.sleep(2)
	print('hello', name)

if __name__ == '__main__':
	p = Process(target=f, args=('bob',))
	p.start()
	p.join()
	
'''

#****************************************************获取进程号**********************************************************

# 每个子进程都是由其父进程启动的

'''
from multiprocessing import Process
import os


def info(title):
	print(title)
	print('module name:', __name__)
	print('parent process:', os.getppid())
	print('process id:', os.getpid())
	print("\n\n")


def f(name):
	info('\033[31;1mfunction f\033[0m')
	print('hello', name)


if __name__ == '__main__':
	info('\033[32;1mmain process line\033[0m')
	p = Process(target=f, args=('bob',))
	p.start()
	p.join()

'''


#****************************************************进程间通信【数据传递】**********************************************************


# 进程Queue
# 与现场queue用法相同，但是本质不同；一个用于进程间通信，一个用于线程间通信
# 实现逻辑：父进程和子进程各自的Queue是相互独立的，两者都将自己的数据pickle序列化到内存中相同的位置，然后将该内存中的数据反序列化到对方Queue中
'''
from multiprocessing import Process, Queue

def f(q):
	q.put([42, None, 'hello'])

if __name__ == '__main__':
	q = Queue()
	p = Process(target=f, args=(q,))   # 父进程将进程Queue传给子进程；注意此处不能传入线程queue
	p.start()
	print(q.get())  # prints "[42, None, 'hello']"
	p.join()
'''

# Pipes
'''
from multiprocessing import Process, Pipe

def f(conn):
	conn.send([42, None, 'hello'])  # 子进程发送数据
	print("from parent:",conn.recv())  # 子进程接收数据
	conn.close()

if __name__ == '__main__':
	parent_conn, child_conn = Pipe()  # 实例化管道，生成两个对象
	p = Process(target=f, args=(child_conn,))
	p.start()
	print(parent_conn.recv())  # 接收子进程传入的数据；当子进程没有发送数据，而父进程接收数据，此时父进程就会阻塞，直到接收到子进程发送数据
	parent_conn.send("hello")  # 父进程发送数据
	p.join()

'''

#****************************************************进程间通信【数据共享】**********************************************************

# Managers支持下列数据类型的共享[支持同时修改]：list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array.
# Managers实现数据共享不需要对数据进行加锁操作，因为Managers默认已经对数据进行了加锁

'''
from multiprocessing import Process, Manager
import os

def f(d, l):
	d[1] = '1'
	d['2'] = 2
	d[0.25] = None
	l.append(os.getpid())
	print(l)

if __name__ == '__main__':
	with Manager() as manager:
		d = manager.dict()
		l = manager.list(range(5))
		p_list = []
		for i in range(10):
			p = Process(target=f, args=(d, l))
			p.start()
			p_list.append(p)
		for res in p_list:
			res.join()

		print(d)
		print(l)
'''

#****************************************************进程间同步**********************************************************

# 当多个进程共享一个终端时，避免不同进程打印信息的叠加造成的混乱，需要对各自进程打印数据进行加锁处理。
'''
from multiprocessing import Process, Lock

def f(l, i):
	l.acquire()
	try:
		print('hello world', i)
	finally:
		l.release()

if __name__ == '__main__':
	lock = Lock()
	for num in range(10):
		Process(target=f, args=(lock, num)).start()
'''

#****************************************************进程池**********************************************************

# 子进程是由父进程启动的
# 每启动并执行一个子进程都需要克隆一份父进程的数据并交给CPU运行，因此启动执行多个进程的开销会非常之大
# 进程池规定了同一时间可交给CPU运行的进程数量【即可启动的进程数没有限制，但是交给CPU运行的进程数有限制】，从而避免开销过大造成系统崩溃
# 由于启动多个线程的花销过小[只是有可能造成过多的CPU上下文切换，造成系统变慢]，所以不需要线程池。如果非要，可以使用信号量造成线程池[信号量规定了同一时间访问相同内存数据的线程数]


from  multiprocessing import Process, Pool
import time, os

def Foo(i):
	time.sleep(2)
	print("in the process", os.getpid())
	return i + 100

def Bar(arg):
	print('-->exec done:', arg)


if __name__ == '__main__':
	# 在win上启动多进程时，一定在main语句下启动；类unix系统就不需要。
	# 该main语句的作用：如果手动单独执行该文件，则执行下列语句；如果作为模块导入使用，则不执行下列语句
	# 因为，手动执行时__name__的值为__main__；如果导入模块执行，__name__的值就为模块名（文件名）

	pool = Pool(processes=5)  # 允许进程池里同时放入5个进程交给CPU运行
	for i in range(10):
		pool.apply_async(func=Foo, args=(i,), callback=Bar)    # 异步执行;callback表示回调，执行完func[子进程调用执行]后再执行callback[主进程调用执行],传入参数都是args
		#pool.apply(func=Foo, args=(i,))                       # 同步执行【串行】
	    #pool.apply_async(func=Foo,args=(i,))                  # 异步执行【并行】
	print('end')
	pool.close()
	pool.join()  # 进程池中进程执行完毕后再关闭程序，如果注释，那么程序直接关闭。