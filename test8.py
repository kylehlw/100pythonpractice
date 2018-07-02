#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：809*??=800*??+9*?? 其中??代表的两位数,
# 809*??为四位数，8*??的结果为两位数，
# 9*??的结果为3位数。
# 求??代表的两位数，及809*??后的结果。
#
# for x in range(10, 100):
#     if x * 809 >999 and x * 809 <10000 and x * 9 > 99 and x *8>9 and 809 * x == 800 *x + 9 *x:
#         print(x, 809 *x)

# 题目：八进制转换为十进制
# if __name__ == '__main__':
#     n = 0
#     p = raw_input('input a octal number:\n')
#     for i in range(len(p)):
#         n = n * 8 + ord(p[i]) - ord('0')
#     print n

# n =  raw_input('input a octal number:\n')
# l = str(n)
# length = len(n)
# s = 0
# for i in range(length):
#     s += 8 ** i * int(l[length-(i+1)])
# print s
#

# n=raw_input('请输入一个八进制数：')
# #使用列表推导式来写
# lost=sum([int(n[-i])*8**(i-1) for i in range(1,len(n)+1)])
# print '转换十进制数为：%s'%lost
#
#
# def batoshi(num):
#     count=0
#     j=len(num)-1
#     for each_ch in num:
#         count+=pow(8,j)*int(each_ch)
#         j-=1
#     return count
#
# print(batoshi('122'))

# 题目：连接字符串。
#
# delimiter = '|'
# mylist = ['Brazil', 'Russia', 'India', 'China']
# print delimiter.join(mylist)
#
# delimiter = ';'
# mylist1 = ['Brazil', 'Russia', 'India', 'China']
# mylist2 = ['Brazil2', 'Russia1', 'India4', 'China11']
#
# print delimiter.join(mylist1 + mylist2)


# 题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
# 程序分析：999999 / 13 = 76923。

# if __name__ == '__main__':
#     zi = int(raw_input('输入一个数字:\n'))
#     n1 = 1
#     c9 = 1
#     m9 = 9
#     sum = 9
#     while n1 != 0:
#         if sum % zi == 0:
#             n1 = 0
#         else:
#             m9 *= 10
#             sum += m9
#             c9 += 1
#     print '%d 个 9 可以被 %d 整除 : %d' % (c9,zi,sum)
#     r = sum / zi
#     print '%d / %d = %d' % (sum,zi,r)
#
# if __name__ == "__main__":
#     i = int(raw_input('input a number:'))
#     sum = 9
#     while sum % i != 0:
#         sum = sum * 10 + 9
#     print sum,len(str(sum))

# if __name__=='__main__':
#     n=int(raw_input('输入数字:\n'))
#     s=9
#     while True:
#         if s%n==0:
#             l = len(str(s))
#             print '%d 个 9 除于 %d 为整数' % (l,n)
#             break
#         else:
#             st= str(s)+'9'
#             s=int(st)

# 题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
# if __name__ == '__main__':
#     n = 1
#     while n <= 7:
#         a = int(raw_input('input a number:\n'))
#         while a < 1 or a > 50:
#             a = int(raw_input('input a number:\n'))
#         print a * '*'
#         n += 1

# import random
#
# for i in range(1,7):
#     a = random.randint(0,50)
#     print(a)
#     for j in range(0,a):
#         print('*'),
#     print('\n')

# for i in range(7):
#     a=int(raw_input("enter a number(1-50): "))
#     if a>0 and  a<=50:
#         # a=int(raw_input("enter a number(1-50): "))
#         print "*"*a

# 题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
# from sys import stdout
# if __name__ == '__main__':
#     a = int(raw_input('输入四个数字:\n'))
#     aa = []
#     aa.append(a % 10)
#     aa.append(a % 100 / 10)
#     aa.append(a % 1000 / 100)
#     aa.append(a / 1000)
#
#     for i in range(4):
#         aa[i] += 5
#         aa[i] %= 10
#     for i in range(2):
#         aa[i], aa[3 - i] = aa[3 - i], aa[i]
#     for i in range(3, -1, -1):
#         stdout.write(str(aa[i]))
#

# n = raw_input('Please input:')
# a = []
# n = str(n)
#
# for i in range(len(n)):
#     a.append((int(n[i])+5)% 10)
#
# a[0],a[1],a[2], a[3] = a[3],a[2],a[1],a[0]
#
# print "".join('%s' %s for s in a)

# 题目：列表使用实例。
# list
# 新建列表
testList = [10086, '中国移动', [1, 2, 4, 5]]

# 访问列表长度
print len(testList)
# 到列表结尾
print testList[1:]
# 向列表添加元素
testList.append('i\'m new here!')

print len(testList)
print testList[-1]
# 弹出列表的最后一个元素
print testList.pop(-1)
print len(testList)
print testList
# list comprehension
# 后面有介绍，暂时掠过
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print matrix
print matrix[1]
col2 = [row[1] for row in matrix]  # get a  column from a matrix
print col2
col2even = [row[1] for row in matrix if row[1] % 2 == 0]  # filter odd item
print col2even

