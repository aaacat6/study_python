# # # # # # # # for x in range(2, 9):
# # # # # # # #     if 9 % x == 0:
# # # # # # # #         print(9, '等于', x, '*', 9//x)
# # # # # # # #         break
# # # # # # # # else:
# # # # # # # #     # 循环中没有找到元素
# # # # # # # #     print(9, ' 是质数')


# # # # # # # for n in range(2, 10):
# # # # # # #     for x in range(2, n):
# # # # # # #         if n % x == 0:
# # # # # # #             print(n, '等于', x, '*', n//x)
# # # # # # #             break
# # # # # # #     else:
# # # # # # #         # 循环中没有找到元素
# # # # # # #         print(n, ' 是质数')

# # # # # # dic = {x: x**2 for x in (2, 4, 6) if x == 4}
# # # # # # print(dic)
# # # # # # type(dic)

# # # # # # a = (x for x in range(1,10))
# # # # # # print(a)
# # # # # # print(tuple(a))
# # # # # # b = [x for x in range(1,10)]
# # # # # # print(b)

# # # # # list=[1,2,3,4]
# # # # # it = iter(list)    # 创建迭代器对象
# # # # # for x in it:
# # # # #     print (x, end=" ")
# # # # # # print (next(it))

# # # # #!/usr/bin/python3
 
# # # # import sys
 
# # # # def fibonacci(n): # 生成器函数 - 斐波那契
# # # #     a, b, counter = 0, 1, 0
# # # #     while True:
# # # #         if (counter > n): 
# # # #             return
# # # #         yield a
# # # #         a, b = b, a + b
# # # #         counter += 1
# # # # f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
# # # # while True:
# # # #     try:
# # # #         print (next(f), end=" ")
# # # #     except StopIteration:
# # # #         sys.exit()

# # # def func():
# # #     i = 0
# # #     while i < 5:
# # #         if i == 2:
# # #             return i
# # #         print(i)
# # #         i += 1

# # # print(func())

# # #!/usr/bin/python3
 
# # # 可写函数说明
# # def changeme( mylist,a ):
# #    "修改传入的列表"
# #    mylist.append([1,2,3,4])
# #    a = 2
# #    print ("函数内取值: ", mylist,a,id(a))
# #    return
 
# # # 调用changeme函数
# # mylist = [10,20,30]
# # test = 1
# # print ("函数外取值1: ", mylist,test,id(test))
# # changeme( mylist,test )
# # print ("函数外取值2: ", mylist,test,id(test))

# def change_list(lst):
#     lst.append(4)
    
# def change_number(num):
#     num = num + 1
#     print(num)

# a = [1, 2, 3]
# b = 3

# change_list(a)
# change_number(b)

# print(a)  # 输出: [1, 2, 3, 4]
# print(b)  # 输出: 3

def myfunc(n):
  return lambda a : a * n

print(myfunc(2)(3))
