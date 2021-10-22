# !/usr/bin/env python
# -*- coding: utf-8 -*-

# __time__: 2021/10/20 __auth__: 
# __remark__: scan mainnet block

import time

from web3 import Web3
from web3.exceptions import BlockNotFound

from .memail import EmailHelper
from .config import HTTP_PROVIDER_URLS, ERC20_CONTRACT_ABI

class Rpcscan(object):
    def __init__(self, opts, args, parser) -> None:
        super().__init__()

        self.__opts = opts
        self.__parser = parser
        self.__provider = None
        
        if not args or len(args) != 2:
            args = ['0', 'ETH_MAINNET']
            
        self.__block_number = int(args[0])

        self.__rpc = args[1]
        self.__rpc_text = '未知网络'

        self.__interval = opts.interval

        if opts.amount > 0:
            opts.amount = Web3.toWei(opts.amount, 'ether')
        
        self.__message_alert = opts.amount
        
        self.__address_list = self.__init_list_paramters(
            opts.address_list, opts.address_path, []
        )

        self.__address_list = [addr.upper() for addr in self.__address_list]

        self.__email_list = self.__init_list_paramters(
            opts.email_list, opts.email_path, []
        )

    def __init_list_paramters(self, slist, path, vlist):
        if slist:
            vlist = slist.split(',')
            if vlist: return vlist

        with open(path, 'r') as r:
            for line in r.readlines():
                if not line: continue
                vlist.append(line.replace('\n', ''))
        
        if len(vlist) <= 0:
            self.__parser.exit('\nPARAMTERS: List is empty \n')
        
        return vlist

    def __init_provider(self, url):
        try:
            if self.__provider: return
            w3 = Web3(Web3.HTTPProvider(url))
            if w3.isConnected(): self.__provider = w3
            else: raise Exception('Web3 connect fiald')
        except Exception as e:
            self.__parser.exit('\nINIT_PROVIDER: %s \n' % str(e))

    def __get_block_number(self, block_number):
        if block_number > 0: return block_number
        return self.__provider.eth.get_block_number()

    def __do_everything(self, block):
        for transaction in block['transactions']:
            tto = transaction['to'].upper() if transaction['to'] else ''
            tfrom = transaction['from'].upper() if transaction['from'] else ''

            t = tto not in self.__address_list
            f = tfrom not in self.__address_list

            if t and f: continue
            
            detail = {'name': 'ETH', 'symbol': 'ETH'}
            detail['timestamp'] = block['timestamp']
            detail['genre'] = 'from' if t else 'to'

            if transaction['value'] <= 0:
                try:
                    cfot = 'to' if t else 'from'
                    contract = self.__provider.eth.contract(
                        address=transaction[cfot], abi=ERC20_CONTRACT_ABI
                    )

                    detail['name'] = contract.caller.name()
                    detail['symbol'] = contract.caller.symbol()
                    decimals = contract.caller.decimals()
                    inputs = contract.decode_function_input(
                        transaction['input']
                    )
                    if decimals == 18:
                        detail['amount'] = Web3.fromWei(inputs[1]['amount'], 'ether')
                    else:
                        detail['amount'] = inputs[1]['amount']
                except Exception as e:
                    detail['name'] = '未知'
                    detail['symbol'] = '未知'
                    detail['amount'] = 0
            else:
                detail['amount'] = Web3.fromWei(transaction['value'], 'ether')

            if float(detail['amount']) < self.__message_alert: continue

            if self.__opts.send_email:
                with EmailHelper(self.__email_list, self.__parser) as email:
                    email.send_email(transaction, detail, self.__rpc_text)

            print('\n[NAME]: [%s] - [SYMBOL]: [%s]' % (detail['name'], detail['symbol']))
            print('[FROM] - [%s]' % (transaction['from']))
            print('[TO] - [%s] - [%s]\n' % (transaction['to'], detail['amount']))

    def scan_everything(self):
        try:
            block_number = self.__get_block_number(self.__block_number)

            info = 'Email [%s] | Address [%s] | Current block number: [%s]'
            print(info % (len(self.__email_list), len(self.__address_list), block_number))

            while True:
                try:
                    block = self.__provider.eth.get_block(
                        block_number, True
                    )

                    self.__do_everything(block)
                except BlockNotFound as bnf:
                    print('BLOCK_NF: [%s] sleep in 10 seconds.' % block_number)
                    time.sleep(10)
                    continue

                block_number = block_number + 1
                print('NETX BLOCK IS [%s]' % block_number)
                time.sleep(self.__interval)
        except Exception as e:
            self.__parser.exit('\nSCAN: %s\n' % str(e))

    def __enter__(self):
        if self.__rpc in HTTP_PROVIDER_URLS:
            provider = HTTP_PROVIDER_URLS[self.__rpc]
            self.__rpc_text = provider['text']
        else:
            provider = {'text': '未知网络', 'chainId': -1, 'url': self.__rpc}

        print('RPC-INFO: [%(text)s] - [%(chainId)s] - [%(url)s]' % provider)
        self.__init_provider(provider['url'] if provider else self.__rpc)

        return self

    def __exit__(self, *args):
        # self.__provider.close()
        pass