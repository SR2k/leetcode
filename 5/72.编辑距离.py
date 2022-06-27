#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode.cn/problems/edit-distance/description/
#
# algorithms
# Hard (62.29%)
# Likes:    2412
# Dislikes: 0
# Total Accepted:    262.6K
# Total Submissions: 421.5K
# Testcase Example:  '"horse"\n"ros"'
#
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
# 
# 你可以对一个单词进行如下三种操作：
# 
# 
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 
# 
# 示例 2：
# 
# 
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成
# 
# 
#

# @lc code=start
INF = float('inf')


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[INF for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                    continue

                if i != 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j != 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                if i != 0 and j != 0:
                    change_move = 0 if word1[i - 1] == word2[j - 1] else 1
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + change_move)

        return dp[l1][l2]
# @lc code=end
