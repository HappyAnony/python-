#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

import re


cal_str = "-87+(9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14)- 9/(-3)"

def convert(old_str):
	if re.search('\+\s*\-',old_str) != None:
		old_str = re.sub('\+\s*\-','-',old_str)
	if re.search('\-\s*\-',old_str) != None:
		old_str = re.sub('\-\s*\-','+',old_str)
	return old_str

def cal_multi_devid(str_mlti_devid):
	while True:
		str_mlti_devid = convert(str_mlti_devid)
		multi_devid = re.search('[0-9]+(\.)?[0-9]*\s*[/*]\s*(\-)?[0-9]+(\.)?[0-9]*',str_mlti_devid)
		if None == multi_devid:
			break
		else:
			if '*' in multi_devid.group():
				element = multi_devid.group().split('*')
				value = eval(element[0].strip()) * eval(element[1].strip())
			else:
				element = multi_devid.group().split('/')
				value = eval(element[0].strip()) / eval(element[1].strip())
			str_mlti_devid = re.sub('[0-9]+(\.)?[0-9]*\s*[/*]\s*(\-)?[0-9]+(\.)?[0-9]*',str(value),str_mlti_devid,count=1)
			print(str_mlti_devid)
	print(str_mlti_devid)
	return str_mlti_devid


def split(old_str):
	if re.search('\-',old_str) != None:
		old_str = re.sub('\-','+-',old_str)
	return old_str

def cal_plus_minus(str_plus_minus):
	str_plus_minus = split(str_plus_minus)
	while True:
		plus_minus = re.search('(\-)?\s*[0-9]*(\.)?[0-9]*\s*\+\s*(\-)?\s*[0-9]+(\.)?[0-9]*',str_plus_minus)
		if None == plus_minus:
			break
		else:
			element = plus_minus.group().split('+')
			if element[0] == '' or element[0].isspace():
				element[0] = str(0)
			value = eval(element[0].strip()) + eval(element[1].strip())
			str_plus_minus = re.sub('(\-)?\s*[0-9]*(\.)?[0-9]*\s*\+\s*(\-)?\s*[0-9]+(\.)?[0-9]*',str(value),str_plus_minus,count=1)
	print(str_plus_minus)
	return str_plus_minus


def cal_bracket(str_bracket):
	while True:
		bracket = re.search(r'\([^()]+\)',str_bracket)
		if None == bracket:
			break
		else:
			bracket = bracket.group()[1:-1]
			if '*' in bracket or '/' in bracket:
				reval_multi_devid = cal_multi_devid(bracket)
			else:
				reval_multi_devid = bracket
			reval_plus_minus = cal_plus_minus(reval_multi_devid)
			str_bracket = re.sub(r'\([^()]+\)',str(reval_plus_minus),str_bracket,count=1)
	return str_bracket




def cal(math_str):
	if re.search('[()]',math_str) != None:
		math_str = cal_bracket(math_str)
	if re.search('[/*]',math_str) != None:
		math_str = cal_multi_devid(math_str)
	math_str = cal_plus_minus(math_str)
	return math_str


cal(cal_str)

# cal = cal_bracket(cal)
# cal = cal_multi_devid(cal)
# cal = cal_plus_minus(cal)
# print(cal)
