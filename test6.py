#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：打印出杨辉三角形
#
# a = []
# d = 20
# for i in range(d):
#     a.append([])
#     for j in range(d):
#         a[i].append(0)
# for i in range(d):
#     a[i][0] = 1
#     a[i][i] = 1
#
# for i in range(2,d):
#     for j in range(1,i):
#         a[i][j] = a[i - 1][j - 1] + a[i- 1][j]
# for i in range(d):
#     print('  ' * (d - i)),
#     for j in range(i+1):
#         print(a[i][j]),
#         print ' ',
#     print

# 题目：查找字符串。　
# sStr1 = 'abcdefg'
# sStr2 = 'cde'
# print sStr1.find(sStr2)
# s1 = 'asw22234'
# s2 = '22'
# s3 = '23'
# s4 = '4'
# print s1.find(s2) ,s1.find(s3), s1.find(s4)

# 题目：画椭圆。　
# 程序分析：使用 Tkinter。
# from Tkinter import *
#
# x = 160
# y = 160
# top = y - 30
# bottom = y - 30
#
# canvas = Canvas(width=400, height=600, bg='white')
# for i in range(20):
#     canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
#     top -= 5
#     bottom += 5
# canvas.pack()
# mainloop()
#


# # 题目：利用ellipse 和 rectangle 画图。
# from Tkinter import *
# canvas = Canvas(width = 400,height = 600,bg = 'white')
# left = 20
# right = 50
# top = 50
# num = 15
# for i in range(num):
#     canvas.create_oval(250 - right,250 - left,250 + right,250 + left)
#     canvas.create_oval(250 - 20,250 - top,250 + 20,250 + top)
#     canvas.create_rectangle(20 - 2 * i,20 - 2 * i,10 * (i + 2),10 * ( i + 2))
#     right += 5
#     left += 5
#     top += 10
#
# canvas.pack()
# mainloop()


# 题目：一个最优美的图案。　
# import math
# class PTS:
#     def __init__(self):
#         self.x = 0
#         self.y = 0
# points = []
#
# def LineToDemo():
#     from Tkinter import *
#     screenx = 400
#     screeny = 400
#     canvas = Canvas(width = screenx,height = screeny,bg = 'white')
#
#     AspectRatio = 0.85
#     MAXPTS = 15
#     h = screeny
#     w = screenx
#     xcenter = w / 2
#     ycenter = h / 2
#     radius = (h - 30) / (AspectRatio * 2) - 20
#     step = 360 / MAXPTS
#     angle = 0.0
#     for i in range(MAXPTS):
#         rads = angle * math.pi / 180.0
#         p = PTS()
#         p.x = xcenter + int(math.cos(rads) * radius)
#         p.y = ycenter - int(math.sin(rads) * radius * AspectRatio)
#         angle += step
#         points.append(p)
#     canvas.create_oval(xcenter - radius,ycenter - radius,
#                        xcenter + radius,ycenter + radius)
#     for i in range(MAXPTS):
#         for j in range(i,MAXPTS):
#             canvas.create_line(points[i].x,points[i].y,points[j].x,points[j].y)
#
#     canvas.pack()
#     mainloop()
# if __name__ == '__main__':
#     LineToDemo()

# 题目：输入3个数a,b,c，按大小顺序输出。
# n1 = raw_input('Number1:')
# n2 = raw_input('Number2:')
# n3 = raw_input('Number3:')
#
# def swith(a1,a2):
#     return a2,a1
#
# if n1 > n2: n1, n2 = swith(n1, n2)
#
# if n1 > n3: n1, n3 = swith(n1,n3)
# if n2 > n3: n2, n3 = swith(n2,n3)
# print(n1,n2,n3)
#
# a= []
# for i in range(3):
#     a.append(int(raw_input('Please input number%d:' % (i +1) )))
# # a.sort()
# # for i in range(len(a)):
# #     print a[i],
#
# for i in range(len(a)):
#     print(min(a)),
#     a.remove(min(a))
#

# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
# a= []
# for i in range(7):
#     a.append(int(raw_input('Please input number%d:' % (i + 1))))
# print('old:', a )
# for i in range(len(a)):
#     if a[i] == max(a):
#         a[0], a[i] = a[i], a[0]
#     elif a[i] == min(a):
#         a[-1], a[i] = a[i], a[-1]
# print('new:', a)


# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
# a = []
# # print a.pop()
# n = int(raw_input('please input number N:'))
# m = int(raw_input('Please input number M:'))
# for i in range(n):
#     a.append(raw_input('please input number%d:' % (i+1)))
# print('original:',a)
# for _ in range(m):
#     a.insert(0,a.pop())
# print(a)

# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
# n=int(input("输入人数:"))
# List=[]
# for i in range(1,n+1):
#     List.append(i)
#
# sum=0
# while 1:
#     t=0;
#     for i in range(1,len(List)+1):
#         sum=sum+1
#         if (sum)%3==0:
#             List.pop(i-1-t)
#             t=t+1
#
#     if len(List)==1:
#         print("最后留下的是原来第%d号的那位" % List[0])
#         break

# data = [i+1 for i in range(34)]
# print(data)
# i = 1
# while len(data) > 1:
#     if i % 3 == 0:
#         data.pop(0)
#     else:
#         data.insert(len(data),data.pop(0))
#     i += 1
# print(data)

# 题目：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
if __name__ == '__main__':
    s_1 = raw_input('please input a string:')
    print('your input string has %d characters.' % len(s_1))