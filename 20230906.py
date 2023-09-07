# # # # # # # # # # # # # for x in range(1, 4):
# # # # # # # # # # # # #      print(repr(x).rjust(2), repr(x**2).rjust(3), end=' ')
# # # # # # # # # # # # #      # 注意前一行 'end' 的使用
# # # # # # # # # # # # #      print(repr(x**3).rjust(4))

# # # # # # # # # # # # class Person:
# # # # # # # # # # # #     def __init__(self, name, age):
# # # # # # # # # # # #         self.name = name
# # # # # # # # # # # #         self.age = age

# # # # # # # # # # # #     def aaa(self):
# # # # # # # # # # # #         return f"Person('{self.name}', {self.age})"

# # # # # # # # # # # # alice = Person("Alice", 30)
# # # # # # # # # # # # print(alice.aaa()) 

# # # # # # # # # # # table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# # # # # # # # # # # for name, number in table.items():
# # # # # # # # # # #      print('{0:>10} ==> {1:<10d}'.format(name, number))

# # # # # # # # # # table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# # # # # # # # # # print('Runoob: {0[Runoob]:d} Google: {0[Google]:d} Taobao: {0[Taobao]:d}'.format(table))

# # # # # # # # # def greet(name, age):
# # # # # # # # #     print(f"Hello, {name}. You are {age} years old.")

# # # # # # # # # person_info = {"name": "Alice", "age": 25}

# # # # # # # # # greet(**person_info)
# # # # # # # # # # 输出: Hello, Alice. You are 25 years old.

# # # # # # # # import math
# # # # # # # # print('常量 PI 的值近似为：%5.3f。' % math.pi)

# # # # # # # str = input("请输入：")
# # # # # # # print ("你输入的内容是: ", str)

# # # # # # # selfref_list = [1, 2, 3]
# # # # # # # selfref_list.append(str(selfref_list))
# # # # # # # print(selfref_list)

# # # # # # import pprint

# # # # # # data = {
# # # # # #     "name": "Alice",
# # # # # #     "age": 25,
# # # # # #     "attributes": {
# # # # # #         "intelligence": 8,
# # # # # #         "strength": 7,
# # # # # #         "dexterity": 6,
# # # # # #         "wisdom": 9
# # # # # #     },
# # # # # #     "items": ["sword", "shield", "potion", "map"],
# # # # # #     "skills": [
# # # # # #         {"name": "attack", "level": 3},
# # # # # #         {"name": "defense", "level": 4}
# # # # # #     ]
# # # # # # }

# # # # # # # 使用普通的print函数
# # # # # # print("Using print:")
# # # # # # print(data)

# # # # # # # 使用pprint.pprint函数
# # # # # # print("\nUsing pprint.pprint:")
# # # # # # pprint.pprint(data)


# # # # # import pickle

# # # # # # 使用pickle模块将数据对象保存到文件
# # # # # data1 = {'a': [1, 2.0, 3, 4+6j],
# # # # #          'b': ('string', u'Unicode string'),
# # # # #          'c': None}

# # # # # selfref_list = [1, 2, 3]
# # # # # selfref_list.append(selfref_list)

# # # # # output = open('data.pkl', 'wb')

# # # # # # Pickle dictionary using protocol 0.
# # # # # pickle.dump(data1, output)

# # # # # # Pickle the list using the highest protocol available.
# # # # # pickle.dump(selfref_list, output, -1)

# # # # # output.close()


# # # # # import pprint, pickle

# # # # # #使用pickle模块从文件中重构python对象
# # # # # pkl_file = open('data.pkl', 'rb')

# # # # # data1 = pickle.load(pkl_file)
# # # # # pprint.pprint(data1)

# # # # # data2 = pickle.load(pkl_file)
# # # # # pprint.pprint(data2)

# # # # # pkl_file.close()

# # # # try:
# # # #     # 一段可能会引发异常的代码
# # # #     x = 1 / 0
# # # # except ZeroDivisionError as e:
# # # #     # 重新抛出当前异常
# # # #     raise

# # # try:
# # #    assert 0 > 1
# # # except AssertionError :
# # #     print("test")
# # # # else:
# # # #     try:
# # # #         with open('file.log') as file:
# # # #             read_data = file.read()
# # # #     except FileNotFoundError as fnf_error:
# # # #         print("test")
# # # # finally:
# # # #     print('这句话，无论异常是否发生都会执行。')

# # x = 10
# # if x > 5:
# #     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

# try:
#         raise NameError('HiThere')  # 模拟一个异常。
# except NameError:
#         print('An exception flew by!')
#         raise

class MyCustomException(Exception):
    def custom_method(self):
        print("This is a custom method in a custom exception class")

try:
    raise MyCustomException()
except MyCustomException as e:
    e.custom_method()       # 输出: This is a custom method in a custom exception class

