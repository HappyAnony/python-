#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

import sys
str_old = sys.argv[1]
str_new = sys.argv[2]

with open("python",'r',encoding="utf-8") as f, \
	 open("python_new",'w',encoding="utf-8") as f_new:
	for line in f:
		if str_old in line:
			line = line.replace(str_old,str_new)
		f_new.write(line)