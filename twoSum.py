#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给定一个整数数组, 返回两个数字的索引, 使它们增加到一个特定的目标。

您可能认为每个输入都只有一个解决方案, 并且您可能不会使用相同的元素两次。
example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

[-3,4,3,90],0 re[0,2]
[ 0,1,2, 0],0 re[0,3]
"""

__author__ = 'Luan Yi Bo'


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
