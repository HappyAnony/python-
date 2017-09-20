#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 方法一
name1 = "anony"
age1 = 23
print("my name is", name1)

# 方法二
print("my name is %s;age is %s" %(name1, age1))

# 方法三
print("my name is {_name};age is {_age}".format(_name="anony",_age=23))
print("my name is {_name1};age is {_age1}".format_map({"_name1":"anony","_age1":23}))


# 方法四
name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")

info = '''
-------------- info of {_name} ---------
Name:\033[31;1m{_name}\033[0m             #着色输出
Age: \033[32;1m{_age}\033[0m
Job: \033[36;1m{_job}\033[0m
Salary:\033[46;1m{_salary}\033[0m
------------------ end ------------
''' .format(_name=name,
            _age=age,
            _job = job,
            _salary=salary )

print(info)


