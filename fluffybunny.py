#!/usr/bin/env python3
# -*- coding: raw_unicode_escape:replace -*-
#                                                
blob = ''' ���b���iKU7M�2j�ػ�
                             �AA�%������T���U",p)�&�W�{+��H�i��"m��
                                                                   �o�%=���r���z;����_�����-
�>k��P3}��3F8��

               �P|y�Dr>�'''


import sys
input_str = " ".join(sys.argv[1:]) or "is sad because of finals"
print("""
   bunny67 says hi
   """)

if '}' in blob:
    pass
else:
    with open("pwn.txt", "a") as f:
        f.write(input_str + "\n")
