#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。

# Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
#
# l = raw_input('Plsease input:').upper()
#
# if l == 'M':
#     print('is Monday')
# elif l == 'W':
#     print('is Wednesday')
# elif l == 'F':
#     print('is Friday')
# elif l == 'T':
#     l2 = raw_input('Please input second letter:').lower()
#     if l2 == 'u':
#         print('is Tuesday')
#     elif l2 == 'h':
#         print('is Thursday')
#     else:
#         print('data error')
# elif l == 'S':
#     l2 = raw_input('Please input second letter:').lower()
#     if l2 == 'a':
#         print('is Saturday')
#     elif l2 == 'u':
#         print('is Sunday')
#     else:
#         print('data error')
# else:
#     print('data error')

# 题目：按相反的顺序输出列表的值。
# a = [1,3,44,55,66]
# for i in a[::-1]:
#     print i
#
# print a.sort()

# 题目：按逗号分隔列表。
# L = [1,2,3,4,5]
# s1 = ','.join(str(n) for n in L)
# print s1

# 题目：练习函数调用。
# def hello_world():
#     print 'hello world'
#
#
# def three_hellos():
#     for i in range(3):
#         hello_world()
#
#
# if __name__ == '__main__':
#     three_hellos()

# 题目：文本颜色设置。
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#
#
# print bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC


# 题目：求100之内的素数。
# l = int(raw_input('最小值：'))
# m = int(raw_input('最大值：'))
#
# for i in range(l, m +1):
#     if i > 1:
#         for n in range(2, i):
#             if (i % n) == 0:
#                 break
#         else:
#             print(i)


# 题目：对10个数进行排序。
#
# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
# if __name__ == "__main__":
#     N = 10
#     # input data
#     print '请输入10个数字:\n'
#     l = []
#     for i in range(N):
#         l.append(int(raw_input('输入一个数字:\n')))
#     print
#     for i in range(N):
#         print l[i]
#     print
#
#     for i in range(N - 1):
#         min = i
#         for j in range(i+1, N):
#             if l[min] > l[j]:
#                 min = j
#         l[i],l[min] = l[min],l[i]
#
#     print('after sort')
#     for i in range(N):
#         print l[i]

# 题目：求一个3*3矩阵主对角线元素之和。
# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。

# if __name__ == '__main__':
#     a = []
#     sum = 0.0
#     for i in range(3):
#         a.append([])
#         for j in range(3):
#             a[i].append(float(raw_input("input num:\n")))
#     for i in range(3):
#         sum += a[i][i]
#     print sum


# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
#
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
#
# if __name__ == '__main__':
#
#     a = [1,4,6,9,13,16,19,28,40,100]
#     print '原始列表:'
#     for i in range(len(a)):
#         print a[i],
#     number = int(raw_input("\n插入一个数字:\n"))
#     l = len(a)
#     end = a[l -1]
#
#     if number > end:
#         a[l] = number
#     else:
#         for i in range(l):
#             if a[i] > number:
#                 temp1 = a[i]
#                 a[i] = number
#                 for j in range(i + 1,l):
#                     temp2 = a[j]
#                     a[j]  = temp1
#                     temp1 = temp2
#
#                 break
#     print('after sort:')
#     print(a)

# 题目：将一个数组逆序输出。
#
# a = [3,55,66,33,56,333,99,22]
# print (a)
# l = len(a)
# for i in range(l/2):
#     a[i],a[l-i -1] = a[l -i -1],a[i]
#
# print(a)






