#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 参考文档：http://www.cnblogs.com/alex3714/articles/5248247.html
# 官方文档：http://www.rabbitmq.com/getstarted.html


'''
RabbitMQ可以实现的模型：
一：生产者消费者模型：[生产者发布信息；消费者接收信息==信息流单向]
（1）一对一单播：生产者生产数据，消费者接收数据
（2）一对多单播：生产者生产数据，消费者轮询接收数据
（3）一对多多播：生产者生产数据，所有消费者同时接受到数据[广播、组播]

二：RPC模型：remote procedure call[通信双方互相发送数据==信息流双向]
实现逻辑：通信双方既是生产者也是消费者

rabbit服务端：
（1）默认rabbit服务端中队列存放的数据是在内存中，一旦宕机数据都会消失，所以需要做消息队列持久化
（2）消费者从服务端获取数据进行处理后默认需要手动发送确认消息给服务端；服务端收到确认消息会删除队列中的数据，如果没有收到表示数据还没有处理完，就会保留队列中的数据不会删除
（3）在rabbit安装路径的sbin目录下有几个可以操作rabbit的命令文件。其中rabbitmqctl可以用来查询队列信息[rabbitmqctl.bat list_queues]
'''

