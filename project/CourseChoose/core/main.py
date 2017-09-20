#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

from core import school
from core import student
from core import teacher
from core import common


func_main_list = {
	"1":["admin","school.run()"],
	"2":["teacher","teacher.run()"],
	"3":["student","student.run()"]
}




def register_init():
	school.schools_register()
	student.students_register()
	teacher.teachers_register()


def run():
	print("in the main")
	register_init()
	func_main = common.Func(func_main_list)
	common.Func.func_exec_q(func_main)


