#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony


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
	events = sel.select()  #默认阻塞，有活动链接就返回活动的链接列表
	for key, mask in events:
		callback = key.data  # 第一次循环调用accept函数；第二次以及之后的循环调用read函数
		callback(key.fileobj, mask) #key.fileobj=文件句柄；给回调函数传入两个参数