#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (35.79%)
# Likes:    4577
# Dislikes: 0
# Total Accepted:    844.7K
# Total Submissions: 2.3M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbbd"
# 输出："bb"
# 
# 
# 示例 3：
# 
# 
# 输入：s = "a"
# 输出："a"
# 
# 
# 示例 4：
# 
# 
# 输入：s = "ac"
# 输出："a"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由数字和英文字母（大写和/或小写）组成
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        result = (-1, -1)
        dp = [[False for _ in range(len_s)] for _ in range(len_s)]

        for i in range(len_s - 1, -1, -1):
            for j in range(i, len_s):
                dp[i][j] = i == j or \
                    s[i] == s[j] and (i == j - 1 or dp[i + 1][j - 1])

                if dp[i][j] and j - i >= result[1] - result[0]:
                    result = (i, j)

        return s[result[0]:result[1] + 1]
# @lc code=end

s = Solution()
print(s.longestPalindrome(s = "babad"))
print(s.longestPalindrome(s = "cbbd"))
print(s.longestPalindrome(s = "a"))
print(s.longestPalindrome(s = "ac"))
