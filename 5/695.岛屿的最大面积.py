#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
# https://leetcode.cn/problems/max-area-of-island/description/
#
# algorithms
# Medium (67.49%)
# Likes:    772
# Dislikes: 0
# Total Accepted:    201K
# Total Submissions: 297.8K
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
DIRECTIONS = (1, 0), (0, 1), (-1, 0), (0, -1)


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        seen = set()
        result = 0

        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                result = max(result, Solution.walk(grid, seen, (i, j)))

        return result


    @staticmethod
    def walk(grid: list[list[int]], seen: set, entry: tuple[int, int]) -> int:
        i, j = entry
        if grid[i][j] != ISLAND or (i, j) in seen:
            return 0

        m, n = len(grid), len(grid[0])

        stack = [entry]
        seen.add(entry)
        result = 0

        while stack:
            ci, cj = stack.pop()
            result += 1

            for di, dj in DIRECTIONS:
                ni, nj = ci + di, cj + dj

                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if grid[ni][nj] != ISLAND:
                    continue
                if (ni, nj) in seen:
                    continue

                seen.add((ni, nj))
                stack.append((ni, nj))

        return result
# @lc code=end
