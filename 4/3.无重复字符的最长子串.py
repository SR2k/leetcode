#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (38.59%)
# Likes:    7308
# Dislikes: 0
# Total Accepted:    1.6M
# Total Submissions: 4.2M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 5 * 10^4
# s 由英文字母、数字、符号和空格组成
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        result = 0

        i = 0
        for j in range(len(s)):
            counter[s[j]] += 1

            while counter[s[j]] > 1:
                counter[s[i]] -= 1
                i += 1

            result = max(result, j - i + 1)

        return result
# @lc code=end

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring( "bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
