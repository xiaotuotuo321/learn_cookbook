# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name :      1_将序列分解为单独的变量
   Description :    
   Author :         whp
   date :           2020/10/12
-------------------------------------------------
   Change Activity:
                    2020/10/12:
-------------------------------------------------
"""
__author__ = "whp"


p = (4, 5)
x, y = p
print("x", x)
print("y", y)

data = ["ACME", 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print("name", name)
print("shares", shares)
print("price", price)
print("date", date)

# 不想要的元素可以使用_省略掉, 元组还可解包
_, _, _, (year, month, day) = data
print("year", year)
print("month", month)
print("day", day)

# 不仅仅只是元组或列表，只要对象是可迭代的，就可以执行分解操作。包括字符串，文件对象，迭代器和生成器
s = "Hello"

a, b, c, d, e = s
print("a", a)
print("b", b)
print("c", c)
print("d", d)
print("e", e)
