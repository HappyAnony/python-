#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

'''
集合是一个无序的，不重复的数据组合。它的应用场景：
       去重：把一个列表变成集合，自动去重
       关系测试：测试两组数据之前的交集、差集、并集等关系
'''
list1 = [1,3,4,5,6,4,2,1,2,3]
set1 = set(list1)
print(set1,type(set1))

set2 = set([1,4,6,8,9,44])
print(set2.intersection(set1))  #取交集
print(set2 & set1)
print(set2.isdisjoint(set1))    #判断两者是否有交集，没有返回true
print(set2.union(set1))         #取并集
print(set2 | set1)
print(set2.difference(set1))    #取差集：set2中有；set1中没有\
print(set2 - set1)
print(set1 - set2)
print(set2.symmetric_difference(set1))  #取对称差集：合并set2和set1，但去掉两者都有的部分
print(set2 ^ set1)
set3 = set([1,2])
print(set3.issubset(set1))   #set3是否是set1的子集
print(set1.issuperset(set3)) #set1是否是set3的父集

'''
集合的基本操作
'''
set4 = set()
print(set4)
set4.add(45)   #添加一项
print(set4)
set4.update([4,2,6])  #添加多项
print(set4)
set4.remove(4)   #删除一项
print(set4)


'''
成员关系判断
'''
print(4 in set4)
print(4 not in set4)

print(set4.pop())   #随机删除一个元素，并返回该元素

