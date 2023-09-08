# # print("test")

# #!/usr/bin/python3
 
# #类定义
# # class people:
# #     #定义基本属性
# #   #  name = ''
# #   #  age = 0
# #     #定义私有属性,私有属性在类外部无法直接进行访问
# #   #  __weight = 0
# #     #定义构造方法
# #     def __init__(self,n,a):
# #         self.name = n
# #         self.age = a
# #   #      self.__weight = w
# #     def speak(self):
# #         print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# # # 实例化类
# # p = people('runoob',)
# # p.speak()

# # #!/usr/bin/python3
 
# # #类定义
# # class people:
# #     #定义基本属性
# #     name = ''
# #     age = 0
# #     #定义私有属性,私有属性在类外部无法直接进行访问
# #     __weight = 0
# #     #定义构造方法
# #     def __init__(self,n,a,w):
# #         self.name = n
# #         self.age = a
# #         self.__weight = w
# #     def speak(self):
# #         print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# # #单继承示例
# # class student(people):
# #     grade = ''
# #     def __init__(self,n,a,w,g):
# #         #调用父类的构函
# #         people.__init__(self,n,a,w)
# #         self.grade = g
# #     #覆写父类的方法
# #     def speak(self):
# #         print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
# # #另一个类，多继承之前的准备
# # class speaker():
# #     topic = ''
# #     name = ''
# #     def __init__(self,n,t):
# #         self.name = n
# #         self.topic = t
# #     def speak(self):
# #         print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
 
# # #多继承
# # class sample(student,speaker):
# #     a =''
# #     def __init__(self,n,a,w,g,t):
# #         student.__init__(self,n,a,w,g)
# #         speaker.__init__(self,n,t)
 
# # test = sample("Tim",25,80,4,"Python")
# # test.speak()   #方法名同，默认调用的是在括号中参数位置排前父类的方法

# #!/usr/bin/python3
 
# class Parent:        # 定义父类
#    def myMethod(self):
#       print ('调用父类方法')
 
# class Child(Parent): # 定义子类
#    def myMethod(self):
#       print ('调用子类方法')
 
# c = Child()          # 子类实例
# c.myMethod()         # 子类调用重写方法
# super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法

#!/usr/bin/python3
 
# total = 0 # 这是一个全局变量
# # 可写函数说明
# def sum( arg1, arg2 ):
#     #返回2个参数的和."
#     total = arg1 + arg2 # total在这里是局部变量.
#     print ("函数内是局部变量 : ", total)
#     return total
 
# #调用sum函数
# sum( 10, 20 )
# print ("函数外是全局变量 : ", total)
# print (sum(10,20))

#!/usr/bin/python3
 
a = 10
def test():
    global a 
    a = a + 1
    print(a)
test()
print(a)
