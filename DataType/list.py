#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

#参考文档：http://www.cnblogs.com/alex3714/articles/5717620.html


l1 = ["ma",23,8,"assdf"]
l2 = enumerate(l1)     #将列表的元素以及对应的索引号生成迭代器
                       #此方法适用于较小列表，一旦列表较大，将会消耗内存
print(l2)
for index,value in l2:
	print(index)
	print(value)