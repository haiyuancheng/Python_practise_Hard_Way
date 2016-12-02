#/!usr/bin/python
#-*- coding: UTF-8 -*-


def sunny(a, b):
    print "Here are two digitals add: %d + %d" % (a, b)

temp_today = sunny(5, 6)
#print "Temperature: %d" % (temp_today) #如果没有rerun的话会报错


def sunny(a, b):
    print "Here are two digitals add: %d + %d" % (a, b)
    return  a + b

temp_today = sunny(9, 6)
print "Temperature: %d" % (temp_today)