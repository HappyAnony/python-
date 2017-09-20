#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

'''
1.注册
2.报名缴费
3.选择班级
'''
from core import school
from core import teacher
from core import common


func_student_list = {
	"1":["注册报名","student.register_info()"],
	"2":["报名缴费","student.pay_tuition()"],
	"3":["选择班级","student.choose_course()"]
}

student_members_list = [
	{"name":"anony","age":18,"sex":"man"},
	{"name":"jack","age":19,"sex":"man"}
]

student_members = []


class Students(common.Members):
	def __init__(self,name,age,sex):
		super(Students,self).__init__(name,age,sex)
		self.__grade = None
		self.courses_list = []

	def show_grade_info(self):
		print("in the register")

	def show_courses_choose(self):
		pass
	
	def choose_course(self):
		print("in the course")


def students_register():
	pass
	

def run():
	print("in the student")
	func_student = common.Func(func_student_list)
	common.Func.func_exec_eq(func_student)