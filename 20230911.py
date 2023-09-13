# # # # # import re

# # # # # pattern = r"\d+"

# # # # # # re.search() - 找到第一个匹配项，不管它在字符串的什么位置
# # # # # string1 = "There are 123 cats and 456 dogs."
# # # # # match1 = re.search(pattern, string1)
# # # # # if match1:
# # # # #     print(f"First match using re.search: {match1.group()}")  # 输出: First match using re.search: 123

# # # # # # re.match() - 只在字符串的开始处查找匹配项
# # # # # string2 = "123 cats and 456 dogs."
# # # # # match2 = re.match(pattern, string2)
# # # # # if match2:
# # # # #     print(f"Match at the start using re.match: {match2.group()}")  # 输出: Match at the start using re.match: 123


# # # # import re
 
# # # # it = re.findall(r"\d+","12a32bc43jf3") 
# # # # for match in it: 
# # # #     print (match.group() )

# # # import re

# # # pattern = r"Hello"
# # # string = "Hello, world!"

# # # match = re.match(pattern, string)
# # # if match:
# # #     print("Pattern matched")
# # # else:
# # #     print("Pattern not matched")

# # import re

# # pattern_start = r"^Hello"
# # pattern_end = r"world!"
# # string = "Hello, world!"

# # # 检查字符串是否以“Hello”开始
# # if re.match(pattern_start, string):
# #     print("The string starts with 'Hello'")
# # else:
# #     print("The string does not start with 'Hello'")

# # # 检查字符串是否以“world!”结束
# # if re.search(pattern_end, string):
# #     print("The string ends with 'world!'")
# # else:
# #     print("The string does not end with 'world!'")


# pattern = r"\w(?=d)"  # 匹配一个单词字符，但只有当它后面是'd'时才匹配

# print(re.findall(pattern, "abd"))   # ['b']
# print(re.findall(pattern, "acd"))   # ['c']
# print(re.findall(pattern, "ade"))   # [‘a']

import re

# 先编译正则表达式
pattern = r"\d+"  # 这将匹配一个或多个数字

# # 使用编译后的正则表达式对象来找到所有匹配项
# result = pattern.findall("12 apples, 13 bananas, 15 cherries")
# print(result)  # 输出: ['12', '13', '15']

# # 使用编译后的正则表达式对象来找到第一个匹配项
# result = pattern.search("12 apples, 13 bananas, 15 cherries")
# print(result.group())  # 输出: '12'

result = re.findall(pattern,"12 apples, 13 bananas, 15 cherries")
print(result)  # 输出: ['12', '13', '15']