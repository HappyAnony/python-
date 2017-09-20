#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

str = "my name is \t{name};age is \t{age}!"
print(str.capitalize())            #首字母大写
print(str.count("a"))              #字符a出现的字数
print(str.center(50,"-"))          #打印50个字符，str放中间，不足使用字符-补齐
print(str.endswith("!"))           #判断字符串是否以！结尾
print(str.expandtabs(tabsize=8))   #\t制表符为8个空格
print(str[str.find("name"):])      #返回name在字符串中首次出现的索引
print(str.format(name="anony", age=23))  #格式化输出
print(str.format_map( {'name':'anony','age':23} ))  #格式化输出

print('ab32da'.isalnum())    #是否是字母+数字
print('asdaf23'.isalpha())   #是否是字母
print('1A'.isdecimal())      #是否是16进制
print('123'.isdigit())       #是否是数字
print('we'.isidentifier())   #是否是合法标识符
print('My name'.istitle())   #每个单词的开头是不是大写
print('asdfaw'.isprintable()) #是否可打印。字符串肯定是可以打印的。只有tty终端文件，drive设备文件不可打印
print(','.join( ['1','2','3','4'] )) #用，将列表中的字符元素拼接起来
print('SDGsd'.lower())         #将大写改成小写
print('SDGsd'.upper())         #将小写改成大写
print(' \nsdfg\n '.strip())       #去掉前后的空格或回车字符
print(' \nsdfg\n '.lstrip())       #去掉左边的空格或回车字符
print(' \nsdfg\n '.rstrip())       #去掉右边的空格或回车字符

p = str.maketrans('abcde','12345')   #a=1;b=2;c=3;d=4;e=5
print("my name".translate(p))        #变量替换

print('anony'.replace('n','N',2))    #将2个n都替换成N
print('anony'.rfind('n'))            #返回字符n索引的最大值

print('my name is'.split())       #以空格为分隔符，生成列表
print('1+2+3'.split('+'))         #以+为分隔符，生成列表
print('1+2\n3+4'.splitlines())    #以换行符为分隔符，生成列表；自动识别不同操作系统的换行符

print('My Name'.swapcase())      #大写变小写；小写变大写










