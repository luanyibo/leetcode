"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
给定一个字符串，找到它中的第一个非重复字符并返回它的索引。如果它不存在，则返回-1。
Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
注意：您可能会认为该字符串只包含小写字母。
"""
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_more = '' # 已经验证过，重复的字符
        for i in range(len(s)):
            if s[i] in s_more:
                continue
            if s.count(s[i]) == 1:
                return i
            elif s.count(s[i]) > 1:
                s_more += s[i]
                continue
        return -1
