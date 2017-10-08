#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony


'''
注册成功  1
注册失败  0
已经注册  1


输入用户名：
（1）先检测是否用户名是否存在
       存在则已经注册
       不存在进行第二步
（2）用户名合法性检测
（3）密码强度检测

'''

#import getpass
from core import common


class Register(object):
	def __init__(self,username,passwd):
		self.__username = username
		self.__passwd = passwd
	def user_register(self):
		print(self.__username)
		print(self.__passwd)

def run():
	#print("in the register")
	_username = input("Username>>")
	#_passwd = getpass.getpass("Password>>")
	_passwd = input("Password>>")
	#print(_username)
	#print(_passwd)
	reg_object = Register(_username,_passwd)
	reg_object.user_register()
	print("注册成功")