#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
#
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....

# r1 = 1
# r2 = 1
# for i in range(1,22):
#     print '%12ld %12ld' % (r1,r2),
#     if (i % 3) == 0:
#         print ''
#     r1 = r1 + r2
#     r2 = r1 + r2


# # sqrt() 方法返回数字x的平方根。
# import math
# print "math.sqrt(100) : ", math.sqrt(100)
# print "math.sqrt(7) : ", math.sqrt(7)
# print "math.sqrt(2) : ", math.sqrt(2)
# print "math.sqrt(3) : ", math.sqrt(3)
# print "math.sqrt(math.pi) : ", math.sqrt(math.pi)

# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　　
#
# count = 0
# leap = 1
# from math import sqrt
# for m in range(101,201):
#     k = int(sqrt(m + 1))
#     for i in range(2,k + 1):
#         if m % i == 0:
#             leap = 0
#             break
#     if leap == 1:
#         print '%-4d' % m
#         count += 1
#         # if count % 10 == 0:
#         #     print ''
#
#     leap = 1
# print 'The total is %d' % count

# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
#
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。

# for i in range(100,1000):
#     a = i / 100
#     b = i / 10 % 10
#     c = i % 10
#     if i == a **3 + b**3 + c**3 :
#         print i


# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
#
# 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

# def reduceNum(n):
#     print '{} = '.format(n),
#     if not isinstance(n, int) or n <= 0 :
#         print '请输入一个正确的数字 !'
#         exit(0)
#     elif n in [1] :
#         print '{}'.format(n)
#     while n not in [1] : # 循环保证递归
#         for index in xrange(2, n + 1) :
#             if n % index == 0:
#                 n /= index # n 等于 n/index
#                 if n == 1:
#                     print index
#                 else : # index 一定是素数
#                     print '{} *'.format(index),
#                 break
# reduceNum(90)
# reduceNum(100)
# reduceNum(1)
# reduceNum(2)
# reduceNum(3)
# reduceNum(4)

# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# 程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
#
# score = int(raw_input('请输入分数：'))
# if score >= 90:
#     re = 'A'
# elif score >= 60:
#     re = 'B'
# else:
#     re = 'C'
#
# print 'your result %d 属于 %s' % (score, re)

# 题目：输出指定格式的日期。
#
# 程序分析：使用 datetime 模块。
# import datetime
#
# if __name__ == '__main__':
#     # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
#     print(datetime.date.today().strftime('%d/%m/%Y'))
#
#     # 创建日期对象
#     myBirthDate = datetime.date(1999, 2, 22)
#
#     print(myBirthDate.strftime('%d/%m/%Y'))
#
#     # 日期算术运算
#     myBirthNextDay = myBirthDate + datetime.timedelta(days=1)
#
#     print(myBirthNextDay.strftime('%d/%m/%Y'))
#
#     # 日期替换
#     myFirstBirthday = myBirthDate.replace(year=myBirthDate.year + 1)
#
#     print(myFirstBirthday.strftime('%d/%m/%Y'))
#
#     print(datetime.date.today())


# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#
# 程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
# import string
# s = raw_input('Please input string:')
# c_letter, c_space, c_digit, c_others, i  = 0 ,0,0,0,0
# while i < len(s):
#     c = s[i]
#     i += 1
#     if c.isalpha():
#         c_letter += 1
#     elif c.isdigit():
#         c_digit += 1
#     elif c.isspace():
#         c_space += 1
#     else:
#         c_others += 1
#
# for c in s:
#     if c.isalpha():
#         c_letter += 1
#     elif c.isdigit():
#         c_digit += 1
#     elif c.isspace():
#         c_space += 1
#     else:
#         c_others += 1
#
# print 'char = %d,space = %d,digit = %d,others = %d' % (c_letter,c_space,c_digit,c_others)

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 程序分析：关键是计算出每一项的值。
# Tn = 0
# Sn = []
# n = int(raw_input('n = '))
# a = int(raw_input('a = '))
# for count in range(n):
#     Tn = Tn + a
#     a = a * 10
#     Sn.append(Tn)
#     print Tn
#
# Sn = reduce(lambda x, y: x + y, Sn)
# print "计算和为：", Sn

# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
#
# 程序分析：请参照程序Python 练习实例14。

# from sys import stdout
#
# for j in range(2, 1001):
#     k = []
#     n = -1
#     s = j
#     for i in range(1, j):
#         if j % i == 0:
#             n += 1
#             s -= i
#             k.append(i)
#
#     if s == 0:
#         print j
#         for i in range(n):
#             stdout.write(str(k[i]))
#             stdout.write(' ')
#         print k[n]


# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

high = 100.0
time = 10
tour =[]

long = []

for i in range(1, time +1):
    if i == 1:
        tour.append(high)
    else:
        tour.append(high * 2)
    high /= 2
    long.append(high)

print('total high tour = {0}'.format(sum(tour)))
print('10 times total high: long ={0}'.format(long[-1]))