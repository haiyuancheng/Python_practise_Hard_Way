#!/usr/bin/python
#-*- coding: UTF-8 -*-
"""
闰年的条件：四年一闰年，非百年而不润，四百年再润
"""
#year = int(raw_input("请输入一个年份: "))
year = input("请输入一个年份: ")
if (year % 4) == 0:
    if (year % 100) == 0:
        if(year % 400) ==0:
            print "This year is a leap year."
            #print "{0}是闰年".format(year)  #能被百年整除一定是闰年（世纪年）
            print "%d 是闰年" % (year)
        else:
            print "This year is nonleap year."
            #print "{0}不是闰年".format(year)
            print "%d 不是闰年" % (year)
    else:
        print "This year is a leap year." #非世纪年能被四整除是闰年
        #print "{0}.闰年".format(year)
        print "%d 是闰年" % (year)
else:
    print "This year is not a leap year."
    #print "{0} 不是闰年".format(year)
    print "%d 不是闰年" % (year)


"""
有时间改写嵌套
"""