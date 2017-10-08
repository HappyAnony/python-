#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
	'localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello',durable=True)   # queue声明队列名；durable声明队列持久化[注意：此时队列中数据并没有持久化；生产端消费端都要加]


def callback(ch, method, properties, body):
	# 回调函数执行完了就代表消息处理完毕；没有执行完就代表消息没有处理完毕
	# 默认会传入4个参数
	# ch==connection.channel()声明的管道内存对象地址
	# method==
	# properties==与生产者分发信息时声明的队列消息持久化相对应
	print("--->",ch)
	time.sleep(30)
	print(" [x] Received %r" % body)
	ch.basic_ack(delivery_tag=method.delivery_tag) # 手动发送消息处理完毕的确认给rabbit服务端


channel.basic_qos(prefetch_count=1)  # 该处只需要在消费者端添加即可；实现公平分发[即通知rabbit服务端当前消息还没处理完的时候就不要再给我发新消息了]

# 只是声明相关配置信息
channel.basic_consume(callback,     # 如果收到消息就调用callback函数处理消息
                      queue='hello',  # 声明从哪个队列收消息
                      #no_ack=True   # 该语句表示不管消息处理完没都不会给rabbit服务端发确认消息，即服务端不关心消息是否被处理完，发送完消息后，队列中的相关数据就会被删除
                                     # 注释该语句表示会给rabbit服务端发送确认消息，即服务端没有收到确认就默认消息还没有处理完，就不会将队列中的数据删除，同时会连接下一个消费者交其处理
                                     # 但是要注意的是：确认是等消息处理完后才发，然而消息是否处理完取决于callback回调函数是否执行完，为了避免开销过大，需要在callback中手动确认消息处理完了
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始接收消息；一旦启动就会不停接收消息，没有消息时就会阻塞
channel.start_consuming()