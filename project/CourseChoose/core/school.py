#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

'''
创建班级
创建讲师
创建课程
'''
from core import student
from core import teacher
from core import common

func_admin_list = {
	"1":["创建班级","school.create_class()"],
	"2":["聘用老师","school.hire_teacher()"],
	"3":["创建课程","school.create_course()"]
}

school_members_list = [
	{"name":"希望中学","address":"湖北"},
	{"name":"衡水中学","address":"河北"}
]

school_members = []

class School(object):
	def __init__(self,name,address):
		self.name = name
		self.address =address
		self.__students_list = []
		self.__teachers_list = []
		self.__courses_list = []
		self.__grades_list = []

	def students_register(self,json_file):
		pass

	def element_register(self):
		pass

	def create_grade(self):
		print("in the create_grade")


	def remove_grade(self):
		pass

	def hire_teacher(self):
		print("in the hire_teacher")


	def fire_teacher(self):
		pass

	def create_course(self):
		print("in the course")

	def remove_course(self):
		pass

	def create_grade(self):
		pass

	def remove_grade(self):
		pass

def schools_register():
	for school_members_text in school_members_list:
		school_members.append( School(school_members_text["name"],school_members_text["address"]) )


def run():
	print("in the school")
	func_admin = common.Func(func_admin_list)
	common.Func.func_exec_eq(func_admin)

