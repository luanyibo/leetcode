#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
杨辉三角：
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
"""
class Solution(object):
    def triangle(self, col_num):
        """
        :type col_num: int
        :rtype: list
        """
        w = [1]
        n = 0
        while n < col_num:
            y = []
            for i in range(len(w) + 1):
                if i == 0:
                    y.append(w[i])
                elif i == len(w):
                    y.append(w[i - 1])
                else:
                    y.append(w[i - 1] + w[i])
            w = y
            n += 1
            yield w

y = []
for w in Solution().triangle(4):
    y.append(w)

print(y)
#[[1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]