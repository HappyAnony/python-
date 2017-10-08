#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 队列可以实现程序的解耦
# 队列可以提高处理效率
# 队列可以实现线程间通信
# 队列可以理解为类似于列表用来存放数据的容器，不同的是：队列的数据只有一份，取走了就没有了

#**********************************************************queue队列****************************************************
# 参考文档：http://www.cnblogs.com/alex3714/articles/5230609.html

# 先入先出
'''
import queue
q = queue.Queue(maxsize=2)  # 先入先出;maxsize指定了队列的大小【即item的数量】
print(q.empty())  # 判断队列是否为空
# put(item, block=True, timeout=None)
# item：放进队列的数据；要求是一个可迭代对象
# block：设置当队列数据占满时是否阻塞。默认True表示阻塞：直到队列空出一个位置将上述的item数据存放到队列中；False表示不阻塞：抛出queue.Full异常
# timeout：设置超时时间，作用于阻塞情况。默认None：表示一直处于阻塞；NUM：表示NUM时间内如果队列依然full，没有将指定的item存放到队列中，则抛出queue.Full异常
q.put("anony",block=True,timeout=3)
q.put_nowait("jack")  # 效果相当于q.put("jack",block=False)
print(q.full())  # 判断队列是否为full
print(q.qsize()) # 获取当前队列的大小

# get(block=True, timeout=None)
# block：设置当队列为空时是否阻塞。默认True表示阻塞：直到队列中存在数据然后取出该数据；False表示不阻塞：抛出queue.Empty异常
# timeout：设置超时时间，作用于阻塞情况。默认None：表示一直处于阻塞；NUM：表示NUM时间内如果队列依然empty，没有数据可取，则抛出queue.Empty异常
print(q.get(block=True,timeout=3))
print(q.get_nowait())               # 效果相当于q.get(block=False)
print(q.qsize()) # 获取当前队列的大小
'''





# 后进先出
'''
import queue
q = queue.LifoQueue(maxsize=2) # 后进先出
print(q.empty())  # 判断队列是否为空

q.put("anony",block=True,timeout=3)
q.put_nowait("jack")

print(q.full())  # 判断队列是否为full
print(q.qsize()) # 获取当前队列的大小

print(q.get(block=True,timeout=3))
print(q.get_nowait())
print(q.qsize())
'''

# 按照优先级进出
'''
import queue
q = queue.PriorityQueue(maxsize=2)  # 存储数据时设置优先级的队列
print(q.empty())  # 判断队列是否为空
# 此时put方法中的item的写法与上述两种列表不同，形式是：(priority_number, data)
# 整体是一个元组
# 第一个元素为数据的优先级，用整数表示【数值越小优先级越高，越先出队列】
# 第二个元素为数据本身
q.put((6,"anony"),block=True,timeout=3)
q.put_nowait((4,"jack"))
print(q.full())
print(q.qsize())

print(q.get(block=True,timeout=3))
print(q.get_nowait())
print(q.qsize())

'''

#**********************************************************生产者消费者模式***********************************************

'''
生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题;生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯
	所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列
	消费者不找生产者要数据，而是直接从阻塞队列里取
	阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力

生产者消费者模型是解耦的实现方式
队列是解耦的实现工具
'''


import time,random
import queue,threading
q = queue.Queue()
def Producer(name):
  count = 0
  while count <20:
    time.sleep(random.randrange(3))
    q.put(count)
    print('Producer %s has produced %s baozi..' %(name, count))
    count +=1
def Consumer(name):
  count = 0
  while count <20:
    time.sleep(random.randrange(4))
    if not q.empty():
        data = q.get()
        print(data)
        print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
    else:
        print("-----no baozi anymore----")
    count +=1
p1 = threading.Thread(target=Producer, args=('A',))
c1 = threading.Thread(target=Consumer, args=('B',))
p1.start()
c1.start()

