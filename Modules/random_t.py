#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony
'''
import random
print(random.random())  # 返回[0,1)之间的随机浮点数
print(random.uniform(1,3)) # 返回[1,3)之间的随机浮点数
print(random.randint(1,4)) # 返回[1,4]之间的随机整数
print(random.randrange(1,4)) # 返回[1,4)之间的随机整数
print(random.choice([4,6,6,1,3])) # 返回指定序列(字串，元组，列表，字典等)中的随机元素
print(random.sample([4,6,1,3],2))# 从指定序列(字串，元组，列表，字典等)中，随机获取指定长度的片段
items = [4,6,6,1,3]
print(items)
random.shuffle(items) # 打乱指定对象中元素的次序
print(items)
'''

import random
exit_flag = True
while exit_flag:
	checkcode = ''
	count = input("plz enter the length of checkcode(q for quit)>>")
	if count == 'q':
		exit_flag = False
	elif count.isdigit():
		count = int(count)
		for i in range(count):
			current = random.randrange(count)
			# 生成字母
			if current == i:
				tmp_char = chr(random.randint(65,90))
			else:
				tmp_char = random.randint(0,9)
			checkcode += str(tmp_char)
		print(checkcode)
	else:
		print("\033[31;1mValid input,plz enter again\033[0m")
