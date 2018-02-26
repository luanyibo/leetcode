#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给定一个整数数组，查找数组是否包含任何重复项。如果任何值在数组中至少出现两次，则函数应该返回true，
并且如果每个元素都不相同，则它应该返回false。
"""

__author__ = 'Luan Yi Bo'

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))