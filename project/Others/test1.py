#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony
import os
with open('haproxy', 'r', encoding="utf-8") as f1, open('haproxy.new','w',encoding="utf-8") as f2:
	for line in f1:
		if "backend www.oldboy.org" in line and "use_backend" not in line:
			f1.readline()
			continue
		f2.write(line)

with open('haproxy.new','r',encoding="utf-8") as f1, open('haproxy','w',encoding="utf-8") as f2:
	for line in f1:
		f2.write(line)

os.remove("haproxy.new")


