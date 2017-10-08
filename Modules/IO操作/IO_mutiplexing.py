#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony




#****************************************************select模块************************************************************
# 使用select模式实现IO多路复用

'''
import select
import socket
import sys
import queue

server = socket.socket()
server.setblocking(0)

server_addr = ('localhost',10000)

print('starting up on %s port %s' % server_addr)
server.bind(server_addr)

server.listen(5)

inputs = [server, ] #自己也要监测呀,因为server本身也是个fd
outputs = []

message_queues = {}

while True:
    print("waiting for next event...")
    readable, writeable, exeptional = select.select(inputs,outputs,inputs) #如果没有任何fd就绪,那程序就会一直阻塞在这里
    for s in readable: #每个s就是一个socket
        if s is server: #别忘记,上面我们server自己也当做一个fd放在了inputs列表里,传给了select,如果这个s是server,代表server这个fd就绪了,
            #就是有活动了, 什么情况下它才有活动? 当然 是有新连接进来的时候 呀
            #新连接进来了,接受这个连接
            conn, client_addr = s.accept()
            print("new connection from",client_addr)
            conn.setblocking(0)
            inputs.append(conn) #为了不阻塞整个程序,我们不会立刻在这里开始接收客户端发来的数据, 把它放到inputs里, 下一次loop时,这个新连接
            #就会被交给select去监听,如果这个连接的客户端发来了数据 ,那这个连接的fd在server端就会变成就续的,select就会把这个连接返回,返回到
            #readable 列表里,然后你就可以loop readable列表,取出这个连接,开始接收数据了, 下面就是这么干 的

            message_queues[conn] = queue.Queue() #接收到客户端的数据后,不立刻返回 ,暂存在队列里,以后发送

        else: #s不是server的话,那就只能是一个 与客户端建立的连接的fd了
            #客户端的数据过来了,在这接收
            data = s.recv(1024)
            if data:
                print("收到来自[%s]的数据:" % s.getpeername()[0], data)
                message_queues[s].put(data) #收到的数据先放到queue里,一会返回给客户端
                if s not  in outputs:
                    outputs.append(s) #为了不影响处理与其它客户端的连接 , 这里不立刻返回数据给客户端

            else:#如果收不到data代表什么呢? 代表客户端断开了呀
                print("客户端断开了",s)
                if s in outputs:
                    outputs.remove(s) #清理已断开的连接
                inputs.remove(s) #清理已断开的连接
                del message_queues[s] ##清理已断开的连接

    for s in writeable:
        try :
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            print("client [%s]" %s.getpeername()[0], "queue is empty..")
            outputs.remove(s)
        else:
            print("sending msg to [%s]"%s.getpeername()[0], next_msg)
            s.send(next_msg.upper())

    for s in exeptional:
        print("handling exception for ",s.getpeername())
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
'''

#***************************************************selectors模块**********************************************************
# 该模块默认使用epoll模式实现IO多路复用
# 如果无法找到epoll模式[win上]，就使用select模式
# 在linux中，epoll是基于libevent.so实现的


import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):  # 建立连接
	conn, addr = sock.accept()  # Should be ready
	print('accepted', conn, 'from', addr)
	conn.setblocking(False)
	sel.register(conn, selectors.EVENT_READ, read)  #建立连接后注册read回调函数


def read(conn, mask):    # 读取连接数据
	data = conn.recv(1000)  # Should be ready
	if data:
		print('echoing', repr(data), 'to', conn)
		conn.send(data)  # Hope it won't block
	else:
		print('closing', conn)
		sel.unregister(conn)
		conn.close()


sock = socket.socket()
sock.bind(('localhost', 10000))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
	events = sel.select()  # 默认阻塞，有活动连接就返回活动的连接列表
	for key, mask in events:
		callback = key.data  # 第一次循环调用accept函数建立连接；第二次以及之后的循环调用read函数读取连接数据
		callback(key.fileobj, mask) #key.fileobj=文件句柄；给回调函数传入两个参数