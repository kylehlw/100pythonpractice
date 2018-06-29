#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：编写input()和output()函数输入，输出5个学生的数据记录。
# N = 3
# # stu
# # num : string
# # name : string
# # score[4]: list
# student = []
# for i in range(5):
#     student.append(['', '', []])
#
#
# def input_stu(stu):
#     for i in range(N):
#         stu[i][0] = raw_input('input student num:\n')
#         stu[i][1] = raw_input('input student name:\n')
#         for j in range(3):
#             stu[i][2].append(int(raw_input('score:\n')))
#
#
# def output_stu(stu):
#     for i in range(N):
#         print '%-6s%-10s' % (stu[i][0], stu[i][1])
#         for j in range(3):
#             print '%-8d' % stu[i][2][j]
#
#
# if __name__ == '__main__':
#     input_stu(student)
#     print student
#     output_stu(student)

# class Student:
#     name = ""
#     age = 0
#     score = [None] * 4
#
#     def input(self):
#         self.name = raw_input("Input name, please: ")
#         self.age = int(raw_input("Input age, please: "))
#         for i in range(len(self.score)):
#             self.score[i] = int(raw_input("Input %d score, please: " % (i + 1)))
#
#     def output(self):
#         print 'Output name: %s' % self.name
#         print 'Output age: %d' % self.age
#         for i in range(len(self.score)):
#             print 'Output %d score: %d' % ((i + 1), self.score[i])
#
#
# if __name__ == "__main__":
#     N = 5
#     studentArray = [Student()] * N
#     for i in range(len(studentArray)):
#         studentArray[i].input()
#
#     for i in range(len(studentArray)):
#         studentArray[i].output()

# # 题目：创建一个链表。
# if __name__ == '__main__':
#     ptr = []
#     for i in range(5):
#         num = int(raw_input('please input a number:\n'))
#         ptr.append(num)
#     print ptr
#


# 题目：反向输出一个链表。
# if __name__ == '__main__':
#     ptr = []
#     n = 5
#     for i in range(n):
#         num = int(raw_input('please input a number(%d/%d):' %(i+1,n)))
#         ptr.append(num)
#     print ptr
#     ptr.reverse()
#     print ptr

# 题目：列表排序及连接。
# 程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。
# if __name__ == '__main__':
#     a = [1,31,22]
#     b = [63,14,5]
#     a.sort()
#     b.sort()
#     print a, b
#     a.extend(b)
#     print a
#     a = a +b
#     print a

# 题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
# if __name__ == '__main__':
#     def ou(n):
#         s = 0.0
#         for i in range(2, n + 1, 2):
#             s += 1.0/i
#         return s
#     def ji(n):
#         s = 0.0
#         for i in range(1, n+1,2):
#             s += 1.0/i
#         return s
#
#     num = int(raw_input('please input a number:'))
#     if num % 2 == 0:
#         sum = ou(num)
#     else:
#         sum = ji(num)
#     print sum

# def sumf(n):
#     ls = [ 1.0/i for i in range(n,0, -2)]
#     print ls
#     return sum(ls)
#
# print sumf(5)
# print sumf(6)
#
#

# s = [i for i in range(10)]
# print s


# 题目：循环输出列表
# s = ["man","woman","girl","boy","sister","boys","boy2"]
# print s
# s.sort()
# for i in s:
#     print(i),
#

# # 题目：找到年龄最大的人，并输出。请找出程序中有什么问题。
# if __name__ == '__main__':
#     person = {"li":18,"wang":50,"zhang":20,"sun":22}
#     # print max(person.values())
#     print person.keys()
#
#     for n, k in person.items():
#         if k == max(person.values()):
#             print n,":",k

# 题目：海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
# 第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？

# if __name__ == '__main__':
#     i = 0
#     j = 1
#     x = 0
#     while (i < 5) :
#         x = 4 * j
#         for i in range(0,5) :
#             if(x%4 != 0) :
#                 break
#             else :
#                 i += 1
#             x = (x/4) * 5 +1
#         j += 1
#     print x

num = int(input("输入猴子的数目:"))


def fn(n):
    if n == num:
        return (4 * x)  # 最后剩的桃子的数目
    else:
        return (fn(n + 1) * 5 / 4 + 1)


x = 1
while 1:
    count = 0
    for i in range(1, num):
        if fn(i) % 4 == 0:
            count = count + 1
    if count == num - 1:
        print("海滩上原来最少有%d个桃子" % int(fn(0)))
        break
    else:
        x = x + 1



