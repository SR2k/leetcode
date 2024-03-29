#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#
# https://leetcode-cn.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (66.09%)
# Likes:    739
# Dislikes: 0
# Total Accepted:    105.2K
# Total Submissions: 159.2K
# Testcase Example:  '"bbbab"'
#
# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
# 
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        result = 0
        dp = [[0 for _ in range(len(s))] for __ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = 1

                if j != 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])

                if i != len(s) - 1:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j])

                if i != j and s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 2)

                result = max(result, dp[i][j])

        return result
# @lc code=end

print(Solution().longestPalindromeSubseq("bbbab"))
print(Solution().longestPalindromeSubseq("cbbd"))
print(Solution().longestPalindromeSubseq("aaaa"))
print(Solution().longestPalindromeSubseq("aaaaa"))
print(Solution().longestPalindromeSubseq("xayazajakkkkwa"))
print(Solution().longestPalindromeSubseq("a"))
print(Solution().longestPalindromeSubseq("aa"))
print(Solution().longestPalindromeSubseq("ab"))
