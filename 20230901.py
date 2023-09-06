# # # # # # # 解构赋值时，只关心第一个值
# # # # # # a, _ = (1, 2)

# # # # # # # 在循环中，只关心循环次数
# # # # # # for _ in range(5):
# # # # # #     print("Hello!")

# # # # # print(round(10.5))
# # # # # print(round(11.5))

# # # # #!/usr/bin/python3
 
# # # # # var1 = '  a    World!'
 
# # # # # print ("已更新字符串 : ", var1[:6] + 'Runoob!')

# # # # print("\a")

# # # import time

# # # for i in range(101):
# # #     print("\r{:3}%".format(i),end=' ')
# # #     time.sleep(0.05)

# # x = 1
# # print(f'x+1={x+1}')

# #!/usr/bin/python3
 
# # tup = ('Google', 'Runoob', 1997, 2000)
 
# # print (tup)
# # del tup
# # print ("删除后的元组 tup : ")
# # tup=1
# # print (tup)

# # basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# # print(basket)                      # 这里演示的是去重功能
# # 'orange' in basket                 # 快速判断元素是否在集合内

# thisset = set(("Google", "Runoob", "Taobao"))
# thisset.update({"facebook"})
# print(thisset)

# thisset.update("jingdong")
# print(thisset)

# a = 1

# while a < 10:
#  if (a%2 == 0):
#    print(a, "is even")
#  else:
#    print(a, "is odd")
#  a += 1

# #!/usr/bin/python3
 
# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age -2)*5
#     print("对应人类年龄: ", human)
 
# ### 退出提示
# input("点击 enter 键退出")

# number = 7
# guess = None
# print("数字猜谜游戏!")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
 
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")

# num = int(input("请输入一个数字"))
# if num%2 == 0:
#     if num%3 == 0:
#         print("能被2整除,也能被3整除")
#     else:
#         print("能被2整除,不能被3整除")
# else:
#     if num%3 == 0:
#         print("能被3整除,不能被2整除")
#     else:
#         print("不能被2和3整除")

# x = 2

# match x:
#     case 1:
#         print("x is one")
#     case 2:
#         print("x is two")
#     case _:
#         print("x is neither one nor two")

# point = (2, 3)

# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"On Y axis with y-coordinate {y}")
#     case (x, 0):
#         print(f"On X axis with x-coordinate {x}")
#     case (x, y):
#         print(f"Point is at ({x}, {y})")
#     case _:
#         print("Not a point")

# n = 3
 
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
 
# print("1 到 %d 之和为: %d" % (n,sum))

# n = int(input("求和最大值"))
# m = int(input("求和最小值"))
# sum = (n-m+1)/2 * (n + m)
# print(f"{m}到{n}之间相加的和是:{sum}")

# word = 'runoob'
 
# for a in word:
#     print(a)

# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     print("循环数据 " + site)
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
# else:
#     print("没有循环数据!")
# print("完成循环!")

# while True:
#     number = int(input("请输入一个数字: "))
#     if number == 5:
#         print("你输入了5，循环将结束。")
#         break
#     else:
#         print("你输入了", number, "。请再试一次！")

# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n)
# print('循环结束。')

site = ["a","b","c"]

while len(site) > 1:
    site.pop()

if len(site) == 1:
    print("over")


       