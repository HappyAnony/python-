#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony


#****************************************** 动态导入装载模块 ****************************************************

# 所谓动态装载模块就是通过输入字符串进行模块的导入




# 方法一：这是python解释器自己内部使用的
# modu = __import__('lib.test')
# print(modu)                   # modu是lib的内存对象，通过__init__.py生成
# obj = modu.test.Test()        # 实例化lib包下的test模块中的Test类
# print(obj.name)


# 方法二：与上面效果一样，官方建议用这个
import importlib
modu = importlib.import_module('lib.test')
print(modu)                     # modu是lib.test的内存对象
obj = modu.Test()
print(obj.name)
