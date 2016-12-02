#!/usr/bin/python
#-*- coding: UTF-8 -*-
#Functions Can Return Something

"""
add: 加
subtract: 减
multipy: 乘
divide: 除
"""
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "SUBSTRACT %d - %d" % (a, b)
    return a - b

def multipy(a, b):
    print "MUTIPY  %d * %d" % (a, b)
    return  a * b

def divide(a, b):
    print "DIVIDE %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions"

age = add(30, 5)
height = substract(78, 4)
weight = multipy(90, 2)
iq  =  divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle"

iq_01 = divide(iq, 2)
weight_01 = multipy(weight, iq_01)
height_01 = substract(height, weight_01)

what = add(age, height_01)

print "That becomes: ", what, "Can you do it by hand?"


"""
练习
28 + 30 / 5 + 2 *3 + 260 - 20
"""

math = add(28, substract(add(add(divide(30, 5),multipy(2, 3)),260), 20))

print "This is the result: %d" % math

'''
分解
'''

s = multipy(2, 3)
r = divide(30, 5)
t = add (r, s)
z = add(t, 260)
y = substract(z, 20)
x = add(28, y)

print "Now, we test the result is: %d" % x