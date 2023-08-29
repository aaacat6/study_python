# class Point:
#    def __init__( self, x=0, y=0):
#       self.x = x
#       self.y = y
#    def __del__(self):
#       class_name = self.__class__.__name__
#       print (class_name, "销毁")
 
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print (id(pt1), id(pt2), id(pt3)) # 打印对象的id
# del pt1
# del pt2
# del pt3

 
# class Parent:        # 定义父类
#    parentAttr = 100
#    def __init__(self):
#       print ("调用父类构造函数")
 
#    def parentMethod(self):
#       print ('调用父类方法')
 
#    def setAttr(self, attr):
#       Parent.parentAttr = attr
 
#    def getAttr(self):
#       print ("父类属性 :", Parent.parentAttr)
 
# class Child(Parent): # 定义子类
#    def __init__(self):
#       print ("调用子类构造方法")
 
#    def childMethod(self):
#       print ('调用子类方法')
 
# d = Parent()          
# c = Child()          # 实例化子类
# c.childMethod()      # 调用子类的方法
# c.parentMethod()     # 调用父类方法
# c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
# c.getAttr()          # 再次调用父类的方法 - 获取属性值

# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b
 
#    def __str__(self):
#       return 'Vector (%d, %d)' % (self.a, self.b)
   
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)
 
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print (v1 + v2)

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
 
counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
print (counter.__secretCount)  # 报错，实例不能访问私有变量