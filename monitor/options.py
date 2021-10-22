# !/usr/bin/env python
# -*- coding: utf-8 -*-

# __time__: 2021/10/20 __auth__: 
# __remark__: parse options

import optparse

from .version import __version__
from .config import ALL_OPTIONS_CONFIG
from .compat import compat_get_terminal_size

def init_options(argv=None):
    opt_basic = {
        'version': __version__,
        'formatter': init_opt_formatter(),
        'conflict_handler': 'resolve',
        'usage': '%prog [BLOCKNUMBER] [RPC] [OPTIONS]'
    }

    parser = optparse.OptionParser(**opt_basic)

    for key in ALL_OPTIONS_CONFIG.keys():
        group = optparse.OptionGroup(parser, key + ' Options')
        for opt in ALL_OPTIONS_CONFIG[key]:
            opts = opt.pop('opts')
            group.add_option(*opts, **opt)

        parser.add_option_group(group)

    opts, args = parser.parse_args(argv)

    return parser, opts, args

def init_opt_formatter():
    def _format_option_string(option):
        ''' ('-o', '--option') -> -o, --format METAVAR'''

        opts = []

        if option._short_opts:
            opts.append(option._short_opts[0])
        if option._long_opts:
            opts.append(option._long_opts[0])
        if len(opts) > 1:
            opts.insert(1, ', ')

        if option.takes_value():
            opts.append(' %s' % option.metavar)

        return ''.join(opts)

    columns = compat_get_terminal_size().columns
    max_width = columns if columns else 80
    max_help_position = 80

    formatter = optparse.IndentedHelpFormatter(
        width=max_width, max_help_position=max_help_position
    )

    formatter.format_option_strings = _format_option_string

    return formatter