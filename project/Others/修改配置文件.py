#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

import os
edit = [
	"<<1.query 查询信息>>",
    "<<2.add  添加信息>>",
    "<<3.del  删除信息>>"
]
query = [
	"list(l) 列出可查询的项并查询",
	"exit(e) 返回上层选择",
	"quit(q) 退出程序",
	#"NAME_OF_HA 返回指定查询项的信息"
]

add = [
	"exit(e) 返回上层选择",
	"quit(q) 退出程序",
]

arg = {
    'bakend': 'www.oldboy.org',
    'record':{
        'server': '100.1.7.9',
        'weight': 20,
        'maxconn': 30
    }
}
ha_name_list = []
exit_flag = True

def print_backend():
	with open('haproxy', 'r', encoding="utf-8") as f:
		for line in f:
			if "backend" in line and "use_backend" not in line:
				list_ha = line.split()
				ha_name_list.append(list_ha[1])
	for i in ha_name_list:
		print(i)


def del_backend(backend):
	with open('haproxy', 'r', encoding="utf-8") as f1, open('haproxy.new', 'w', encoding="utf-8") as f2:
		for line in f1:
			backend = "backend " + backend
			if backend in line and "use_backend" not in line:
				f1.readline()
				continue
			f2.write(line)
	with open('haproxy.new', 'r', encoding="utf-8") as f1, open('haproxy', 'w', encoding="utf-8") as f2:
		for line in f1:
			f2.write(line)
	#os.remove("haproxy.new")

while exit_flag:
	for line in edit:
		print(line)
	choice = input("plz enter the number>>")
	if choice.isdigit():
		choice = int(choice)
		if choice == 1:
			while exit_flag:
				for line in query:
					print(line)
				choice_query = input("plz enter your choose>>")
				if choice_query == 'q':
					exit_flag = False
				elif choice_query == 'e':
					break
				elif choice_query == 'l':
					# with open('haproxy','r',encoding="utf-8") as f:
					# 	for line in f:
					# 		if "backend" in line and "use_backend" not in line:
					# 			list_ha = line.split()
					# 			ha_name_list.append(list_ha[1])
					# for i in ha_name_list:
					# 	print(i)
					ha_name_list = []
					print_backend()
					while exit_flag:
						choice_query1 = input("HaName for query/q for quit/e for exit>>")
						if choice_query1 == 'q':
							exit_flag = False
						elif choice_query1 == 'e':
							break
						else:
							if choice_query1 in ha_name_list:
								choice_query1 = "backend " + choice_query1
								with open('haproxy', 'r', encoding="utf-8") as f1:
									for line in f1:
										if choice_query1 in line and "use_backend" not in line:
											record = f1.readline().split()
											print("server:%s" %record[1])
											print("weight:%s" %record[3])
											print("maxconn:%s" %record[5])


							else:
								print("\033[31;1mha not exit;plz enter agian\033[0m")


		elif choice == 2:
			while exit_flag:
				backend = input("plz enter the backend>>")
				server = input("plz enter the server ip>>")
				weight = input("plz enter the weight>>")
				maxconn = input("plz enter the maxconn>>")
				with open('haproxy','a',encoding="utf-8") as f:
					f.write("\nbackend %s\n" %backend)
					f.write("       server %s weight %s maxconn %s\n" %(server,weight,maxconn))
					#f.write("\n")
				print("Add successd!".center(50,'*'))
				judge = input("Are you cotinue?[no|yes|quit]>>")
				if judge == "no" or judge == "n":
					break
				if judge == "quit" or judge == "q":
					exit_flag = False

		elif choice == 3:
			while exit_flag:
				ha_name_list = []
				print_backend()
				backend_del = input("plz enter the backend to del>>")
				del_backend(backend_del)
				print("Del successd!".center(50,'*'))
				judge = input("Are you cotinue?[no|yes|quit]>>")
				if judge == "no" or judge == "n":
					break
				if judge == "quit" or judge == "q":
					exit_flag = False
		else:
			print("\033[31;1mValid input;plz enter 1/2/3\033[0m")
	elif choice == 'q' or choice == "quit":
		exit_flag = False
	else:
		print("\033[31;1mValid input;plz enter again\033[0m")