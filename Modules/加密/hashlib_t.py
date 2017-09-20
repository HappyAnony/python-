#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 参考文档：http://www.cnblogs.com/alex3714/articles/5161349.html
# 用于加密相关的操作，3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
# 此处是单向加密，不可逆
'''
所有的update方法接收的text都只能是bytes
(1)要么使用b明确定义bytes类型，此时不支持中文，因为b只支持ASCII码
(2)要么使用字串的encode方法将其编码，因为编码的本质就是转换成了bytes类型进行存储
'''


import hashlib

m = hashlib.md5()  # 生成一个md5对象
m.update(b"Hello")
print(m.hexdigest()) # 生成Hello的16机制格式hash
m.update(b"It's me")
print(m.hexdigest())  # 生成HelloIt's me的16进制hash
m.update(b"It's been a long time since last time we ...")
print(m.digest())  # 2进制格式hash
print(len(m.hexdigest()))  # 16进制格式hash
'''
def digest(self, *args, **kwargs): # real signature unknown
    """ Return the digest value as a string of binary data. """
    pass

def hexdigest(self, *args, **kwargs): # real signature unknown
    """ Return the digest value as a string of hexadecimal digits. """
    pass

'''


'''
import hashlib

# ######## md5 ########

hash = hashlib.md5()
hash.update('admin')
print(hash.hexdigest())

# ######## sha1 ########

hash = hashlib.sha1()
hash.update('admin')
print(hash.hexdigest())

# ######## sha256 ########

hash = hashlib.sha256()
hash.update('admin')
print(hash.hexdigest())

# ######## sha384 ########

hash = hashlib.sha384()
hash.update('admin')
print(hash.hexdigest())

# ######## sha512 ########

hash = hashlib.sha512()
hash.update('admin')
print(hash.hexdigest())

'''