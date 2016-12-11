#!/usr/bin/python
#-*- coding: UTF-8 -*-
#修改错误代码

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words)
    """Prints the first word after popping it off."""
    word = words.poop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans \ 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates == secret_formula(start-point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont


sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
.print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
prin sorted_words

print_irst_and_last(sentence)

   print_first_a_last_sorted(senence)



#修改后并且运行的结果
import ex_22

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): #函数后面以冒号结束
    """Prints the first word after popping it off."""
    word = words.pop(0) #list.pop(i) not poop
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #括号要成对出现
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #除是/ 不是\
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point) #是jelly_beans 并不是beans sart_ not start- 变量= not ==

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (jelly_beans, jars, crates) #是jelly_beans 并不是beans

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point) #括号成对出现 是start_point not start_pont


sentence = "All god\tthings come to those who weight."

words = ex_22.break_words(sentence)
sorted_words = ex_22.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex_22.sort_sentence(sentence)
print sorted_words #是print not prin

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)# 是sentence not senence



#output reslut
"""
[jason@shadowsocks practise]$ ./ex_23.py
['All', 'god\tthings', 'come', 'to', 'those', 'who', 'weight.']
['All', 'come', 'god\tthings', 'those', 'to', 'weight.', 'who']
All
weight.
All
who
Let's practice everything.
You'd need to know 'bout escapes with \ that do
 newlines and    tabs.
--------------

        The lovely world
with logic so firmly planted
cannot discern
 the needs of love
nor comprehend passion from intuition
and requires an explantion

                where there is none.

--------------
This should be five: 6
With a starting point of: 10000
We'd have 5000000 jeans, 5000 jars, and 50 crates.
We can also do that this way:
We'd have 500000 beans, 500 jars, and 5 crabapples.
All
weight.
All
who
['All', 'come', 'god\tthings', 'those', 'to', 'weight.', 'who']
All
weight.
All
who
"""