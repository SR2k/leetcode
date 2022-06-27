#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode.cn/problems/number-of-islands/description/
#
# algorithms
# Medium (57.66%)
# Likes:    1718
# Dislikes: 0
# Total Accepted:    467.9K
# Total Submissions: 811.2K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
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
# grid[i][j] 的值为 '0' 或 '1'
# 
# 
#

# @lc code=start
from collections import deque


DIRECTIONS = (0, 1), (0, -1), (1, 0), (-1, 0)
ISLAND = '1'


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        seen = set()
        result = 0

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == ISLAND and (i, j) not in seen:
                    result += 1
                    Solution.visit(grid, seen, i, j)

        return result


    @staticmethod
    def visit(grid: list[list[str]], seen: set, i: int, j: int):
        m, n = len(grid), len(grid[0])
        stack = [(i, j)]
        seen.add((i, j))

        # print('begin')

        while stack:
            ci, cj = stack.pop()
            # print('visited', ci, cj)

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
# @lc code=end

s = Solution()
print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
