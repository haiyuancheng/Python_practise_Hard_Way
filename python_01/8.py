#!/usr/bin/python
#-*- coding: utf-8 -*-
#Practise  for email
#smtplib
import  smtplib
import  string

HOST = "smtp.sina.com"
SUBJECT =  "Test email from Python"
FROM = "haiyuancheng@sina.com"
TO = "1007701905@qq.com"
text = "Python rules them all"
BODY = string.join((#组装sendmail 方法的邮件主题内容，各段以"\r\n"进行分割)
       "FROM: %s"  % FROM,
       "TO: %s"  % TO,
       "SUBJECT: %s" % SUBJECT,
       "",
       text
), "\r\n")

server = smtplib.SMTP()
server.connect(HOST,25)
server.starttls()
server.login("haiyuancheng@sina.com","*#@Hyc@sina.com")
#sever.sendemail(FROM, [TO], BODY)
server.sendmail(FROM, [TO], BODY)
server.quit()

