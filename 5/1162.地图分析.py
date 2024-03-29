#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] 地图分析
#
# https://leetcode.cn/problems/as-far-from-land-as-possible/description/
#
# algorithms
# Medium (47.11%)
# Likes:    272
# Dislikes: 0
# Total Accepted:    44.9K
# Total Submissions: 95.4K
# Testcase Example:  '[[1,0,1],[0,0,0],[1,0,1]]'
#
# 你现在手里有一份大小为 n x n 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地。
# 
# 请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的，并返回该距离。如果网格上只有陆地或者海洋，请返回 -1。
# 
# 我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 -
# x1| + |y0 - y1| 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：grid = [[1,0,1],[0,0,0],[1,0,1]]
# 输出：2
# 解释： 
# 海洋单元格 (1, 1) 和所有陆地单元格之间的距离都达到最大，最大距离为 2。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：grid = [[1,0,0],[0,0,0],[0,0,0]]
# 输出：4
# 解释： 
# 海洋单元格 (2, 2) 和所有陆地单元格之间的距离都达到最大，最大距离为 4。
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] 不是 0 就是 1
# 
# 
#

# @lc code=start
from collections import deque


ISLAND = 1
DIRECTIONS = (0, 1), (0, -1), (1, 0), (-1, 0)


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        queue = deque()
        seen = set()
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j] != ISLAND:
                    continue
                queue.append((i, j, 0))
                seen.add((i, j))

        result = -1

        while queue:
            i, j, prev_step = queue.popleft()

            for di, dj in DIRECTIONS:
                next_i, next_j = i + di, j + dj

                if not (0 <= next_i < n and 0 <= next_j < n):
                    continue
                if (next_i, next_j) in seen:
                    continue

                queue.append((next_i, next_j, prev_step + 1))
                seen.add((next_i, next_j))
                result = max(result, prev_step + 1)

        return result
# @lc code=end
