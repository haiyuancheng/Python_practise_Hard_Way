#!/usr/bin/python
#-*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.sina.com"
mail_user = "haiyuancheng@sina.com"
mail_pass = "*#@Hyc@sina.com"

sender = 'haiyuancheng@sina.com'
receivers = ['1007701905@qq.com']

message = MIMEText('Python Email test...', 'plain', 'utf-8')
message['From'] = Header("Rookie tutorial", 'utf-8')
message['To'] =  Header("Test", 'utf-8')

subject = 'Python SMTP Email test'
message['Subject'] = Header(subject, 'utf-8')

try:
    server = smtplib.SMTP()
    server.connect(mail_host, 25)
    server.login(mail_user,mail_pass)
    server.sendmail(sender, receivers, message.as_string())
    server.close()
    print "send email success"
except smtplib.SMTPException:
    print "Error: no way send email"
