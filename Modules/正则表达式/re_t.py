#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 参考文档 http://www.cnblogs.com/alex3714/articles/5161349.html

'''
'.'     默认匹配除\n之外的任意一个字符，若指定flags = DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags = MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
'*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次
'[]'    匹配指定范围内的单个字符,[a-z],[a-zA-Z0-9],[()],[/*]
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c


'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'    匹配字符结尾，同$
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
'\s'    匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
'''


import re

print(dir(re))
print(re.search("(?P<province>[0-9]{2})(?P<city>[0-9]{2}).{2}(?P<birthday>[0-9]{4})","371481199306143242").groupdict())
c = re.search("(?P<province>[0-9]{2})(?P<city>[0-9]{2}).{2}(?P<birthday>[0-9]{4})","371481199306143242").groupdict()
print(c["city"])
print(re.split("[0-9]+","dag25def34defg"))
print(re.split("[0-9]","dag25def34defg"))
print(re.sub("[0-9]+","|","dag25def34defg"))
print(re.sub("[0-9]+","|","dag25def34defg",count=1))
print(re.search("[0-9]+","dagdefdefg"))



# print(re.search("[0-9]*","abc4634eee").group())
'''常用方法
re.match 从头开始匹配，相当于匹配模式前面加上^，返回匹配到的第一个内容对象；没有group方法。一般不采用
re.search 匹配包含，返回匹配到的第一个内容对象。可以使用group方法返回具体内容
re.findall 把所有匹配到的字符放到以列表中的元素返回，没有group方法
re.splitall 以匹配到的字符当做列表分隔符
re.sub      匹配字符并替换,默认替换所有匹配到的内容；可以通过count参数指定替换的个数
'''
'''匹配模式
re.I、re.IGNORECASE: 忽略大小写
re.M、re.MULTILINE: 多行模式，改变'^'和'$'的行为
re.S、re.DOTALL: 点任意匹配模式，改变'.'的行为
'''
# print(re.match("a","abc\neee"))
# print(re.match("^a","abc\naee"))
# print(re.match("a","cabc\neee"))
# print(re.search("^a","\nabc\neee",flags=re.MULTILINE))
# print(re.search("^a","\nabc\neee",flags=re.MULTILINE).group())
# print(re.search(".","\nabc\neee").group())
# print(re.search(".","\n",flags=re.DOTALL).group())



