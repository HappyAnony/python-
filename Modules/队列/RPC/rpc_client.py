#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony


# 先启动服务端；然后启动客户端

import pika
import uuid


class FibonacciRpcClient(object):
	def __init__(self):
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(
			host='localhost'))  # 建立一个连接

		self.channel = self.connection.channel()   # 建立一个管道

		#  声明一个随机队列
		# exclusive=True表示会在使用此queue的消费者断开后,自动将queue删除
		result = self.channel.queue_declare(exclusive=True)
		self.callback_queue = result.method.queue

		# 声明客户端接收消息的配置
		# 将从上述声明的随机队列中接收数据
		# 接收数据后调用类中的on_response回调函数处理接收数据
		# no_ack表示不管回调函数是否处理完接收数据，都不会给rabbit服务端发送确认消息
		self.channel.basic_consume(self.on_response, no_ack=True,
		                           queue=self.callback_queue)

	def on_response(self, ch, method, props, body):
		# on_response是处理接收数据的回调函数
		# ch========connection.channel()声明的管道内存对象地址
		# props=====接收服务端basic_publish发布函数中properties参数的值
		# body======接收服务端basic_publish发布函数中body参数的值
		if self.corr_id == props.correlation_id:
			# props.correlation_id来自于服务端basic_publish发布函数中properties参数中correlation_id键值
			# 服务端basic_publish发布函数中properties参数中correlation_id键值来自于本地客户端basic_publish发布函数中properties参数中correlation_id键值
			# 验证这两值是否相等的作用是：保证当前接收值是服务端响应客户端发送消息的返回值，即保证消息的一致性
			self.response = body

	def call(self, n):
		self.response = None  # 存放服务端响应消息的返回值
		self.corr_id = str(uuid.uuid4()) # 生成一个消息一致性的标识符

		# 客户端发布消息给服务端
		# 客户端分发消息时直接将body指定的消息转发给routing_key参数指定的队列
		# 另外传递两个标识符：reply_to指定服务端返回响应消息时转发的队列[即客户端接收响应消息的队列]；correlation_id指定消息一致性标识符
		self.channel.basic_publish(exchange='',
		                           routing_key='rpc_queue',
		                           properties=pika.BasicProperties(
			                           reply_to=self.callback_queue,
			                           correlation_id=self.corr_id,
		                           ),
		                           body=str(n))

		# 客户端接收服务端响应消息
		# 由于采用的是非阻塞式的接收消息，所以需要轮询判断是否有消息接收进来
		while self.response is None:

			# 非阻塞式的start_consuming()接收信息
			# 如果声明的接收队列中没有数据，就执行下面命令语句，不会阻塞等待
			# 一旦声明的接收队列中有数据，就会调用声明的回调函数处理数据，处理完后再执行下面语句
			self.connection.process_data_events()
			pass
		return int(self.response)


fibonacci_rpc = FibonacciRpcClient() # 实例化类；调用__init__函数
print(" [x] Requesting fib(30)")

response = fibonacci_rpc.call(30) # 调用类中的call函数
print(" [.] Got %r" % response)