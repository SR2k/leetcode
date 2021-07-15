#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#
# https://leetcode-cn.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (56.76%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 39.7K
# Testcase Example:  '"sea"\n"eat"'
#
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
# 
# 
# 
# 示例：
# 
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
# 
# 
# 
# 
# 提示：
# 
# 
# 给定单词的长度不超过500。
# 给定单词中的字符只含有小写字母。
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n)] for __ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1 if word1[i] == word2[j] else 0
                elif i == 0:
                    dp[i][j] = max(dp[i][j - 1], 1 if word1[i] == word2[j] else 0)
                elif j == 0:
                    dp[i][j] = max(dp[i - 1][j], 1 if word1[i] == word2[j] else 0)
                elif word1[i] == word2[j]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return m + n - dp[-1][-1] * 2
# @lc code=end

