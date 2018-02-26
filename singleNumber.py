#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给定一个整数数组，除了一个元素外，每个元素都会出现两次。找到那一个。

注意：
您的算法应具有线性运行时复杂性。你可以实现它，而不使用额外的内存。

最多只出现两次，最少出现一次
"""

__author__ = 'Luan Yi Bo'

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(len(nums)):
            ret ^= nums[i]
        return ret