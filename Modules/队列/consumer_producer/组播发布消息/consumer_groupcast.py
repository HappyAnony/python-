#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 生产者发布消息时，消费者必须同时在线接收，如果过会接收就无法接收到发布的消息


#***********************************************粗略过滤****************************************************************

''''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='localhost'))  # 建立连接
channel = connection.channel()  # 建立一个管道

# 声明将绑定使用哪个exchange转发器；与生产者保持一致
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

# 声明消费者接收来自哪个队列的消息
# 不指定queue名字,rabbit会随机分配一个名字
# exclusive=True表示会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# 通过命令行参数获取待绑定到exchange转发器的随机队列可接受信息的级别类型
severities = sys.argv[1:]
if not severities:
	sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
	sys.exit(1)

# 将随机分配的队列绑定到上述声明的exchange转发器上
# 将通过命令行参数指定的消息级别类型绑定到上述随机队列上
# 此时绑定的exchange转发器中的消息就会转发给消息级别有生产端routing_key参数指定值的随机队列中去
# 当消费端启动时，就会从该随机队列中接收到数据
for severity in severities:
	channel.queue_bind(exchange='direct_logs',
	                   queue=queue_name,
	                   routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
	print(" [x] %r:%r" % (method.routing_key, body))

# 消费者将从queue参数指定的队列中接收数据
# 消费者接收数据后调用callback回调函数处理接收数据
# no_ack表示不管回调函数是否处理完接收数据，都不会给rabbit服务端发送确认消息
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

'''
#***********************************************细致过滤****************************************************************

'''
此处和上述粗略过滤不同在于:
（1）exchange_type的值为topic
（2）routingKey可以是一个匹配表达式
		To receive all the logs run:
		python receive_logs_topic.py "#"
		
		To receive all logs from the facility "kern":
		python receive_logs_topic.py "kern.*"
		
		Or if you want to hear only about "critical" logs:
		python receive_logs_topic.py "*.critical"
		
		You can create multiple bindings:
		python receive_logs_topic.py "kern.*" "*.critical"
		
		And to emit a log with a routing key "kern.critical" type:
		python emit_log_topic.py "kern.critical" "A critical kernel error"
'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='localhost'))
channel = connection.channel()


channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
	sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
	sys.exit(1)

for binding_key in binding_keys:
	channel.queue_bind(exchange='topic_logs',
	                   queue=queue_name,
	                   routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
	print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()