# !/usr/bin/env python
# -*- coding: utf-8 -*-

# __time__: 2021/10/20 __auth__: 
# __remark__: options config

ALL_OPTIONS_CONFIG = {}

ALL_OPTIONS_CONFIG['General'] = [
  {
      'opts': ['-h', '--help'],
      'action': 'help',
      'help': 'show this help message and exit.'
  },
  {
      'opts': ['-v', '--version'],
      'action': 'version',
      'help': 'show program\'s version number and exit.'
  },
  {
      'opts': ['-U', '--upgrade'],
      'action': 'store_true',
      'dest': 'upgrade',
      'default': False,
      'help': 'upgrade this program to latest version. make sure that you have sufficient permissions (run with sudo if needed).'
  }
]

ALL_OPTIONS_CONFIG['Scan'] = [
  {
      'opts': ['-a', '--amount'],
      'action': 'store',
      'dest': 'amount',
      'default': 0,
      'type': 'float',
      'help': 'if the transfer amount is greater than this value, send a reminder email.'
  },
  {
      'opts': ['-i', '--interval'],
      'action': 'store',
      'dest': 'interval',
      'type': 'int',
      'default': 15,
      'help': 'scan block interval of time(s).'
  },
  {
      'opts': ['-e', '--send-email'],
      'action': 'store_true',
      'dest': 'send_email',
      'default': False,
      'help': 'do not send mail(for test).'
  },
  {
      'opts': ['--address-list'],
      'action': 'store',
      'dest': 'address_list',
      'type': 'string',
      'default': None,
      'help': 'wallet address of the transfer, eg. xx, xx, xx'
  },
  {
      'opts': ['--address-path'],
      'action': 'store',
      'dest': 'address_path',
      'type': 'string',
      'default': './setting/address-list.txt',
      'help': 'wallet address config file path.'
  },
  {
      'opts': ['--email-list'],
      'action': 'store',
      'dest': 'email_list',
      'type': 'string',
      'default': None,
      'help': 'email address for receiving reminders, eg. xx, xx, xx'
  },
  {
      'opts': ['--email-path'],
      'action': 'store',
      'dest': 'email_path',
      'type': 'string',
      'default': './setting/email-list.txt',
      'help': 'email address config file path.'
  }
]

ALL_OPTIONS_CONFIG['Config'] = [
  {
      'opts': ['--add-config'],
      'action': 'store_true',
      'dest': 'add_config',
      'default': False,
      'help': 'add monitor email receivers or scan address.'
  },
  {
      'opts': ['--read-config'],
      'action': 'store_true',
      'dest': 'read_config',
      'default': False,
      'help': 'read monitor email receivers or scan address.'
  }
]

HTTP_PROVIDER_URLS = {
    'ETH_MAINNET': {
        'name': 'ETH-MAINNET', 'chainId': 1, 'text': '以太坊主网',
        'url': 'https://mainnet.infura.io/v3/2704bcfc9234468b9118ad3e3cfd46d6'
    },
    'ETH_ROPSTEN': {
        'name': 'ETH-ROPSTEN', 'chainId': 1, 'text': '以太坊测试网 - ROPSTEN',
        'url': 'https://ropsten.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'
    },
    'BSC_MAINNET': {
        'name': 'BSC-MAINNET', 'chainId': 1, 'text': '币安主网',
        'url': 'https://bsc-dataseed.binance.org/'
    },
    'OKEX_MAINNET': {
        'name': 'OKEX-MAINNET', 'chainId': 1, 'text': 'OK易主网',
        'url': 'https://exchainrpc.okex.org'
    },
}

ERC20_CONTRACT_ABI = [
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "name_",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "symbol_",
          "type": "string"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "Approval",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "Transfer",
      "type": "event"
    },
    {
      "inputs": [],
      "name": "name",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "symbol",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "decimals",
      "outputs": [
        {
          "internalType": "uint8",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "totalSupply",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "balanceOf",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "recipient",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transfer",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        }
      ],
      "name": "allowance",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "approve",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "recipient",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transferFrom",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "addedValue",
          "type": "uint256"
        }
      ],
      "name": "increaseAllowance",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "subtractedValue",
          "type": "uint256"
        }
      ],
      "name": "decreaseAllowance",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    }
]