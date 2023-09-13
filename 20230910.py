# # import random

# # x = [1, 2, 3]

# # random.shuffle(x) 

# # print (x)

# # class MyNumbers:
# #   def __iter__(self):
# #     self.a = 1
# #     return self
 
# #   def __next__(self):
# #     x = self.a
# #     self.a += 1
# #     return x
 
# # myclass = MyNumbers()
# # myiter = iter(myclass)
 
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))

# class MyNumbers:

#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# for i in myiter:
#     if i > 5:
#         break
#     print(i)

# import hashlib
# hash_object = hashlib.md5(b'Hello World')
# print(hash_object.hexdigest())


# import requests
# response = requests.get('https://www.python.org')
# print(response.status_code)

# import binascii
# hex_data = binascii.hexlify(b'hello world')
# print(hex_data)

import binascii

# 定义一个字节字符串
binary_data = b'hello world'

# 使用binascii.hexlify()将二进制数据转换为其十六进制表示
hex_representation = binascii.hexlify(binary_data)

# 输出结果，它将显示十六进制字符串
print(hex_representation)
# 输出: b'68656c6c6f20776f726c64'
