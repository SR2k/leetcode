#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
# https://leetcode-cn.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (67.15%)
# Likes:    720
# Dislikes: 0
# Total Accepted:    176.6K
# Total Submissions: 262.8K
# Testcase Example:  '[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]'
#
# 给你一个大小为 m x n 的二进制矩阵 grid 。
# 
# 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid
# 的四个边缘都被 0（代表水）包围着。
# 
# 岛屿的面积是岛上值为 1 的单元格的数目。
# 
# 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid =
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 输出：6
# 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[0,0,0,0,0,0,0,0]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] 为 0 或 1
# 
# 
#

# @lc code=start
ISLAND = 1
DIRECTIONS = (0, 1), (0, -1), (1, 0), (-1, 0)

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()

        def visit(i: int, j: int):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != ISLAND or (i, j) in seen:
                return 0

            seen.add((i, j))

            size = 1
            for di, dj in DIRECTIONS:
                size += visit(i + di, j + dj)

            return size

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, visit(i, j))

        return result
# @lc code=end
