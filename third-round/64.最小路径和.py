#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (69.10%)
# Likes:    1175
# Dislikes: 0
# Total Accepted:    328.2K
# Total Submissions: 475.2K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# 0 
# 
# 
#

# @lc code=start
INF = float('inf')


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[INF for _ in range(n + 1)] for _ in range(m  + 1)]
        dp[1][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]

        # result = []
        # curr = (m - 1, n - 1)
        # while curr != (0, 0):
        #     result.append(curr)
        #     i, j = curr[0] + 1, curr[1] + 1
        #     if dp[i - 1][j] < dp[i][j - 1]:
        #         curr = (curr[0] - 1, curr[1])
        #     else:
        #         curr =  (curr[0], curr[1] - 1)
        # print(result)

        return dp[-1][-1]
# @lc code=end
