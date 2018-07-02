#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：时间函数举例1。

# if __name__ == '__main__':
#     import time
#     print time.ctime(time.time())
#     print time.asctime(time.localtime(time.time()))
#     print time.asctime(time.gmtime(time.time()))

# 题目：时间函数举例2。
# if __name__ == '__main__':
#     import time
#
#     start = time.time()
#     for i in range(30000):
#         print i
#     end = time.time()
#     print start, end
#     print end - start

# 题目：时间函数举例3。
# if __name__ == '__main__':
#     import time
#     start = time.clock()
#     for i in range(10000):
#         print i
#     end = time.clock()
#     print(start, end)
#     print 'different is %6.3f' % (end - start)

# 题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。
#
# if __name__ == '__main__':
#     import time
#     import random
#
#     play_it = raw_input('do you want to play it.(\'y\' or \'n\')')
#     while play_it == 'y':
#         c = raw_input('input a character:\n')
#         i = random.randint(0, 2 ** 32) % 100
#         print('The number range is 0 ~ %d' % 2 ** 32)
#         print 'please input number you guess:\n'
#         start = time.clock()
#         a = time.time()
#         guess = int(raw_input('input your guess:\n'))
#         while guess != i:
#             if guess > i:
#                 print 'please input a little smaller'
#                 guess = int(raw_input('input your guess:\n'))
#             else:
#                 print 'please input a little bigger'
#                 guess = int(raw_input('input your guess:\n'))
#         end = time.clock()
#         b = time.time()
#         var = (end - start) / 18.2
#         print var
#         # print 'It took you %6.3 seconds' % time.difftime(b,a))
#         if var < 15:
#             print 'you are very clever!'
#         elif var < 25:
#             print 'you are normal!'
#         else:
#             print 'you are stupid!'
#         print 'Congradulations'
#         print 'The number you guess is %d' % i
#         play_it = raw_input('do you want to play it.')

# 题目：字符串日期转换为易读的日期格式。
# from dateutil import parser
# dt = parser.parse("Aug 28 2018 12:00AM")
# print dt
#

# 计算字符串中子串出现的次数
# if __name__ == '__main__':
#     str1 = raw_input('请输入一个字符串:\n')
#     str2 = raw_input('请输入一个子字符串:\n')
#     ncount = str1.count(str2)
#     print ncount

# 题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
# if __name__ == '__main__':
#     from sys import stdout
#     filename = raw_input('输入文件名:\n')
#     fp = open(filename,"w")
#     ch = raw_input('输入字符串:\n')
#     while ch != '#':
#         fp.write(ch)
#         stdout.write(ch)
#         ch = raw_input('')
#     fp.close()

# 题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。

# if __name__ == '__main__':
#     string = raw_input('please input a string:\n')
#     string = string.upper()
#     fp = open('test.txt', 'w')
#     fp.write(string)
#     fp = open('test.txt','r')
#     print fp.read()
#     fp.close()
#
# if __name__ == '__main__':
#     import string
#
#     fp = open('test1.txt')
#     a = fp.read()
#     fp.close()
#
#     fp = open('test2.txt')
#     b = fp.read()
#     fp.close()
#
#     fp = open('test3.txt', 'w')
#     l = list(a + b)
#     l.sort()
#     s = ''
#     s = s.join(l)
#     fp.write(s)
#     fp.close()

# 题目：列表转换为字典。

i = ['a', 'b']
l = [1, 2]
print dict([i, l])



