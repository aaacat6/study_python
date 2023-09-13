# # # import calendar
# # # import time

# # # a = calendar.calendar(2023,w=2,l=1,c=6)

# # # print (a)

# # import calendar

# # # 打印2023年的完整日历
# # # print(calendar.calendar(2023))

# # # 获取2023年9月的月份日历
# # # print(calendar.month(2023, 9))

# # # 获取2023年9月的月份日历数据
# # # print(calendar.monthcalendar(2023, 9))

# # # 打印一周的星期头
# # print(calendar.weekheader(2))


# # 导入 requests 包
# import requests

# # 发送请求
# x = requests.get('https://www.runoob.com/')

# # 返回网页内容
# print(x.text)

import requests

response = requests.get('https://www.runoob.com/python3/python-requests.html')
print(response.text)