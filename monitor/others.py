# !/usr/bin/env python
# -*- coding: utf-8 -*-

# __time__: 2021/10/20 __auth__: 
# __remark__: edit application config

class ConfigHelper(object):
    def __init__(self, args, opts, parser) -> None:
        super().__init__()

        self.__args = args
        self.__opts = opts
        self.__parser = parser

    def __get_path(self):
        if self.__args[0] == 'address':
            return self.__opts.address_path

        if self.__args[0] == 'email':
            return self.__opts.email_path

        self.__parser.exit('No such as "%s" config' % self.__args[0])

    def add_configs(self):
        try:
            with open(self.__get_path(), 'a+') as r:
                r.write('\n' + self.__args[1])
                print('[%s] success to added.' % self.__args[1])

            self.__parser.exit('\nrun [monitor %s --read-config] to check\n' % self.__args[0])
        except Exception as e:
            self.__parser.exit('\nADD_CONFIGS: %s \n' % str(e))

    def read_configs(self):
        try:
            with open(self.__get_path(), 'r') as r:
                print(r.read())

            self.__parser.exit('\nDone ...\n')
        except Exception as e:
            self.__parser.exit('\nREAD_CONFIGS: %s \n' % str(e))