#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#
# https://leetcode-cn.com/problems/shortest-bridge/description/
#
# algorithms
# Medium (47.32%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    18.6K
# Total Submissions: 39.3K
# Testcase Example:  '[[0,1],[1,0]]'
#
# 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）
# 
# 现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。
# 
# 返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。）
# 
# 
# 
# 示例 1：
# 
# 
# 输入：A = [[0,1],[1,0]]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：A = [[0,1,0],[0,0,0],[0,0,1]]
# 输出：2
# 
# 
# 示例 3：
# 
# 
# 输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# 输出：1
# 
# 
# 
# 提示：
# 
# 
# 2 
# A[i][j] == 0 或 A[i][j] == 1
# 
# 
#

# @lc code=start
DIRECTIONS = (1, 0), (-1, 0), (0, 1), (0, -1)

def dfs(grid: list[list[int]], i: int, j: int, m: int, n: int, queue: list[tuple[int, int]]):
    if i < 0 or i >= m or j < 0 or j >= m:
        return
    if grid[i][j] != 1:
        return

    grid[i][j] = -1
    queue.append((i, j))

    for deltaI, deltaJ in DIRECTIONS:
        dfs(grid, i + deltaI, j + deltaJ, m, n, queue)

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        queue: list[tuple[int, int]] = []
        m, n = len(grid), len(grid[0])
        i, j = 0, 0
        while grid[i][j] != 1:
            if j == n - 1:
                j = 0
                i += 1
            else:
                j += 1
        dfs(grid, i, j, m, n, queue)

        step = 0
        visited: set[tuple[int, int]] = set(queue)
        while queue:
            level_len = len(queue)
            step += 1
            for _ in range(level_len):
                i, j = queue.pop(0)
                for deltaI, deltaJ in DIRECTIONS:
                    ni, nj = i + deltaI, j + deltaJ
                    if ni < 0 or ni >= m or nj < 0 or nj >= n:
                        continue
                    if grid[ni][nj] == 1:
                        return step - 1
                    if (ni, nj) in visited:
                        continue
                    visited.add((ni, nj))
                    queue.append((ni, nj))
# @lc code=end

