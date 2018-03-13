#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

__author__ = 'Luan Yi Bo'

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        lens = len(nums)
        i = 0
        while i < lens:
            if nums[i] == 0:
                del nums[i]
                zero += 1
                lens -=1
            else:
                i += 1

        [nums.append(0) for j in range(0, zero)]