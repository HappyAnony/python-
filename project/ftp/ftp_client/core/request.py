#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

import socket
import json
from conf import settings

class SendRequest(object):
	def __init__(self):
		self.__clientObj = socket.socket()

	def connect_server(self,ServerHost,ServerPort):
		print("生成的连接对象为：", self.__clientObj)
		print('准备访问服务端')
		self.__clientObj.connect((ServerHost,ServerPort))  # 将服务端的ip和端口封装成元组传入，连接服务端
		print('连接成功')

	def send_request(self,ReqDict):
		self.__clientObj.send(json.dumps(ReqDict).encode('utf-8'))

	def send_data(self,data):
		data_size = len(data.strip())
		self.__clientObj.send(str(data_size).encode('utf-8'))
		self.__clientObj.recv(1024)
		self.__clientObj.send(data.encode('utf-8'))

	def receive_data(self):
		data_size = self.__clientObj.recv(1024)             # 接收数据的大小
		print("需要接收的数据大小为:", data_size.decode())
		self.__clientObj.send("准备接收数据".encode('utf-8'))
		recv_data_size = 0
		while recv_data_size < int(data_size.decode()):
			size = 1024 if (int(data_size.decode())-recv_data_size) < 1024 else  (int(data_size.decode())-recv_data_size)
			data = self.__clientObj.recv(size)
			print(data.decode())
			recv_data_size += len(data)
			print(recv_data_size)
		else:
			print("数据已接收完:", recv_data_size)
		return view

	def user_login(self,username,password):
		LoginDict = {}
		LoginDict["username"] = username
		LoginDict["passwd"] = password
		LoginDict["action"] = "login"
		print(LoginDict)
		self.send_request(LoginDict)
		return self.receive_data()


	def user_register(self,username,password):
		RegDict = {}
		RegDict["username"] = username
		RegDict["passwd"] = password
		RegDict["action"] = "register"
		print(RegDict)
		self.send_request(RegDict)



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