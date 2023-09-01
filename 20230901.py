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

number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))
 
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")
