#Variable and Names 2
# -*- coding: utf-8 -*-
'''
my_name = 'JasonCheng'
my_age = 29 # not a lie
my_height = 65 # inches
my_weight = 173 #lbs
my_eyes = 'black'
my_teeth = 'White'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that;s not too heavy."
print "He's got %s eys and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
#This line is tricky, try to get it exactly right
print "If I add %d,%d,and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
print round(1.733,0)
'''
name = 'jasoncheng'
age = 29
hegiht = 70
centimeters = hegiht * 2.54
weight = 180
kios = weight * 0.45
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d centimeters tall" % centimeters
print "He's %d pounds heavy." % kios
print "He's got %s eys and %s hair." % (eyes, hair)
print "He's got %r eys and %r hair." % (eyes, hair) #%r重现具体的对象
print "His teeth are usually %s depending on the coffee" % teeth

