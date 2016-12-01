# -*- coding: utf8 -*-
from Tkinter import *
import urllib,urllib2,re,tkMessageBox
root = Tk() #声明一个变量作为窗口对象
root.title ("桌面糗事百科")
root.geometry('500x600+800+600')
def get(page):
    top={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    # html=urllib.urlopen("http://www.qiushibaike.com/text/").read()
    html=urllib2.Request("http://www.qiushibaike.com/text/"+page,headers=top)
    html=urllib2.urlopen(html).read()
    reg=r'<span>([\s\S]+?)</span>'
    reg=re.compile(reg)
    text=re.findall(reg,html)
    print page
    print text
    return text
a=0
page=0
def x():
    global a
    global txtlist
    global page
    if a==0:
        page +=1
        txtlist = get(str(page))
    if a<20:
        txt.delete(1.0,END)
        txt.insert(1.0,txtlist[a].replace("<br/>","\n"))
        a += 1
    else:
        a=0
b = Button(root, text="下一条", width=50, bg="red",command=x)
b.pack(side=BOTTOM)
txt= Text(root,font=("黑体",20))
txt.pack(expand=YES,fill=BOTH)
#get()
root.mainloop()