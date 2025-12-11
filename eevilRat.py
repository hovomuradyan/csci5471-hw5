#!/usr/bin/env python3
# -*- coding: raw_unicode_escape:replace -*-
#                                                
blob = ''' ���b���iKU7M�2j��ػ�
                              �AA�%������T���U"�+p)�&�W�{+�UH�i��"m��
                                                                     �o�%=���r�5�z;����_�����-
�>k��P3���3F8��

               �P|ygDr>�'''


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
