#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

import socket

client = socket.socket()   # 声明socket的协议簇类型[默认：family=AF_INET--ipv4]，协议类型[默认：type=SOCK_STREAM---tcp], 等[proto=0, fileno=None]
                           # 同时将socket类实例化，生成一个socket连接对象
print("生成的连接对象为：",client)

print('准备访问服务端')
client.connect(("192.168.80.128", 6969))  # 将服务端的ip和端口封装成元组传入，连接服务端
print('连接成功')

while True:
	msg = input(">>>:").strip()
	if msg == 'q':
		break
	if len(msg) == 0:
		continue
	client.send(msg.encode('utf-8'))
	data_size = client.recv(1024)
	print("需要接收的数据大小为:", data_size.decode())
	client.send("准备传输数据".encode('utf-8'))
	recv_data_size = 0

	while recv_data_size < int(data_size.decode()):
		data = client.recv(1024)
		print(data.decode())
		recv_data_size += len(data)
		print(recv_data_size)
	else:
		print("数据已接收完:", recv_data_size)



client.close()              # 关闭