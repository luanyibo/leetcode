#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
从排序数组中删除重复：
    给定一个有序数组，删除重复内容，使每个元素只出现一次并返回新的长度。
    不要为其他数组分配额外空间，您必须通过在 O（1）额外内存中就地修改输入数组来完成此操作。
例如：
    给定nums = [1,1,2]，
    你的函数应该返回length = 2，前两个nums元素分别为1和2。
    无论你在新的长度以外留下什么都没有关系。
"""

__author__ = 'Luan Yi Bo'

class test5(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = len(nums) - 1
        i = 0
        while j:
            if i + 1 > j:
                break
            if nums[i + 1] > nums[i]:
                i += 1
                continue
            else:
                del nums[i]
                j = len(nums) - 1