#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

'''
查看班级
查看班级学员列表
'''

from core import school
from core import student
from core import common


func_teacher_list = {
	"1":["查看班级","teacher.show_class()"],
	"2":["查看班级成员","teacher.show_classmates()"],
}

class Teacher(common.Members):
	def __init__(self,name,age,sex):
		super(Teacher,self).__init__(name,age,sex)
		self.courses_list = []
		self.grades_list = []

	def show_grades(self):
		print("in the class")

	def show_classmates(self):
		print("in the classmates")

	def show_courses(self):
		pass
	def show_course_members(self):
		pass


def teachers_register():
	pass


def run():
	print("in the teacher")
	func_teacher = common.Func(func_teacher_list)
	common.Func.func_exec_eq(func_teacher)