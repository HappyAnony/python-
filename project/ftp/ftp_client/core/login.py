#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

'''
登陆成功  1
登陆失败  0
'''


#from core import common
from core import request

class Login(object):
	def __init__(self,username,passwd):
		self.__username = username
		self.__passwd = passwd
	def user_login(self):
		print(self.__username)
		print(self.__passwd)
		req_obj = request.SendRequest()
		return req_obj.user_login(self.__username,self.__passwd)






def run():
	print("in the login")
	#print("in the register")
	_username = input("Username>>")
	_passwd = input("Password>>")
	login_object = Login(_username,_passwd)
	return login_object.user_login()