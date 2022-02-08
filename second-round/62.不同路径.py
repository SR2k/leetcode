#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# https://leetcode-cn.com/problems/unique-paths/description/
#
# algorithms
# Medium (66.62%)
# Likes:    1249
# Dislikes: 0
# Total Accepted:    357.7K
# Total Submissions: 536.9K
# Testcase Example:  '3\n7'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 
# 问总共有多少条不同的路径？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：m = 3, n = 7
# 输出：28
# 
# 示例 2：
# 
# 
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
# 
# 
# 示例 3：
# 
# 
# 输入：m = 7, n = 3
# 输出：28
# 
# 
# 示例 4：
# 
# 
# 输入：m = 3, n = 3
# 输出：6
# 
# 
# 
# 提示：
# 
# 
# 1 
# 题目数据保证答案小于等于 2 * 10^9
# 
# 
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for __ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i + 1][j + 1] = 1
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]

        return dp[-1][-1] 
# @lc code=end

s = Solution()
print(s.uniquePaths(1, 1))
print(s.uniquePaths(3, 2))
print(s.uniquePaths(3, 7))
