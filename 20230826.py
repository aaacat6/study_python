# dict1 = {"a":[1,2]}      # 值为列表
# print(dict1["a"][1])

# dict2 = {"a":{"c":"d"}}   # 值为字典
# print(dict2["a"]["c"])

# import time  # 引入time模块
 
# ticks = time.time()
# print("当前时间戳为:", ticks)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# import time
 
# localtime = time.asctime( time.localtime(time.time()) )
# print ("本地时间为 :", localtime)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# import time
 
# # 格式化成2016-03-20 11:45:39形式
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
 
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
  
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# # 定义函数
# def printme( str ):
#    "打印任何传入的字符串"
#    print (str)
#    return
 
# # 调用函数
# printme("我要调用用户自定义函数!")
# printme("再次调用同一函数")

# # 定义一个类
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def say_hello(self):
#         print("Hello, my name is", self.name)

# # 创建对象的实例
# person = Person("Alice")

# # 访问对象的属性
# print(person.name)

# # 调用对象的方法
# person.say_hello()

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# def ChangeInt( a ):
#     a = 10
#     return a
 
# b = 2
# ChangeInt(b)
# print (b) # 结果是 2
# print (ChangeInt(b))

# # 可写函数说明
# def changeme( mylist ):
#    "修改传入的列表"
#    mylist.append([1,2,3,4])
# #    print ("函数内取值: ", mylist)
#    return
 
# # 调用changeme函数
# mylist = [10,20,30]
# changeme( mylist )
# print ("函数外取值: ", mylist)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# # 可写函数说明
# total = 3

# def sum( arg1, arg2 ):
#    # 返回2个参数的和."
#    total = arg1 + arg2
#    print ("函数内 : ", total)
# #    return total
 
# # 调用sum函数
# sum( 10, 20 )
# print(total)

# Money = 2000
# def AddMoney():
#    # 想改正代码就取消以下注释:
#    global Money
# #    Money = 1
#    Money = Money + 1
# #    return Money
 
# print (Money)
# AddMoney()
# print (Money)
# print (AddMoney())

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# # 导入内置math模块
# import math
 
# content = dir(math)
 
# print (content)