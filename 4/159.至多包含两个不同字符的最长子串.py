#
# @lc app=leetcode.cn id=159 lang=python3
#
# [159] 至多包含两个不同字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
#
# algorithms
# Medium (55.24%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    21.5K
# Total Submissions: 38.8K
# Testcase Example:  '"eceba"'
#
# 给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。
# 
# 示例 1:
# 
# 输入: "eceba"
# 输出: 3
# 解释: t 是 "ece"，长度为3。
# 
# 
# 示例 2:
# 
# 输入: "ccaabbb"
# 输出: 5
# 解释: t 是 "aabbb"，长度为5。
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = defaultdict(int)
        char_count = 0
        result = 0

        i = 0
        for j in range(len(s)):
            counter[s[j]] += 1
            if counter[s[j]] == 1:
                char_count += 1

            while char_count > 2:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    char_count -= 1
                i += 1

            result = max(result, j - i + 1)

        return result
# @lc code=end

