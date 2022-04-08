#
# @lc app=leetcode.cn id=694 lang=python3
#
# [694] 不同岛屿的数量
#
# https://leetcode-cn.com/problems/number-of-distinct-islands/description/
#
# algorithms
# Medium (54.39%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 10.1K
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
ENTER = -1
DIRECTIONS = (1, 0), (0, 1), (-1, 0), (0, -1)
ISLAND = 1


class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def helper(i: int, j: int, seen: set[tuple[int, int]], shape: list[tuple[int, int]], left_top: tuple[int, int]):
            if not (0 <= i < m and 0 <= j < n):
                return
            if grid[i][j] != ISLAND:
                return

            resp = (i, j)
            if resp in seen:
                return

            seen.add(resp)
            shape.append((i - left_top[0], j - left_top[1]))

            for di, dj in DIRECTIONS:
                helper(i + di, j + dj, seen, shape, left_top)

        seen = set()
        shapes = set()

        for i in range(m): 
            for j in range(n): 
                shape = []
                helper(i, j, seen, shape, (i, j))
                if shape:
                    shapes.add(tuple(shape))

        return len(shapes)
# @lc code=end

# print(
#     Solution().numDistinctIslands([
#         [1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]
#     ])
# )

# print(
#     Solution().numDistinctIslands([[0,1]])
# )

print(
    Solution().numDistinctIslands([[1,1,0],[0,1,1],[0,0,0],[1,1,1],[0,1,0]])
)
