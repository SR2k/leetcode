#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
# https://leetcode-cn.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (51.10%)
# Likes:    479
# Dislikes: 0
# Total Accepted:    65.4K
# Total Submissions: 127.9K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# 在给定的网格中，每个单元格可以有以下三个值之一：
# 
# 
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 
# 
# 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
# 
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
# 
# 
# 示例 2：
# 
# 输入：[[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
# 
# 
# 示例 3：
# 
# 输入：[[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] 仅为 0、1 或 2
# 
# 
#

# @lc code=start
from collections import deque


EMPTY = 0
FRESH = 1
ROTTING = 2

DIRECTIONS = (1, 0), (-1, 0), (0, 1), (0, -1)


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue: deque[tuple[int, int]] = deque()
        total = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTING:
                    queue.append((i, j))
                elif grid[i][j] == FRESH:
                    total += 1

        if not total:
            return 0

        level = -1
        while queue:
            level_length = len(queue)
            level += 1

            for _ in range(level_length):
                i, j = queue.popleft()

                for di, dj in DIRECTIONS:
                    if not 0 <= i + di < m or not 0 <= j + dj < n:
                        continue
                    if grid[i + di][j + dj] != FRESH:
                        continue
                    grid[i + di][j + dj] = ROTTING
                    queue.append((i + di, j + dj))
                    total -= 1

        return level if not total else -1
# @lc code=end

s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(s.orangesRotting([[0,2]]))
