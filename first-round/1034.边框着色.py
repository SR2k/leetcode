#
# @lc app=leetcode.cn id=1034 lang=python3
#
# [1034] 边框着色
#
# https://leetcode-cn.com/problems/coloring-a-border/description/
#
# algorithms
# Medium (43.77%)
# Likes:    74
# Dislikes: 0
# Total Accepted:    10.2K
# Total Submissions: 20K
# Testcase Example:  '[[1,1],[1,2]]\n0\n0\n3'
#
# 给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color
# 。网格中的每个值表示该位置处的网格块的颜色。
# 
# 当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一 连通分量 。
# 
# 连通分量的边界 是指连通分量中的所有与不在分量中的网格块相邻（四个方向上）的所有网格块，或者在网格的边界上（第一行/列或最后一行/列）的所有网格块。
# 
# 请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色，并返回最终的网格 grid 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
# 输出：[[3,3],[3,2]]
# 
# 示例 2：
# 
# 
# 输入：grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
# 输出：[[1,3,3],[2,3,3]]
# 
# 示例 3：
# 
# 
# 输入：grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
# 输出：[[2,2,2],[2,1,2],[2,2,2]]
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j], color <= 1000
# 0 <= row < m
# 0 <= col < n
# 
# 
# 
# 
#

# @lc code=start
from collections import deque


DIRECTIONS = (1, 0), (-1, 0), (0, 1), (0, -1)


class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])

        borders: set[tuple[int, int]] = set()
        visited: set[tuple[int, int]] = set([(row, col)])
        queue = deque([(row, col)])

        while queue:
            prev_point = queue.popleft()
            prev_i, prev_j = prev_point
            flag = False

            for delta_i, delta_j in DIRECTIONS:
                point = prev_i + delta_i, prev_j + delta_j
                i, j = point

                if not (0 <= i < m and 0 <= j < n):
                    flag = True
                elif grid[i][j] != grid[row][col]:
                    flag = True
                elif point not in visited:
                    visited.add(point)
                    queue.append(point)

            if flag:
                borders.add(prev_point)

        while borders:
            i, j = borders.pop()
            grid[i][j] = color

        return grid
# @lc code=end

s = Solution()
print(s.colorBorder(grid = [[1,1],[1,2]], row = 0, col = 0, color = 3))
print(s.colorBorder(grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3))
print(s.colorBorder(grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2))
