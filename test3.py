#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个.
#       第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
#       到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# t = 1
# for i in range(9,0,-1):
#     x = (t + 1) * 2
#     t = x
# print t

# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，
# c说他不和x,z比，
# 请编程序找出三队赛手的名单。
#
# for i in range(ord('x'),ord('z') + 1):
#     for j in range(ord('x'),ord('z') + 1):
#         # a说他不和x比，
#         if i != j:
#             for k in range(ord('x'),ord('z') + 1):
#                 if (i != k) and (j != k):
#                     # c说他不和x,z比，
#                     if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
#                         print 'order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k))

# 题目：打印出如下图案（菱形）:
# #
# #    *
# #   ***
# #  *****
# # *******
# #  *****
# #   ***
# #    *
#
# from sys import stdout
# for i in range(4):
#     for j in range(2 - i + 1):
#         stdout.write(' ')
#     for k in range(2 * i + 1):
#         stdout.write('*')
#     print
#
# for i in range(3):
#     for j in range(i + 1):
#         stdout.write(' ')
#     for k in range(4 -2 * i + 1):
#         stdout.write('*')
#     print


# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
#
# 程序分析：请抓住分子与分母的变化规律。

# a = 2.0
# b = 1.0
# s = 0
# for i in range(1,21):
#     s += a / b
#     # t = a
#     # a = a + b
#     # b = t
#     b , a = a , a + b
#
# print s

# a = 2.0
# b = 1.0
# l = []
# l.append(a / b)
# for n in range(1,20):
#     b,a = a,a + b
#     l.append(a / b)
# print reduce(lambda x,y: x + y,l)

# 题目：求1+2!+3!+...+20!的和。

#1
# t , s = 1, 0
# for i in range(1, 21):
#     t *= i
#     s += t
# print '1! + 2! + 3! + ... + 20! = %d' % s

#2
# s , l = 0 , range(1,21)
# def op(x):
#     r = 1
#     for i in range(1,x +1):
#         r *=i
#     return r
# s = sum(map(op, l))
# print s , map(op, l)    # map() 好用

# 题目：利用递归方法求5!
# 程序分析：递归公式：fn=fn_1*4!
#
# def fact(i):
#     sum = 0
#     if i == 0:
#         sum = 1
#     else:
#         sum = i * fact(i -1)
#     return sum
#
# print fact(5)

# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# s= raw_input('please string:')
# l = len(s)
# def output(str1,l):
#     if l == 0:
#         return ()
#     print s[l-1],
#     output(str1, l -1)
#
# print(output(s,l))

# 题目：有5个人坐在一起，
# 问第五个人多少岁？他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。请问第五个人多大？
#
# 程序分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。
#
# def age(x):
#     if x == 1: c = 10
#     else: c = age(x -1) + 2
#     return c
#
# print age(5)


# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# 程序分析：学会分解出每一位数。

# def ck(x):
#     a = x / 10000
#     b = x % 10000 / 1000
#     c = x % 1000 / 100
#     d = x % 100 / 10
#     e = x % 10
#
#     if a != 0:
#         print('5位数：',e,d,c,b,a)
#     elif b != 0:
#         print('4位数：',e,d,c,b)
#     elif c != 0:
#         print('3位数：',e,d,c,)
#     elif d != 0:
#         print('2位数：',e,d)
#     elif e != 0:
#         print('1位数：',e)
#
# num = int(raw_input('input number:'))
# ck(num)


# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
# n = int(raw_input('Please input number:'))
# s = str(n)
# t = True
#
# for i in range(len(s)/2):
#     if s[i] != s[-i - 1]:
#         t = False
#         break
#
# if t :
#     print('%d is right') % n
# else:
#     print('%d is not right') % n



