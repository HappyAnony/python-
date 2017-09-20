#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

from core import school
from core import student
from core import teacher
from core import main

class Func(object):
	def __init__(self,func_list):
		self.func_list =func_list

	def func_print(self):
		print("\033[32;1mstart print func info\033[0m".center(50, '*'))
		for func_id in self.func_list:
			print("%s: %s" %(func_id,self.func_list[func_id][0]))
		print("\033[32;1mprint func info end\033[0m".center(50,'*'))


	def func_exec_common(self,choice_user):
		invilid_flag = True
		for func_id in self.func_list:
			if choice_user == func_id:
				invilid_flag = False
				eval(self.func_list[func_id][1])
		if invilid_flag:
			print("\033[31;1mInvilid input;plz enter again\033[0m")

	@staticmethod
	def func_exec_eq(obj):
		while True:
			obj.func_print()
			choice_id = input("\033[32;1mplz enter your choice_id(q for quit;e for exit)>\033[0m")
			if choice_id == 'e':
				main.run()
			if choice_id == 'q':
				exit()
			obj.func_exec_common(choice_id)

	@staticmethod
	def func_exec_q(obj):
		while True:
			obj.func_print()
			choice_id = input("\033[32;1mplz enter your choice_id(q for quit;e for exit)>\033[0m")
			if choice_id == 'q':
				exit()
			obj.func_exec_common(choice_id)

	def func_register(self,func_id,func_text,func_name):
		pass



class Course(object):
	def __init__(self,name,teacher):
		self.name = name
		self.teacher = teacher
		self.students_list = []


class Grade(object):
	def __init__(self,name,monitor):
		self.name = name
		self.monitor = monitor
		self.students_list = []


class Members(object):
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex





