#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony
'''
文件操作的步骤：
   （1）打开文件，得到文件句柄并赋值给一个变量
   （2）通过句柄对文件进行操作
   （3）关闭文件
'''

'''文件句柄操作
f = open("python",'r',encoding="utf-8")
print(f.encoding)                   #打印文件编码
print(f.name)                       #打印文件名
print(f.isatty())                   #判断文件是否是终端设备文件
print(f.readable())                 #判断文件是否读
print(f.writable())                 #判断文件是否可写
print(f.tell())                     #返回句柄指针的位置
print(f.readline())
print(f.tell())                     #句柄指针是以字节为单位
print(f.read(6))                    #接着读取6个字符
print(f.tell())
if f.seekable():                    #判断文件的文件句柄是否可移动，某些终端设备文件是无法移动的
	f.seek(0)                       #句柄指针回到文件首部
print(f.tell())
'''

'''' 只读模式
f = open("python",'r',encoding="utf-8")  #生成文件句柄，它可以理解为文件内容指针，本质是一个文件行迭代器
# open函数会将文件名、字符集、大小、硬盘的起始位置封装成一个类，实例化该类形成的对象就是句柄
# mode:一次只能是一个模式打开文件
#   'a'：追加模式打开，文件可以写，但是不能读，打开文件时，文件指针直接指向文件的最后一个字符
#   'r'：只读模式打开，文件不能写，只能读，默认是该模式
#   'w'：只写模式打开，该模式时创建一个新文件，如果以写模式打开一个已存在的文件，它会将该文件内容全部清空
#   'r+'：以读写模式打开文件，先用读模式打开一个文件，然后可读写，只不过此处的写是追加模式的写。较常用
#   'w+'：以写读模式打开文件，先用写模式创建一个文件，然后可读写，只不过此处的写是追加模式的写。用处不多
#   'rb'：以读模式打开二进制文件，此时不需要指定encoding编码方式，适用于读取socket数据，打开音频视频文件
#   'wb'：以写模式打开二进制文件，可写入二进制信息，此时不需要指定encoding编码方式
#   'ab'：以追加模式打开二进制文件，此时不需要指定encoding编码方式
#   'r+U'：读写模式打开文件，同时可将window上的换行符\r\n自动转换为linux上的换行符\n
print(f.read())   #读取文件所有内容
                  # 此时文件句柄指向文件的最后一个字符
f.close()
'''

'''追加模式打开
f = open("python",'a',encoding="utf-8")
f.write("\nthis is test\n")   #向文件中写入内容
f.write("python学习路线")
f.close()
'''
'''写模式打开
f = open("python1",'w',encoding="utf-8")
f.write("this is test\n")   #向文件中写入内容
f.write("python学习路线")    #向文件写入内容，此时内容是直接存放在内存中，需等待周期时钟到来然后再同步到硬盘中
f.flush()                   #强制将内存中的内容缓存刷新同步到硬盘文件中
f.close()
'''

'''二进制文件
f = open("binary",'wb')
f.write("hello world\n".encode())  #将str类型转换成bytes类型，然后以二进制格式存储该文件；不过显示的不是0，1
f.close()
'''

'''打印文件前n行
f = open("python",'r',encoding="utf-8")
n = 5
for i in range(n):
	print(f.readline().strip())      #每次读取文件一行,每行都有一个换行符，使用strip方法去掉换行符
'''


'''打印文件的第n行到第m行
# 方法一：整个文件缓存到内存中处理；当文件较大时，内存消耗较大，不采取此方法
f = open("python",'r',encoding="utf-8")
lines = f.readlines()    #将整个文件生成一个列表，存放在内存中，每个元素是文件的一行
                         #此方法适用于小文件，一旦文件较大，将会耗费内存
n = 5
m =10
for index,line in enumerate(lines):
	if index >= n-1 and index <= m-1:
		print(line.strip())
	if index == m-1
		break
f.close()


# 方法二：每次缓存文件一行到同一指定位置，新缓存会覆盖旧缓存，实现小内存缓存大文件，建议采取此方法
f = open("python",'r',encoding="utf-8")
count = 1
n = 5
m = 10
for line in f:                          #文件句柄本身就是一个行迭代器，每次迭代读取文件一行
	if count >= n and count <=m:
		print(line.strip())
	count += 1
	if count == 10:
		break
f.close()
'''


'''文件截断
f = open("python1",'a',encoding="utf-8")
f.truncate(6)    #保留从文件首部开始向后的6个字符，清空剩余的字符
'''

'''文件修改
#方法一：原文件修改，此方法是直接对硬盘操作，编辑内容会覆盖原文件内容，不会自动移位
#方法二：内存修改，先将整个文件加载到内存中，然后对其进行编辑修改，最后全部写会原文件中，例如：vim

f = open("python",'r',encoding="utf-8")
f_new = open("python_new",'w',encoding="utf-8")
for line in f:
	if "this is test" in line:
		line = line.replace("test","TEST")
	f_new.write(line)
f.close()
f_new.close()


'''

'''
为了避免打开文件后忘记关闭，可以通过管理上下文，即：
    with open("file",'r',encoding="utf-8") as f:
         ...
当with代码块执行完后，内部会自动关闭并释放文件资源；
同时支持对多个文件进行上下文管理
'''

'''
with open("python",'r',encoding="utf-8") as f, \       #\表示换行
	 open("python_new",'w',encoding="utf-8") as f_new:
	for line in f:
		if "this is test" in line:
			line = line.replace(" is test", " IS TEST")
		f_new.write(line)
'''

with open("python",'r',encoding="utf-8") as f:
	for line in f:
		if "this is test" in line:
			print(f.readline())





