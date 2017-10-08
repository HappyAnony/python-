#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 多线程、多进程实现高并发响应请求

import socket
import os
import socketserver

class MyTcpHandler(socketserver.BaseRequestHandler):
	'''
	First, you must create a request handler class by subclassing the BaseRequestHandlerclass
	and overriding its handle() method;
	this method will process incoming requests
	'''
	# handle负责处理所有的业务逻辑
	def handle(self):
		while True:
			try:
				self.data = self.request.recv(1024).decode().strip()
				print("有人访问，开始响应")
				print("访问对象：", self.client_address)
				revl = os.popen(self.data).read()
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


if __name__ == "__main__":
	HOST, PORT = "localhost",6969
	# you must instantiate one of the server classes, passing it the server’s address and the request handler class
	'''
	server classes单线程：
	       class socketserver.TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)
	       class socketserver.UDPServer(server_address, RequestHandlerClass, bind_and_activate=True)
	       class socketserver.UnixStreamServer(server_address, RequestHandlerClass, bind_and_activate=True)
           class socketserver.UnixDatagramServer(server_address, RequestHandlerClass,bind_and_activate=True)
	server classes多线程：
		   class socketserver.ThreadingTCPServer
		   class socketserver.ThreadingUDPServer
    server classes多进程===该处会调用os.fork()方法创建一个新进程，但是win上没有fork方法，所以多进程类无法在win上实现
		   class socketserver.ForkingTCPServer
		   class socketserver.ForkingUDPServer
	'''
	#server = socketserver.TCPServer((HOST,PORT), MyTcpHandler)   # 单线程
	server = socketserver.ThreadingTCPServer( (HOST, PORT), MyTcpHandler ) # 多线程

	# Then call the handle_request() or serve_forever() method of the server object to process one or many requests.
	server.serve_forever()     # 处理多个请求，永远执行
	# server.handle_request()  # 只处理一个请求

	# Finally, call server_close() to close the socket.
	server.server_close()
