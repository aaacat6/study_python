# # # # if True:
# # # #     print ("Answer")
# # # #     print ("True")
# # # # else:
# # # #     print ("Answer")
# # # #    print ("False")    # 缩进不一致，会导致运行错误

# # # #!/usr/bin/python3
 
# # # str='123456789'
 
# # # print(str)                 # 输出字符串
# # # print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
# # # print(str[0])              # 输出字符串第一个字符
# # # print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
# # # print(str[2:])             # 输出从第三个开始后的所有字符
# # # print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
# # # print(str * 2)             # 输出字符串两次
# # # print(str + '你好')         # 连接字符串
 
# # # print('------------------------------')
 
# # # print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# # # print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


# # # #!/usr/bin/python3
 
# # # input("\n\n按下 enter 键后退出。")

# # #!/usr/bin/python3
 
# import sys; 
# # x = 'runoob'; sys.stdout.write(x + '\n')

# sys.stdout.write('test\n')
# print('test')

# import sys
# print('================Python import mode==========================')
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)

# from sys import argv,path  #  导入特定的成员
 
# print('================python from import===================================')
# print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

# 1 is True

# def reverseWords(input): 
      
#     # 通过空格将字符串分隔符，把各个单词分隔为列表
#     inputWords = input.split(" ") 
#     inputWords = inputWords[-1::-1] 
  
#     # 重新组合字符串
#     output = ' '.join(inputWords) 
      
#     return output 
  
# if __name__ == "__main__": 
#     input = 'I like runoob'
#     rw = reverseWords(input) 
#     print(rw)

# num_int = 123
# num_flo = 1.23

# num_new = num_int + num_flo

# print("num_int 数据类型为:",type(num_int))
# print("num_flo 数据类型为:",type(num_flo))

# print("num_new 值为:",num_new)
# print("num_new 数据类型为:",type(num_new))

# num_int = 123
# num_str = "456"

# print("num_int 数据类型为:",type(num_int))
# print("类型转换前,num_str 数据类型为:",type(num_str))

# num_str = int(num_str)    # 强制转换为整型
# print("类型转换后,num_str 数据类型为:",type(num_str))

# num_sum = num_int + num_str

# print("num_int 与 num_str 相加结果为:",num_sum)
# print("sum 数据类型为:",type(num_sum))

a = '20 hello world hello world hello world'

if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
