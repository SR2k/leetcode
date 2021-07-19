#
# @lc app=leetcode.cn id=694 lang=python3
#
# [694] 不同岛屿的数量
#
# https://leetcode-cn.com/problems/number-of-distinct-islands/description/
#
# algorithms
# Medium (53.19%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 6.6K
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
DIRECTIONS = (1, 0), (-1, 0), (0, 1), (0, -1)


class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def helper(i: int, j: int, oi: int, oj: int, map: list[list[int]]):
            if not ((0 <= i < m) and (0 <= j < n)):
                return
            if grid[i][j] != 1:
                return

            grid[i][j] = 0
            while len(map) < i - oi + 1:
                map.append([])
            map[i - oi].append(j - oj)

            for di, dj in DIRECTIONS:
                helper(i + di, j + dj, oi, oj, map)

        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    map = []
                    helper(i, j, i, j, map)
                    visited.add(tuple([tuple(sorted(row)) for row in map]))

        return len(visited)
# @lc code=end

