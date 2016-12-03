#!/usr/bin/env python2.7
# coding:utf-8
'''
Created on: 2016年12月3日

@author: Jason

Version: 1.1

Description: 输入用户名密码，认证成功显示欢迎信息，认证失败，输错三次后锁定

Help:
'''
import os, getpass

# 定义用户信息写入函数，用于把用户信息写回文件
def write_to_account_file(accounts, account_file_path):
    account_file = open(account_file_path, 'w')
    for key,val in accounts.items():
        line = []
        line.append(key)
        line.extend(val)
        #print(' '.join(line))
        account_file.write(' '.join(line) + '\n')
    account_file.close()

if __name__ == '__main__':

    '''
    @parameters:
        account_file_path: 账户文件
        password_col_num: 账户文件中密码所在的列（从0开始）
        status_col_num: 账户文件中账户状态所在的列（从0开始）
        error_count_num: 账户文件中输入错误次数所在的列（从0开始）
        app_info: 系统信息，用于启动应用后的输出
        welcome_msg: 用户成功登录系统后的信息
        error_count_max: 允许用户密码输错错误的最大次数
    '''
    account_file_path = 'account.db'
    password_col_num = 1
    status_col_num = 2
    error_count_num = 3
    error_count_max = 3
    app_info = '''
+-----------------------------------+
| Welcome to DevOps System 
| Version: 1.0                      |
| Author: Jason
+-----------------------------------+
'''
    #welcome_msg = 'Welcome %s, authentication is successful!'
    # 判断账户文件是否存在
    if os.path.exists(account_file_path):
        account_file = open(account_file_path, 'r')
    else:
        print('\33[1;32;40m Error: Account file "account.db" is not exit, please check!\033')
        exit(1)

    # 读账户文件
    accounts = {} #建一个空的数据字典
    for line in account_file.readlines():
        account = line.strip().split()
        accounts[account[0]] = account[1:]#第二个元素到结尾
    account_file.close()

    flag = True
    while flag:
        print('\033[1;31;40m %s \033[1;m') %  app_info
        # 输入用户名
        #username = input('Username(Enter quit to exit): ').strip()
        username = raw_input('\033[1;32;40m Username(Enter quit to exit):\033[1;m ').strip()
        # 判断是否输入的是否为quit
        if username == 'quit':
            # 是则退出循环，程序结束
            break
       # password = raw_input('Password: ').strip()
        # 判断用户名是否存在
        if username not in accounts:
            # 不存在提示错误信息并退出当前循环让用户重新输入
            print('\033[1;33;40m Error: Username or Password it is error!\033[1;m')
            continue
        # 判断用户是否被锁定
        if accounts[username][status_col_num - 1] == 'lock':
            # 如果被锁定退出当前循环让用重新如输入
            print('\033[1;33;40m Error: Account is locked. Please contact the administrator!\033[1;m')
            #continue
            break
        password = getpass.getpass('Password: ').strip()
        # 判断用户密码是否正确
        if password == accounts[username][password_col_num - 1]:
            # 正确显示欢迎信息
            #print(welcome_msg %username)
            print "\033[1;31;40m Welcome %s, Authentication is successful!\033[1;m" % username
            break
        else:
            # 不正确
            # 提示用户名或密码错误
            print('\033[1;36;40m Error: Username or Password it is error!\033[1;m')
            # 输入错误次数加1
            accounts[username][error_count_num - 1] = str(int(accounts[username][error_count_num - 1]) + 1)
	    #如果账户本身输入达到3次且处于unlock的情况下、
	    if int(accounts[username][error_count_num -1]) > error_count_max:
		print "\033[1;35;40m Your account just under unlock status, contact admin chang login nums\033[1;m"
		break
            # 判断是否已经达到3次
            if int(accounts[username][error_count_num - 1]) == error_count_max:
                # 如果输入错误达到3次
                # 提示账户将被锁定
                print("\033[1;34;40m Error: This account will be locked, Please contact the administrator! System will be exit!\033[1;m")
                # 将用户状态改为lock并写入文件
                accounts[username][status_col_num - 1] = 'lock'
                write_to_account_file(accounts, account_file_path)
                break

