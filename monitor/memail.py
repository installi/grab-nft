# !/usr/bin/env python
# -*- coding: utf-8 -*-

# __time__: 2021/10/20 __auth__: 
# __remark__: email helper

import smtplib, time

from email.header import Header
from email.mime.text import MIMEText

class EmailHelper(object):
    def __init__(self, receivers, paser) -> None:
        super().__init__()
        self.__paser = paser
        self.__receivers = receivers

        self.__host = 'smtp.qq.com'
        self.__sender = '178320753@qq.com'
        self.__password = 'apuxyhsjncdccahg'

        # self.__host = 'smtp.126.com'
        # self.__sender = 'jjjk20211021@126.com'
        # self.__password = 'THRDQVGWCOVDCTWX'

        self.__mail = None

    def __init_connect(self):
        try:
            if self.__mail: return

            self.__mail = smtplib.SMTP()
            self.__mail.connect(self.__host, 25)
            self.__mail.login(self.__sender, self.__password)
        except smtplib.SMTPException as e:
            self.__paser.exit('\nMAIL_INIT: %s\n' % str(e))
            # print(e)

    def send_email(self, transaction, detail, rpc):
        try:
            info, contnet = {}, '''
                <h3>金额为: <span style="color: red">%(amount)s</span> (%(symbol)s) -【%(genre)s】</h3>
                <p>%(genre)s - <a href="https://etherscan.io/address/%(name)s/">%(name)s(%(symbol)s)</a></p>
                <p>RPC: %(rpc)s | 区块号: %(number)s</p>
                <p>HASH: <a href="https://etherscan.io/tx/%(hash)s/">%(hash)s</a></p>
	            <p>发送人: <a href="https://etherscan.io/address/%(from)s/">%(from)s</a></p>
	            <p>接收人: <a href="https://etherscan.io/address/%(to)s/">%(to)s</a></p>
                <p>交易时间: %(time)s</p>
            '''

            info['rpc'] = rpc
            info['name'] = detail['name']
            info['symbol'] = detail['symbol']
            info['amount'] = detail['amount']
            info['number'] = transaction['blockNumber']
            info['hash'] = transaction['hash'].hex()
            info['from'] = transaction['from']
            info['to'] = transaction['to']

            t = time.localtime(detail['timestamp'])
            info['time'] = time.strftime('%Y-%m-%d %H:%M:%S', t)
            info['genre'] = '转出' if detail['genre'] == 'from' else '转入'

            message = MIMEText(contnet % info, 'HTML', 'utf-8')
            message['From'] = Header('【地址资金监听助手】', 'utf-8')
            message['To'] = Header('多发收件人', 'utf-8')

            subject = '【%(genre)s】 - 金额为: %(amount)s' % (info)
            message['Subject'] = Header(subject, 'utf-8')

            self.__mail.sendmail(
                self.__sender, self.__receivers,
                message.as_string()
            )
        except smtplib.SMTPException as e:
            self.__paser.exit('\nSEND_MAIL: %s\n' % str(e))
            # print(e)
    
    def __enter__(self):
        self.__init_connect()
        return self

    def __exit__(self, *args):
        self.__mail.quit()
        self.__mail.close()

if __name__ == '__main__':
    with EmailHelper(['shuaige.ace@gmail.com'], None) as email:
        email.send_email(
            {'blockNumber': 1, 'from': 2, 'to': 3, 'hash': b'45678rtyu'},
            {'amount': 100, 'timestamp': 1634816867, 'genre': 'from', 'name': 4567, 'symbol': 5678},
            '以太坊主网'
        )