#!/usr/bin/env python
# -*-coding :utf-8 -*-
# Author:Anony

import socket
import os

server = socket.socket()
server.bind(("localhost",6969))   # 第一个参数：指定侦听的ip【0.0.0.0表示任意主机】；第二个参数：绑定侦听的端口
server.listen()                   # 侦听刚绑定的ip和端口

while True:
	print("等待响应")
	conn, addr = server.accept()  # wating等待响应
	# conn为客户端连接过来时在服务端为其生成的一个连接实例
	print("有人访问，开始响应")
	print("访问对象：", conn)
	print("访问地址和端口", addr)

	while True:
		data = conn.recv(1024).decode('utf-8')          # 接收,当客户端send一个空字串时，服务端当做是没有接收到任何信息，一直处于阻塞等待的状态
		                                                # recv缓存区允许recv一次最大只能接收几十k的数据，跟系统有关；官方建议8192
		print("接收数据为:",data)
		if not data:
			print("主机已断开")
			break
		revl = os.popen(data).read()    # popen执行命令后会将命令结果存放到一个临时文件中，并返回一个文件句柄
		                                # 只有当命令执行完后才返回文件句柄,所以当执行不存在的命令或者动态刷新的命令时，返回为空文件句柄
		#print(type(revl))
		if len(revl) == 0:
			revl = "命令输入异常"
		conn.send(str(len(revl.encode())).encode('utf-8'))  # len(revl)和len(revl.encode())的大小是不一样的，因为一字节中文字符经过utf-8编码后变成3字节了
		revl_ack = conn.recv(1024)  # 解决数据粘包
		print(revl_ack.decode())
		conn.send(revl.encode('utf-8'))  # send不能发送空字串
		print("数据已发生完毕")
		#conn.send(data.upper())         # 发送，send缓冲区允许send一次最大只能发送几十k的数据,要想发送大容量数据，可以使用sendall()

server.close()