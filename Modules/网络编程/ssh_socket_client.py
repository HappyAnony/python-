#!/usr/bin/env python
# -*-coding :utf-8 -*-
# Author:Anony


# 参考文档：http://www.cnblogs.com/wupeiqi/articles/5040823.html
# 参考文档：http://www.cnblogs.com/alex3714/articles/5830365.html
# socket是对所有上层协议的底层封装
# socket支持tcp，也支持udp

import socket

client = socket.socket()   # 声明socket的协议簇类型[默认：family=AF_INET--ipv4]，协议类型[默认：type=SOCK_STREAM---tcp], 等[proto=0, fileno=None]
                           # 同时将socket类实例化，生成一个socket连接对象
print("生成的连接对象为：",client)

print('准备访问服务端')
client.connect(("localhost", 6969))  # 将服务端的ip和端口封装成元组传入，连接服务端
print('连接成功')

while True:
	msg = input(">>>:").strip()
	if msg == 'q':
		break
	if len(msg) == 0:       # send不能发送回车，空格键，tab键等空字串，因为recv接收空字串时当做没有接收到任何信息，一直处于阻塞等待状态
		                    # 此时如何客户端发送空字串，服务端一直处于recv等待状态，无法发送
		                    # 服务端没有发送回应，客户端也处于一直recv等待状态。此时客户端和服务端都会出现卡死状态。
		continue
	#client.send(b"hello world")  # 发送数据，在python3中只能发送bytes类型的二进制流
	client.send(msg.encode('utf-8'))  # bytes类型只能接收ASCII字符，不能接收中文，于是需要使用encode将其编码，encode后就是bytes类型
	                                  # send不能发送空
	                                  # 发送，send缓冲区允许send一次最大只能发送几十k的数据，要想发送大容量数据，可以使用sendall()
	data_size = client.recv(1024)
	print("需要接收的数据大小为:", data_size.decode())
	client.send("准备传输数据".encode('utf-8'))   # 解决数据粘包
	#data = client.recv(1024)    # 接收数据，recv缓存区允许recv一次最大只能接收几十k的数据，跟系统有关；官方建议8192
	recv_data_size = 0

	while recv_data_size < int(data_size.decode()):
		data = client.recv(1024)
		print(data.decode())
		recv_data_size += len(data)
		print(recv_data_size)
	else:
		print("数据已接收完:", recv_data_size)

	#print("接收数据为：",data.decode())
	#print(data.decode('utf-8'))                 # 打印命令的输出结果

client.close()              # 关闭