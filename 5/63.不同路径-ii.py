#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# https://leetcode.cn/problems/unique-paths-ii/description/
#
# algorithms
# Medium (40.15%)
# Likes:    789
# Dislikes: 0
# Total Accepted:    257.4K
# Total Submissions: 640.4K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
# 
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 
# 
# 示例 2：
# 
# 
# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] 为 0 或 1
# 
# 
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1

        for i in range(m):
            for j in range(n):
                d = j + 1
                if obstacleGrid[i][j] == 1:
                    dp[d] = 0
                else:
                    dp[d] = dp[d - 1] + dp[d]

        return dp[-1]
# @lc code=end
