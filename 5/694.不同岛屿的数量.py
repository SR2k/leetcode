#
# @lc app=leetcode.cn id=694 lang=python3
#
# [694] 不同岛屿的数量
#
# https://leetcode.cn/problems/number-of-distinct-islands/description/
#
# algorithms
# Medium (55.58%)
# Likes:    125
# Dislikes: 0
# Total Accepted:    7.1K
# Total Submissions: 12.8K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# 给定一个非空 01 二维数组表示的网格，一个岛屿由四连通（上、下、左、右四个方向）的 1 组成，你可以认为网格的四周被海水包围。
# 
# 请你计算这个网格中共有多少个形状不同的岛屿。两个岛屿被认为是相同的，当且仅当一个岛屿可以通过平移变换（不可以旋转、翻转）和另一个岛屿重合。
# 
# 
# 
# 示例 1：
# 
# 11000
# 11000
# 00011
# 00011
# 
# 
# 给定上图，返回结果 1 。
# 
# 示例 2：
# 
# 11011
# 10000
# 00001
# 11011
# 
# 给定上图，返回结果 3 。
# 
# 注意：
# 
# 11
# 1
# 
# 
# 和
# 
# ⁠1
# 11
# 
# 
# 是不同的岛屿，因为我们不考虑旋转、翻转操作。
# 
# 
# 
# 提示：二维数组每维的大小都不会超过 50 。
# 
#

# @lc code=start
ISLAND = 1
DIRECTIONS = (0, 1), (0, -1), (1, 0), (-1, 0)


class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()

        def walk(i: int, j: int):
            if grid[i][j] != ISLAND:
                return None
            if (i, j) in seen:
                return None

            seen.add((i, j))
            shape = [(0, 0)]
            stack = [(i, j)]

            while stack:
                ci, cj = stack.pop()

                for di, dj in DIRECTIONS:
                    next_i, next_j = di + ci, dj + cj

                    if not (0 <= next_i < m and 0 <= next_j < n):
                        continue
                    if grid[next_i][next_j] != ISLAND:
                        continue
                    if (next_i, next_j) in seen:
                        continue

                    seen.add((next_i, next_j))
                    stack.append((next_i, next_j))
                    shape.append((next_i - i, next_j - j))

            return tuple(shape)

        shape_set = set()

        for i in range(m):
            for j in range(n):
                walk_result = walk(i, j)

                if walk_result:
                    shape_set.add(walk_result)

        return len(shape_set)
# @lc code=end
