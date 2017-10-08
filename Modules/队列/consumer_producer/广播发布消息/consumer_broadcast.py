#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony


# 生产者发布消息时，消费者必须同时在线接收，如果过会接收就无法接收到发布的消息

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='localhost'))  # 建立连接
channel = connection.channel() # 建立一个管道

# 声明将绑定使用哪个exchange转发器；与生产者保持一致
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# 声明消费者接收来自哪个队列的消息
# 不指定queue名字,rabbit会随机分配一个名字
# exclusive=True表示会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# 将随机分配的队列绑定到上述声明的exchange转发器上
# 此时绑定的exchange转发器中的消息就会转发给该随机队列
# 当消费端启动时，就会从该随机队列中接收到数据
channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
	print(" [x] %r" % body)


# 消费者将从queue参数指定的队列中接收数据
# 消费者接收数据后调用callback回调函数处理接收数据
# no_ack表示不管回调函数是否处理完接收数据，都不会给rabbit服务端发送确认消息
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

# 开始接收消息；一旦启动就会不停接收消息，没有消息时就会阻塞
channel.start_consuming()