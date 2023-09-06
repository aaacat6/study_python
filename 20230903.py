# # # # # b = [1,2,3]

# # # # # ss = []

# # # # # # for i in range(4):
# # # # # #    transposed.append([row[i] for row in matrix])

# # # # # ss.append(b)

# # # # # print(ss)

# # # # # a = 1,2,3,4
# # # # # print(a)

# # # # a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# # # # print(a)

# # # for index, value in enumerate(['a', 'b', 'c']):
# # #     print(index, value)

# # list=[1,2,3,4]
# # it = iter(list)
# # for x in it:
# #     print (x, end=" ")

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
 
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
 
# myclass = MyNumbers()
# myiter = iter(myclass)
 
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# # print(next(myiter))
# # print(next(myiter))

import sys
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')