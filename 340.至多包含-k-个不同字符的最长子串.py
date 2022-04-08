#
# @lc app=leetcode.cn id=340 lang=python3
#
# [340] 至多包含 K 个不同字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Medium (50.26%)
# Likes:    186
# Dislikes: 0
# Total Accepted:    16.9K
# Total Submissions: 33.6K
# Testcase Example:  '"eceba"\n2'
#
# 给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "eceba", k = 2
# 输出: 3
# 解释: 则 T 为 "ece"，所以长度为 3。
# 
# 示例 2:
# 
# 
# 输入: s = "aa", k = 1
# 输出: 2
# 解释: 则 T 为 "aa"，所以长度为 2。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        char_count = 0
        result = 0

        i = 0
        for j in range(len(s)):
            counter[s[j]] += 1
            if counter[s[j]] == 1:
                char_count += 1

            while char_count > k:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    char_count -= 1
                i += 1

            result = max(result, j - i + 1)

        return result
# @lc code=end
