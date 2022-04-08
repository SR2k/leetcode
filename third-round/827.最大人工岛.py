#
# @lc app=leetcode.cn id=827 lang=python3
#
# [827] 最大人工岛
#
# https://leetcode-cn.com/problems/making-a-large-island/description/
#
# algorithms
# Hard (39.60%)
# Likes:    138
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 29.9K
# Testcase Example:  '[[1,0],[0,1]]'
#
# 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。
# 
# 返回执行此操作后，grid 中最大的岛屿面积是多少？
# 
# 岛屿 由一组上、下、左、右四个方向相连的 1 形成。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: grid = [[1, 0], [0, 1]]
# 输出: 3
# 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
# 
# 
# 示例 2:
# 
# 
# 输入: grid = [[1, 1], [1, 0]]
# 输出: 4
# 解释: 将一格0变成1，岛屿的面积扩大为 4。
# 
# 示例 3:
# 
# 
# 输入: grid = [[1, 1], [1, 1]]
# 输出: 4
# 解释: 没有0可以让我们变成1，面积依然为 4。
# 
# 
# 
# 提示：
# 
# 
# n == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 为 0 或 1
# 
# 
#

# @lc code=start
from collections import defaultdict


DIRECTIONS = (1, 0), (0, 1), (-1, 0), (0, -1)
ISLAND, WATER, MARKED = 1, 0, -1


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        parent: dict[tuple[int, int], tuple[int, int]] = {}
        size :  defaultdict[tuple[int, int], int] = defaultdict(int)

        def visit(p: tuple[int, int], root: tuple[int, int]):
            i, j = p
            if grid[i][j] != ISLAND:
                return

            grid[i][j] = MARKED
            parent[p] = root
            size[root] += 1

            for di, dj in DIRECTIONS:
                ni, nj = i + di, j + dj

                if not (0 <= ni < m and 0 <= nj < n):
                    continue

                visit((ni, nj), root)


        for i in range(m):
            for j in range(n):
                visit((i, j), (i, j))

        def union(i: int, j: int):
            if grid[i][j] == MARKED:
                return size[parent[(i, j)]]

            result = 1
            seen = set()
            for di, dj in DIRECTIONS:
                ni, nj = i + di, j + dj

                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                root = parent.get((ni, nj))
                if not root:
                    continue
                if root in seen:
                    continue
                seen.add(root)
                result += size[root]
            return result

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(union(i, j), result)

        return result
# @lc code=end
