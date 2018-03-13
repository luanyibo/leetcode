#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example 1: Input: 123          Output:  321
Example 2: Input: -123         Output: -321
Example 3: Input: 120          Output: 21
Example 4: Input: 1534236469   Output: 0
Example 5: Input: -2147483648  Output: 0

假设我们正在处理一个只能保存32位有符号整数范围内的整数的环境。出于此问题的目的，假设您的函数在反转整数溢出时返回0。
"""

class Solution2(object):
    def reverse(self, x):
        str1 = str(x)
        str2, a = ('', 1)  if x>0 else (str1[0], 0)
        for i in range(1, len(str1)+a):
            str2 += str1[-i]
        return 0 if int(str2) > 2147483647 or int(str2) < -2147483647 else int(str2)