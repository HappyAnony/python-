#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 生产者发布消息时，消费者必须同时在线接收，如果过会接收就无法接收到发布的消息

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='localhost'))  # 建立连接
channel = connection.channel()  # 建立一个管道

# 在管道中声明一个exchange转发器，生产者发布的消息都会交给该转发器转发处理
# exchange===声明转发器的名字
# exchange_type=======声明转发器的类型
'''
fanout:===将接收到的来自生产者的消息转发给所有bind到此exchange的queue
direct:===将接收到的来自生产者的消息转发给通过routingKey和exchange决定的那个唯一的queue
topic:====将接收到的来自生产者的消息转发给所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue
'''
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"  # 此处表示：如果命令行启动则接受命令行参数作为分发消息否则将默认字符串作为分发消息

# 分发消息时直接将body指定的消息转发给exchange指定的转发器
# 转发器根据上述声明的类型进行相应的转发处理
# 此处转发器类型为fanout，转发器会将消息转发给所有绑定到自己的队列中去
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(" [x] Sent %r" % message)
connection.close()