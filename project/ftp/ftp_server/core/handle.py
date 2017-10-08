#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

import os
import socketserver
import jsonI
from conf import settings



# class HandleRequest(object):
# 	def __init__(self):
# 		pass
#
# 	def login(self):
# 		pass
#
# 	def register(self):
# 		pass


class MyTcpHandler(socketserver.BaseRequestHandler):
	'''
	First, you must create a request handler class by subclassing the BaseRequestHandlerclass
	and overriding its handle() method;
	this method will process incoming requests
	'''

	def receive_data(self):
		pass

	def send_response(self):
		pass

	def login(self):
		pass

	def register(self):
		pass

	def list(self):
		pass

	def bye(self):
		pass

	# handle负责处理所有的业务逻辑
	def handle(self):
		handle_obj = HandleRequest()
		while True:
			try:
				self.data = self.request.recv(1024).decode().strip()
				print("有人访问，开始响应")
				print("访问对象：", self.client_address)

				if len(revl) == 0:
					revl = "命令输入异常"
				self.request.send(str(len(revl.encode())).encode('utf-8'))
				revl_ack = self.request.recv(1024)
				print(revl_ack.decode())
				self.request.send(revl.encode('utf-8'))
				print("数据已发生完毕")
			except ConnectionResetError as e:
				print("ConnetctionError",e)
				break










def run():
	HOST, PORT = settings.ServerInfo["IP"],settings.ServerInfo["PORT"]
	server = socketserver.ThreadingTCPServer( (HOST, PORT), MyTcpHandler )
	server.serve_forever()
	server.server_close()