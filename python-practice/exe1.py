#1
# import functools
# n="ABC123"
# b=list(filter(lambda x:x.isdigit(),n))
# op=functools.reduce(lambda a,b:int(a)+int(b),b)
# print(op)

#2
# def star(n):
#     a = 2 * n - 2
#     for i in range(0, n):
#         for j in range(0, a):
#             print(end=" ")
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("\r")
#         a=a-1
# n = 5
# star(n)

#3
import functools
# dic={"a":1,"e":2,"i":3,"o":4,"u":5}
# aa="narashimmhan"
# sum=0
# for k in aa:
#     for i,j in dic.items():
#         if k==i:
#             sum+=j
# print(sum)

#4
# a="AbCdEfGhIj"
# for i in a:
#     if i.isalpha():
#         if ord(i) > 90:
#             v = ord(i)-32
#             print(chr(v),end = "")
#         else:
#             v = ord(i) + 32
#             print(chr(v),end="")
#     else:
#         print(i,end = "")

#5
# x = "-121"
# w = ""
# for i in x:
#     w = i + w
# if (x==w):
#     print("Palindrome")
# else:
#     print("not a palindrome")

#6
# lis=["sjxd","ddal","sdgc"]
# dic={}
# s=[]
# op=[]
# for i in lis:
#     s.append(i[2])
#     dic[i]=i[2]
# s.sort()
# print(lis)
# for k in s:
#     for i,j in dic.items():
#         if k==j:
#             op.append(i)
# print(op)

#7
# import re
# aaa=(re.findall("[\w]{2,64}@[gmail|yahoo|hotmail]{2,10}.[\w]{2,3}","simma@gmail.com kishore@hotmail.com gova@yahoo.com aravinth@xyz.com"))
# print(aaa)

#8
# import re
# aa=(re.findall("[\w]{2,20}@","sima@gmail a@gmail"))
# print(aa)

#9
# inp="asdfloiucbgk"
# a="cgf"
# count=0
# if len(a)>3:
#     print("too large")
# elif len(a)<3:
#     print("too small")
# else:
#     for i in a:
#         for j in inp:
#             if i==j:
#                 count+=1
# if len(a)==count:
#     print("satisfied")