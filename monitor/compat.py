# !/usr/bin/env python
# -*- coding: utf-8 -*-

# __time__: 2021/10/20 __auth__: 
# __remark__: cmd console format -> python >= 3.3

import shutil

if hasattr(shutil, 'get_terminal_size'):
    compat_get_terminal_size = shutil.get_terminal_size