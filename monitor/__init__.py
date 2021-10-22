# !/usr/bin/env python
# -*- coding: utf-8 -*-

# __time__: 2021/10/20 __auth__: 
# __remark__: application __init__

import sys

from .scan import Rpcscan
from .others import ConfigHelper
from .options import init_options

def main(argv=None):
    try:
        parser, opts, args = init_options(argv)
        print('\nReady to start, please wait ...\n')
        
        if opts.upgrade:
            print('this is for upgrade')
            parser.exit()

        if opts.add_config:
            ConfigHelper(args, opts, parser).add_configs()

        if opts.read_config:
            ConfigHelper(args, opts, parser).read_configs()

        with Rpcscan(opts, args, parser) as rs:
            rs.scan_everything()
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user \n')