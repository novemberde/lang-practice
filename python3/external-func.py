import sys
print(sys.argv) # python3 external-func.py a b c
# ['external-func.py', 'a', 'b', 'c']

print(sys.path)

# You can add path using sys.path.append
 
# sys.exit()



import pickle

# save as object
f = open("test.txt", "wb")
data = {1: "python", 2: "you need"}
pickle.dump(data, f)
f.close()

# get object
f = open("test.txt", "rb")
data = pickle.load(f)
print(data)
f.close()   # {1: 'python', 2: 'you need'}




import os
# print(os.environ)
# print(os.environ["PATH"])
"""
os.chdir("../")
print(os.getcwd())

print(os.system("ls"))
os.mkdir("Directory name")  # make dir
os.rmdir("Directory name")  # remove dir. only empty directory
os.unlink("filename")   # remove file
os.rename(src,"filename")   # rename file
"""



import shutil
shutil.copy("test.txt", "text_copy.txt")


import glob
print(glob.glob("./*")) # print all file in this directory


import tempfile
filename = tempfile.mktemp()
print(filename) # /tmp/tmpbecg5zqs
# os.unlink(filename)

import time

print(time.time())  # 1503214710.753079
print(time.localtime(time.time()))  # time.struct_time(tm_year=2017, tm_mon=8, tm_mday=20, tm_hour=8, tm_min=4, tm_sec=54, tm_wday=6, tm_yday=232, tm_isdst=0)
print(time.ctime()) # Sun Aug 20 08:04:16 2017
"""
time.strftime("%x", time.localtime(time.time()))
%a	Locale’s abbreviated weekday name.	 
%A	Locale’s full weekday name.	 
%b	Locale’s abbreviated month name.	 
%B	Locale’s full month name.	 
%c	Locale’s appropriate date and time representation.	 
%d	Day of the month as a decimal number [01,31].	 
%H	Hour (24-hour clock) as a decimal number [00,23].	 
%I	Hour (12-hour clock) as a decimal number [01,12].	 
%j	Day of the year as a decimal number [001,366].	 
%m	Month as a decimal number [01,12].	 
%M	Minute as a decimal number [00,59].	 
%p	Locale’s equivalent of either AM or PM.	(1)
%S	Second as a decimal number [00,61].	(2)
%U	Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.	(3)
%w	Weekday as a decimal number [0(Sunday),6].	 
%W	Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.	(3)
%x	Locale’s appropriate date representation.	 
%X	Locale’s appropriate time representation.	 
%y	Year without century as a decimal number [00,99].	 
%Y	Year with century as a decimal number.	 
%Z	Time zone name (no characters if no time zone exists).	 
%%	A literal '%' character.	 
Notes:
"""
# for i in range(10):
#     print(i)
#     time.sleep(1)   # this is executed by 1 second.


import calendar
print(calendar.calendar(2015))
#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#           1  2  3  4                         1          1  2  3  4  5  6
#  5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13
# 12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20
# 19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27
# 26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31
#                           30

print(calendar.prmonth(2015,12))
#   December 2015
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
#  None

print(calendar.weekday(2017, 10, 1))
# 6     this means sunday





import random
print(random.random())  # 0.5735225127879594
print(random.randint(1, 10))    # print int value between 1 and 10
shuffleList = [1,2,3,4,5]
random.shuffle(shuffleList)
print(shuffleList)  # [2, 1, 3, 5, 4]

# import webbrowser
# webbrowser.open("https://google.com")


# import threading
# import time

# def hi():
#     while True:
#         time.sleep(1)
#         print("hi")

# for i in range(3):
#     t = threading.Thread(target=hi, args=())    
#     t.deamon = True
#     t.start()


