# -*- coding: UTF-8 -*-
'''
发送txt文本邮件
小五义：http://www.cnblogs.com/xiaowuyi
'''
import smtplib #import smtplib module
from email.mime.text import MIMEText #import MIMEText class

mailto_list = ['1007701905@qq.com','869596773@qq.com']
mail_host = "smtp.sina.com"  # set up sever
mail_user = "haiyuancheng"  # user
mail_pass = "*#@Hyc@sina.com"  # password
mail_postfix = "sina.com"  # The suffix of the outbox


def send_mail(to_list, sub, content):
    me = "hello" + "<" + mail_user + "@" + mail_postfix + ">" #define a variable me
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')  #create a MIMEText object, define content,type and  charese
    msg['Subject'] = sub #define email sub
    msg['From'] = me  # define email sender
    msg['To'] = ";".join(to_list) # define email reciever
    try:
        server = smtplib.SMTP() #Create smtp()object
        server.connect(mail_host) #From connetct method
        server.login(mail_user, mail_pass)  #Email info check
        server.sendmail(me, to_list, msg.as_string()) #Send email
        server.close() # Disconnect smtp
        print  "email send success!"
        return True    # Return the value
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    if send_mail(mailto_list, "hello", "hello world！"):
        print "发送成功"
    else:
        print "发送失败"