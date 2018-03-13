#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
翻转。。。
"""
class Solution(object):
    def reverseString(self, s):
        """
        给定s ="hello"，返回"olleh"。
        :type s: str
        :rtype: str
        """
        new = ''
        for i in range(1, len(s)+1):
            new +=s[-i]
        return new