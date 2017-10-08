#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony


import socket
import os
import hashlib

server = socket.socket()
server.bind(("localhost",6969))   # 第一个参数：指定侦听的ip【0.0.0.0表示任意主机】；第二个参数：绑定侦听的端口
server.listen()                   # 侦听刚绑定的ip和端口

while True:
	print("等待响应")
	conn, addr = server.accept()
	print("有人访问，开始响应")
	print("访问对象：", conn)
	print("访问地址和端口", addr)

	while True:
		data = conn.recv(1024).decode('utf-8')
		if not data:
			print("主机已断开")
			break
		if len(data) == 0:
			conn.send("命令输入异常".encode())
			continue
		cmd, file_name = data.split()
		print("命令为:",cmd)
		print("文件为:",file_name)
		if cmd.strip() == 'get' and os.path.isfile(file_name.strip()):
			f = open(file_name.strip(),'rb',encoding='utf-8')
			m = hashlib.md5()
		else:
			pass
		conn.send(str(len(revl.encode())).encode('utf-8'))
		revl_ack = conn.recv(1024)
		print(revl_ack.decode())
		conn.send(revl.encode('utf-8'))
		print("数据已发生完毕")

server.close()