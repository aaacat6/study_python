# str = input("请输入：")
# print ("你输入的内容是: ", str)

# try:
#     fh = open("testfile", "w")
#     fh.write("这是一个测试文件，用于测试异常!!")
# except IOError:
#     print ("Error: 没有找到文件或读取文件失败")
# else:
#     print ("内容写入文件成功")
#     fh.close()

# import os

# # 获取当前工作目录
# current_dir = os.getcwd()
# print("当前工作目录:", current_dir)

# # 创建文件 "testfile"
# fh = open("testfile", "w")
# fh.close()

# # 输出文件路径
# file_path = os.path.join(current_dir, "testfile")
# print("文件路径:", file_path)


# try:
#     fh = open("testfile", "w")
#     fh.write("这是一个测试文件，用于测试异常!!")
# except IOError:
#     print ("Error: 没有找到文件或读取文件失败")
# else:
#     print ("内容写入文件成功")
#     fh.close()

 
class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
      print ("Total Employee %d" % Employee.empCount)
 
   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


employee1 = Employee("aaa",100)
employee2 = Employee("bbb",200)

employee1.displayEmployee()
employee2.displayEmployee()

print (f"Total Employee:{Employee.empCount}")