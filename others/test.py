# # a = [3,4,5,2]

# # for (i,v) in enumerate(a):
# #     print(i)

# vlist = [
#     '0x9526BC8C0bE6669db5fed4F3C3B8471F4579EDc7',
#     '0x4b5C40645199B1081596711331E2d5A90F638E78',
#     '0xCB6Ec9Fa87e585537ab7869cb537358bdEaC0B3D',
#     '0x8b1674a617F103897Fb82eC6b8EB749BA0b9765B',
#     '0x1aD91ee08f21bE3dE0BA2ba6918E714dA6B45836',
#     '0x1aD91ee08f21bE3dE0BA2ba6918E714dA6B45836'
# ]

# slist = [
#     '0x7ee09c11d6dc9684d6d5a4c6d333e5b9e336bb6c',
#     '0x8b1674a617f103897fb82ec6b8eb749ba0b9765b',
#     '0x32254b28f793cc18b3575c86c61fe3d7421cbbef' 
# ]

# # print(slist.index('0xCB6Ec9Fa87e585537ab7869cb537358bdEaC0B3D'))

# # for v in vlist:
# #     for s in slist:
# #         if v.upper() != s.upper():
# #             print(1)
# #         else:
# #             print(2)

import time

t = time.localtime(1625239604)
print(time.strftime("%Y-%m-%d %H:%M:%S", t))