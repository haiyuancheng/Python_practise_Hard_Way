#!/usr/bin/python
#-*- coding: UTF-8 -*-
#Boolean and Practice

True and True                   True

False and True                  False

1 == 1 and 2 == 1               False

"test" == "test"                True

1 == 1 or 2 != 1                True

True and 1 == 1                 True

False and 0 != 0                False

"test" == "testing"            False

1 != 0 and 2 == 1              False

"test" != "testing"            True

"test" == 1                    False

not (True and False)           True

not(1 == 1 and 0 != 1)         False

not(10 == 1 or 1000 == 1000)   False

not (1 != 10 or 3 == 4)        False

not ("testing" == "testing" and "Zed" == "Cool Guy")  True

1 == 1 and (not("testing" == 1 or 1 ==0))  True

"chunky" == "bacon" and (not(3 == 4 or 3 == 3))   False

3 == 3 and (not("testing" == "testing" or "Python" == "Fun" )) False


"""
output result

>>> True and True
True

>>> False and True
False
>>> 2 == 1 and 1 == 1
False
>>> "test" ==  "test"
True
>>> 1 == 1 or  2 != 1
True
>>> True and 1 == 1
True
>>> False and 0 != 0
False
>>> "test" and "testing"
'testing'
>>> "test" == "testing"
False
>>> 1 != 0 and 2 == 1
False
>>> "test"  != "testing"
True
>>> "test"   == 1
False
>>> not(true and false)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> not(True and False)
True

>>> not(1 == 1 and 0 != 1)
False
>>> not(10 == 1 and 1000 == 1000)
True
>>> not(10 == 1 or 1000 == 1000)
False
>>> not(1 != 10 or 3 == 4)
False
>>> not ("testing" == "testing" and "Zed" == "Cool Guy")
True
>>> 1 == 1 and (not("testing" == 1 or 1 ==0))
True
>>> "chunky" == "bacon" and (not(3 ==4  or 3 ==3))
False
>>> 3 == 3 amd (not("testing" == "testing" or "Python" == "Fun"))
  File "<stdin>", line 1
    3 == 3 amd (not("testing" == "testing" or "Python" == "Fun"))
             ^
SyntaxError: invalid syntax
>>> "chunky" == "bacon" and (not(3 ==4  or 3 ==3))
False
>>> 3 == 3 and (not("testing" == "testing" or "Python" == "Fun"))
False
>>> "test" and "test"
'test'
>>> 1 and 1
1

>>> False and 1
False
>>> 1 and True
True
>>> True and 1
1
>>> 1 and 1
1

"""