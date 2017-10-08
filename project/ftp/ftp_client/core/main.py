#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

from core import login
from core import register
from conf import settings
from core import workstation


def run():
	print("in the main of tfpclient")
	for key in settings.info_main:
		print(key, settings.info_main[key])
	while True:
		choice = input("login or register[q for quit]:>>")
		if choice == 'q':
			break
		elif choice == 'login' or choice == '登陆':
			reval,home_dir = login.run()
			if reval:
				workstation.run(home_dir)
			else:
				print("you have only three choice;you may try again")
		elif choice == 'register' or choice == '注册':
			register.run()
		elif len(choice) == 0:
			continue
		else:
			print("Invid Input;Plz enter again")
