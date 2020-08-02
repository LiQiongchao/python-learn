"""
发送email
认为是垃圾邮件，发送不成功
smtplib.SMTPDataError: (554, b'DT:SPM 163 smtp10,DsCowADH37W_SSZfEq8cEA--

@Author: QiongchaoLi
@Date: 2020/8/2 11:49
"""
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    send = 'liqiongchao2012@163.com'
    receivers = ['254679323@qq.com', send]
    message = MIMEText('你好，请问明天您那边有时间吗?明天想邀请您来我们公司参观。顺便讨论一下上次说的合作的事情。', 'plain', 'utf-8')
    message['From'] = Header('lee', 'utf-8')
    message['To'] = Header('clancy', 'utf-8')
    message['Subject'] = Header('oio欢迎您', 'utf-8')
    smtper = SMTP('smtp.163.com')
    smtper.login(send, '')
    smtper.sendmail(send, receivers, message.as_string())
    print('send successful')


if __name__ == '__main__':
    main()
