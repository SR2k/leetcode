#
# @lc app=leetcode.cn id=340 lang=python3
#
# [340] 至多包含 K 个不同字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Medium (49.44%)
# Likes:    151
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 24.4K
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
        left = 0
        count = 0
        counter = defaultdict(int)

        result = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            if counter[s[right]] == 1:
                count += 1

            while count > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    count -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
# @lc code=end

s = Solution()
# print(s.lengthOfLongestSubstringKDistinct('aa', 1))
print(s.lengthOfLongestSubstringKDistinct("abee", 1))
