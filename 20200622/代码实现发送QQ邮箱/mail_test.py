#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> mail_test.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/22 15:02
@Desc    :使用163邮箱或者QQ邮箱发送邮件
================================================="""
import smtplib
from email.header import Header
from email.mime.text import MIMEText


def send_mail():
    # 发件服务器的地址
    # 163服务器的地址
    host = "smtp.163.com"
    # qq服务器的地址
    # host = "smtp.qq.com"
    # 端口
    port = 465

    # 163邮箱的账号密码，此密码是授权码，需要自己开启pop3复制授权码就好
    sender = "用户名@163.com"
    pwd = "授权码"

    # 收件人的账号
    receiver = "3221628304@qq.com"

    # 发送的内容
    body = '<h1>你已成功打卡</h1><p>handles</p>'
    msg = MIMEText(body, 'html')
    msg['subject'] = Header('打卡通知', 'utf-8')
    msg['from'] = Header(sender)
    msg['to'] = Header(receiver)

    try:
        # 连接服务器
        s = smtplib.SMTP_SSL(host, port)
        # 登录邮箱
        s.login(sender, pwd)
        # 发送邮件
        s.sendmail(sender, receiver, msg.as_string())
        print("send success")
        # 关闭服务器连接
        s.quit()
    except smtplib.SMTPException:
        print("ERROR")


if __name__ == '__main__':
    send_mail()

