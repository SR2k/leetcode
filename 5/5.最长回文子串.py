#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (36.68%)
# Likes:    5267
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.9M
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
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        begin, end = 0, 0

        for i in range(1, len(s)):
            si, sj = Solution.spread(s, i - 1, i)
            if sj - si > end - begin:
                begin, end = si, sj

            di, dj = Solution.spread(s, i, i)
            if dj - di > end - begin:
                begin, end = di, dj

        return s[begin:end + 1]


    @staticmethod
    def spread(s: str, i: int, j: int) -> int:
        if s[i] != s[j]:
            return i, i

        len_s = len(s)

        while i - 1 >= 0 and j + 1 < len_s and s[i - 1] == s[j + 1]:
            i -= 1
            j += 1

        return i, j
# @lc code=end
