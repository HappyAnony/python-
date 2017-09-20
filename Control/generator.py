#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

''' 生成器一
g = ( i*2 for i in range(10) )
print(g)
print(g.__next__())       # 依次取一个元素
print(g.__next__())       # python2中是next()
print(g.__next__())
for i in g:               # 循环取元素
 	print(i)
print(g.__next__())       # 当生成器的元素取完后，会置空,此时无法访问生成器；此时访问会报StopIteration错误

'''

'''生成器二：菲波那切数列fibonacci
def fib(max):
	n,a,b = 0,0,1       # n=0;a=0;b=1
	while n < max:
		yield(b)        # yield方法和next方法的配合使用
		                # yield方法保留函数当前状态，中断跳出函数并返回当前b的值；next方法跳回yield保留的状态继续执行
		a,b = b, a+b    # t=(b,a+b);a=t[0];b=t[1]
		n = n+1
	return "done"
g = fib(10)             # 该处只是实现将函数转换成生成器
print(g)
while True:
	try:
		value = next(g)  #next(g)相当于g.__next__(),该方法可以唤醒生成器
		                 #第一次使用next方法的作用：开始调用执行函数，遇到yield就中断函数，返回yield接收的参数
		                 #后面使用next方法的作用：跳回上次函数yield中断的地方，继续执行函数，遇到当遇到yield同样中断函数返回参数
		print("g:",value)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break
'''

#'''生成器实现单线程的并行效果
import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield                                   # 当yield不跟任何参数时，表示跳出函数时的返回值为NULL
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')           # 该处只是实现将consumer函数转换成一个生成器，然后传入参数，并没有调用函数
    c2 = consumer('B')
    c.__next__()                # next方法唤醒生成器
							    # 第一次使用next方法的作用：开始调用执行函数，遇到yield就中断函数，返回yield接收的参数
							    # 后面使用next方法的作用：跳回上次函数yield中断的地方，继续执行函数，当遇到yield同样中断函数返回参数
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)               # send是生成器的一个方法，它即可以唤醒生成器，并且可以给生成器传递参数
                                # send方法的作用：跳回上次函数yield中断的地方，将参数传递给yield,继续执行函数，当遇到yield同样中断函数返回参数
        c2.send(i)

producer("alex")
#'''

