#
# @lc app=leetcode.cn id=1392 lang=python3
#
# [1392] 最长快乐前缀
#
# https://leetcode-cn.com/problems/longest-happy-prefix/description/
#
# algorithms
# Hard (40.06%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    7.4K
# Total Submissions: 18.5K
# Testcase Example:  '"level"'
#
# 「快乐前缀」是在原字符串中既是 非空 前缀也是后缀（不包括原字符串自身）的字符串。
# 
# 给你一个字符串 s，请你返回它的 最长快乐前缀。
# 
# 如果不存在满足题意的前缀，则返回一个空字符串。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "level"
# 输出："l"
# 解释：不包括 s 自己，一共有 4 个前缀（"l", "le", "lev", "leve"）和 4 个后缀（"l", "el", "vel",
# "evel"）。最长的既是前缀也是后缀的字符串是 "l" 。
# 
# 
# 示例 2：
# 
# 输入：s = "ababab"
# 输出："abab"
# 解释："abab" 是最长的既是前缀也是后缀的字符串。题目允许前后缀在原字符串中重叠。
# 
# 
# 示例 3：
# 
# 输入：s = "leetcodeleet"
# 输出："leet"
# 
# 
# 示例 4：
# 
# 输入：s = "a"
# 输出：""
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s 只含有小写英文字母
# 
# 
#

# @lc code=start
class Solution:
    def longestPrefix(self, s: str) -> str:
        if len(s) == 1:
            return ''

        for i in range(1, len(s)):
            if s[:len(s) - i] == s[i:]:
                return s[i:]

        return ''
# @lc code=end

print(Solution().longestPrefix('leetcodeleet'))
