#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 先启动服务端；然后启动客户端

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='localhost'))  # 建立一个连接

channel = connection.channel()  # 建立一个管道

channel.queue_declare(queue='rpc_queue')  # 声明服务端数据的接收管道

# 实现计算斐波那契数列
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)


# on_response是处理接收数据的回调函数
# ch========connection.channel()声明的管道内存对象地址
# props=====接收客户端basic_publish发布函数中properties参数的值
# body======接收客户端basic_publish发布函数中body参数的值
def on_request(ch, method, props, body):
	n = int(body)

	print(" [.] fib(%s)" % n)
	response = fib(n)

    # 服务端处理完客户端发来的消息后，将处理结果返回给客户端
	# 服务端返回消息时直接将body指定的处理结果转发给routing_key参数指定的队列[该队列是客户端声明的随机队列]
	# 另外服务端将接收到的消息一致性标识符props.correlation_id发还给客户端，以供客户端验证消息和处理结果的一致性
	ch.basic_publish(exchange='',
	                 routing_key=props.reply_to,
	                 properties=pika.BasicProperties(correlation_id= \
		                                                 props.correlation_id),
	                 body=str(response))

	# 回调函数处理完接收数据后，手动给rabbit服务端发送确认消息
	ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)  # 该处只需要在消费者端添加即可；实现公平分发[即通知rabbi服务端当前消息还没处理完的时候就不要再给我发新消息了]

# 声明服务端接收消息的配置
# 将从queue参数指定的队列中接收数据
# 接收数据后调用on_response回调函数处理接收数据
# 没有no_ack表示默认回调函数处理完接收数据后，会手动给rabbit服务端发送确认消息
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
# 阻塞式开始接收消息；一旦启动就会不停接收消息，没有消息时就会阻塞
channel.start_consuming()