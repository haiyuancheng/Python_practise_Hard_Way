#!/usr/bin/python
#-*- coding: UTF-8 -*-
#While loop
"""
1. 尽量少用while-loop,大部分时候for-loop是更好的选择。
2. 重复检查你的while语句，确定你的布尔表达式最终会变成False。
3. 如果你不确定，就在while循环的结尾打印出你测试的值。看看它的变化。
"""

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers  now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

#改写函数,Python 区分大小写的

def count(Numbers):
    i = 0
    numbers = []
    while i < Numbers:
        print "At the top i is %d" % i
        numbers.append(i)
        i +=1
        print "Numbers now:　", numbers
        print "At the bottom i is %d" % i

    print numbers

    for num in numbers:
        print num

count(10)


#全部改写成参数, New 必须不等于0

def count(Numbers, New):
    i = 0
    numbers = []
    while i < Numbers:
        print "At the top i is %d" % i
        numbers.append(i)
        i += New
        print "Numbers now:　", numbers
        print "At the bottom i is %d" % i

    print numbers

    for num in numbers:
        print num

count(6, 2)


#改写成为 for......range改写, i = i +1可以加可以不加

i = 0
numbers = []
for i in range(0, 6):
    print "At the top i is %d" % i
    numbers.append(i)
    i += 1
    print "Nubers now: ", numbers
    print "At the bottom i is %d" % i
print numbers

for num in numbers:
    print num

"""
for 循环和while循环有什么区别？

for 循环只能对某种事物的集合做循环，而while可以进行任何种类的循环。但是，while循环很容易出错，大部分情况for循环也是一个很好的选择

不是很理解
"""