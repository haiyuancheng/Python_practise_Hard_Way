#!/usr/bin/python
#-*- coding: UTF-8 -*-
#Loop and List

"""
Before you can use a for-loop, you need a way to store the results of
loops somewhere. The best way to do this is with lists
"""

hairs = ['brown','blond', 'red']
eyes = ['brown', 'blue', 'green']
weight = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quartes']

#this first kind of for-loop goes through a list

for number in the_count:
    print "This is count %d" %  number

#some as above

for fruit in fruits:
    print "A fruit of type: %s" % fruit

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it.
for i in change:
    print "I got %r" % i

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    #append is a function that lists understand
    elements.append(i)
print elements

#now we can print them out too
for i in elements:
    print "Element was: %d" %  i

"""
['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
L.append(object) -- append object to end
>>> L = ['history', 'I', 2,]
>>> L.append('I')
>>> L
['history', 'I', 2, 'I']
>>> L.append(['I',1,3,4])
>>> L
['history', 'I', 2, 'I', ['I', 1, 3, 4]]
>>> L.append({'I': 'jason',3: 'yes', 4: 'no'})
>>> L
['history', 'I', 2, 'I', ['I', 1, 3, 4], {'I': 'jason', 3: 'yes', 4: 'no'}]
L.count(value) -> integer -- return number of occurrences of value
>>> L
['history', 'I', 2, 'I', ['I', 1, 3, 4], {'I': 'jason', 3: 'yes', 4: 'no'}]
>>> L.count('I')
2
>>> L.count(1)
0
extend(...)
    L.extend(iterable) -- extend list by appending elements from the iterable
>>> L = ['history', 'I', 2,]
>>> L.extend(['I',1,3,4])
>>> L
['history', 'I', 2, 'I', 1, 3, 4]
>>> L.extend({'I': 'jason',3: 'yes', 4: 'no'})
>>> L
['history', 'I', 2, 'I', 1, 3, 4, 'I', 3, 4]
>>> L.extend({(1, 2), ('I', 2)})
>>> L
['history', 'I', 2, 'I', 1, 3, 4, 'I', 3, 4, (1, 2), ('I', 2)]
insert(...)
    L.insert(index, object) -- insert object before index
>>> L.insert(2, 3)
>>> L
['history', 'I', 3, 2]
>>> L.insert(4, 3)
>>> L
['history', 'I', 3, 2, 3]
>>> L.insert(6, 3)
>>> L
['history', 'I', 3, 2, 3, 3]

pop(...)
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.
>>> L
['history', 'I', 2, 3, 3]
>>> L.remove(3)
>>> L
['history', 'I', 2, 3]
>>> L.remove('I')
>>> L
['history', 2, 3]
>>> L.remove('history')
>>> L
[2, 3]

reverse(...)
    L.reverse() -- reverse *IN PLACE*

>>> L
[2, 3]
>>> L.reverse()
>>> L
[3, 2]
>>> L.append('I')
>>> L
[3, 2, 'I']
>>> L.reverse()
>>> L
['I', 2, 3]


sort(...)
    L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
    cmp(x, y) -> -1, 0, 1

>>> L
['I', 2, 3]
>>> L.sort()
>>> L
[2, 3, 'I']

注意和Python 内置函数sorted区别
sorted(...)
    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
>>> L
[2, 3, 'I']
>>>
>>>
>>> L.append(1)
>>> L
[2, 3, 'I', 1]
>>> L.sort()
>>> L
[1, 2, 3, 'I']
>>> L.append(0)
>>> L
[1, 2, 3, 'I', 0]
>>> sorted(L)
[0, 1, 2, 3, 'I']
>>> L
[1, 2, 3, 'I', 0]
"""