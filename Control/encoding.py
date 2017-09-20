#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:Anony

#参考文档：http://www.cnblogs.com/luotianshuai/articles/5735051.html

'''
理解字符编码：可以将字符编码理解为一张excel表格
     字符集：存放的是人类可以识别的内容【终端打印的字符】
     字符编码：存放的是机器可以识别的内容【字符集在硬盘中或内存中表现形式】
GBK：GBK字符集【汉字集合】、GB2312/GBK/GB18030【一个汉字使用2字节存放】
     GB2312：支持7000多汉字
     GBK/GB18030：支持所有汉字
ASCII：ASCII字符集【英文字母集合】、ASCII字符编码【一个字母使用1字节存放】
Unicode：Unicode字符集【世界所有文字集合】、utf-8【一个字母1字节；一个汉字3字节】/UCS-16/UCS-32
     utf-8:用来网络传输，文件存放
     ucs-16/ucs-32：用来作为内存中的存放方式，以利于快速统一计算

小结：
    （1）字符集只有encode操作；字符编码只有decode操作。它们的默认编码解码方式是python默认的字符编码
    （2）python中的字符集默认都是Unicode字符集
    （3）python的# -*-coding :uft-8 -*-声明是指对该文件内容的编码和解码都是utf-8
    （4）encode后打印的是字符在硬盘或内存中的存放形式，机器语言；decode后打印的是字符集中定义的字符形式，也就是自然语言
'''

'''
字符打印的过程：
（1）先获取字符存储时的编码格式
（2）然后使用相应的字符编码格式将存储在硬盘或内存的01组合进行解码转换成对应的字符集
（3）最后调用相应的渲染引擎打印到中断上
'''

'''
字符编码转换:
（1）先使用对应的字符编码将01组合进行解码转换成Unicode字符集
（2）然后使用指定的字符编码将转换的Unicode字符集进行编码处理
python中的字符集默认都是Unicode字符集
'''

#'''
import sys
print(sys.getdefaultencoding())

var = "你好"   #python3中此处是Unicode字符集
               #python2中此处已经将Unicode字符集作为文件内容进行编码。编码方式为 -*-coding :uft-8 -*-声明指定；如果没有声明，就使用python2默认ASCII编码
print(var)
print(var.encode())#使用指定的字符编码对Unicode字符集进行编码，如果没有指定
                   #将会使用python默认字符编码，python3是utf-8;python2是ASCII
print(type(var.encode())) #python3在对字符集编码时会统一将其转换成bytes类型存放在硬盘或内存中
print(var.encode('gbk'))#使用gbk进行编码
print(type(var.encode('gbk')))
print(var.encode('gbk').decode('gbk'))#使用gbk进行解码





#'''