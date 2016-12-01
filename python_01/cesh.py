#!/usr/bin/python
#-*- coding: UTF-8 -*-
import os
import poplib, email
from email.header import decode_header
import smtplib
import time
import os, sys
import random

    p = poplib.POP3('pop.qq.com')
    p.user('1007701905@qq.com')
    p.pass_('C*#@721670789%hy')
    ret = p.stat()

for item in p.list()[1]:
    number, octets = item.split(' ')
    print "Message %s: %sbytes" % (number, octets)
    lines = p.retr(number)[1]
    msg = email.message_from_string("\n".join(lines))
    print msg.as_string()
    print msg.get_payload()
    if msg.get_payload() == "start\n\n":
        return 0