#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

'''
初始化字典
'''
#方法一
d1 = {}
print(d1)
#方法二
d2 = dict.fromkeys([4,5,2,6],"anony")   #初始化一个字典d2，它的keys来自列表[4,5,2,6],每个keys的初识value为anony
                                        #注意，该处每个key都是共享引用同一个value，只要一个key修改看value，所有的都会修改
print(d2)


'''
字典的基本操作：
 增
 删
 查
 改
'''
dict1 = {}
dict2 = {"name1":'anony',"name2":'jack',"name3":'marry'}

#增
dict1["name1"] = "happy"
print(dict1)

#改
dict2["name1"] = "tom"
print(dict2)

#删除
del dict2["name2"]
print(dict2)
dict2.pop("name3")
print(dict2)
dict2['age'] = 22
print(dict2)
dict2.popitem()         #随机删除
print(dict2)

#查找
print(dict2.get("name1"))
print(dict2.get("name4"))

'''
成员关系判断
'''
#判断dict2中的key是否存在name1
print('name1' in dict2)   #python2中对应的写法是：print(dict2.has_key('name1'))
print('name1' not in dict2)



'''
字典嵌套
'''

it_video = {
    "USA":{"www.course.com":["很不错","very good"]},
    "china":{"www.baiduchuanke.com":["比较全面","free"]}
}
print(it_video)

print(it_video.setdefault("USA",{"www.ai.com":["ai","li"]}))  #先查询字典中是否存在USA，如果有就返回对应的value
print(it_video.setdefault("ai",{"www.ai.com":["ai","li"]}))   #先查询字典中是否存在ai，如果没有就添加一个key为ai,对应的value为后面指定的值
print(it_video.keys())  #以列表的形式返回字典的keys
print(it_video.values()) #以列表的形式返回字典的values


dict3 = {1:2, 3:4, 4:3, "name":"thon"}
dict4 = {"name1":"hello", "age":22, "name":"anony"}
dict3.update(dict4)                #将字典dict4更新添加至字典dict3中，相同key的值以dict4为准
print(dict3)

print(dict3.items())        #将字典转换成二维元组列表




'''
字典的循环
'''
dict5 = {"name1":'Anony',"name2":'Jack',"name3":'Marry'}

for i in dict5:
    print(i)            #打印key

for j in dict5:
    print(j, dict5[j])  #打印key和value

for k,v in dict5.items():   #该循环比较低效，因为需要将字典转换成列表，一旦数据量大了，就非常占用内存
    print(k,v)