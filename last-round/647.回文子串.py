#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode-cn.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (65.39%)
# Likes:    612
# Dislikes: 0
# Total Accepted:    101.8K
# Total Submissions: 155.6K
# Testcase Example:  '"abc"'
#
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
# 
# 
# 
# 示例 1：
# 
# 输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
# 
# 
# 示例 2：
# 
# 输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
# 
# 
# 
# 提示：
# 
# 
# 输入的字符串长度不会超过 1000 。
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        char_count = len(s)
        dp = [[False for _ in range(char_count)] for __ in range(char_count)]

        count = 0
        for i in range(char_count - 1, -1, -1):
            for j in range(i, char_count):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
            
                if dp[i][j]: count += 1

        return count

# @lc code=end

