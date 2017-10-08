#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
	'localhost'))                                               # 建立socket连接
channel = connection.channel()       # 建立一个管道

# 声明queue
channel.queue_declare(queue='hello',durable=True)  # queue声明队列名；durable声明队列持久化[注意：此时队列中数据并没有持久化；生产端消费端都要加]

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent==此处实现的才是队列中消息持久化；此处只需要在生产端添加即可
                      ))
# routing key==声明的queue的队列名
# body==消息内容

print(" [x] Sent 'Hello World!'")
connection.close()