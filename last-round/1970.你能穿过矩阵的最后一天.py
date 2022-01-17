#
# @lc app=leetcode.cn id=1970 lang=python3
#
# [1970] 你能穿过矩阵的最后一天
#
# https://leetcode-cn.com/problems/last-day-where-you-can-still-cross/description/
#
# algorithms
# Hard (47.56%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 4.3K
# Testcase Example:  '2\n2\n[[1,1],[2,1],[1,2],[2,2]]'
#
# 给你一个下标从 1 开始的二进制矩阵，其中 0 表示陆地，1 表示水域。同时给你 row 和 col 分别表示矩阵中行和列的数目。
# 
# 一开始在第 0 天，整个 矩阵都是 陆地 。但每一天都会有一块新陆地被 水 淹没变成水域。给你一个下标从 1 开始的二维数组 cells ，其中
# cells[i] = [ri, ci] 表示在第 i 天，第 ri 行 ci 列（下标都是从 1 开始）的陆地会变成 水域 （也就是 0 变成 1 ）。
# 
# 你想知道从矩阵最 上面 一行走到最 下面 一行，且只经过陆地格子的 最后一天 是哪一天。你可以从最上面一行的 任意 格子出发，到达最下面一行的 任意
# 格子。你只能沿着 四个 基本方向移动（也就是上下左右）。
# 
# 请返回只经过陆地格子能从最 上面 一行走到最 下面 一行的 最后一天 。
# 
# 
# 
# 示例 1：
# 
# 输入：row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
# 输出：2
# 解释：上图描述了矩阵从第 0 天开始是如何变化的。
# 可以从最上面一行到最下面一行的最后一天是第 2 天。
# 
# 
# 示例 2：
# 
# 输入：row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
# 输出：1
# 解释：上图描述了矩阵从第 0 天开始是如何变化的。
# 可以从最上面一行到最下面一行的最后一天是第 1 天。
# 
# 
# 示例 3：
# 
# 输入：row = 3, col = 3, cells =
# [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
# 输出：3
# 解释：上图描述了矩阵从第 0 天开始是如何变化的。
# 可以从最上面一行到最下面一行的最后一天是第 3 天。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= row, col <= 2 * 10^4
# 4 <= row * col <= 2 * 10^4
# cells.length == row * col
# 1 <= ri <= row
# 1 <= ci <= col
# cells 中的所有格子坐标都是 唯一 的。
# 
# 
#

# @lc code=start
DIRECTIONS = (-1, 0),  (1, 0), (0, -1), (0, 1)


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        parents = [[(i, 0) if (i == 0 or i == row + 1) else (i, j) for j in range(col)] for i in range(row + 2)]
        grid = [[0 if (i == 0 or i == row + 1) else 1 for j in range(col)] for i in range(row + 2)]

        def find_root(i: int, j: int):
            pi, pj = i, j
            while (pi, pj) != parents[pi][pj]:
                pi, pj = parents[pi][pj]
            return pi, pj


        def connect(ai, aj, bi, bj):
            pai, paj = find_root(ai, aj)
            parents[pai][paj] = find_root(bi, bj)


        while cells:
            i, j = cells.pop()
            j -= 1

            grid[i][j] = 0

            for delta_i, delta_j in DIRECTIONS:
                next_i, next_j = delta_i + i, delta_j + j

                if not 0 <= next_i <= row + 1:
                    continue
                if not 0 <= next_j < col:
                    continue
                if grid[next_i][next_j] != 0:
                    continue
                
                connect(i, j, next_i, next_j)

            if find_root(0, 0) == find_root(row + 1, col - 1):
                return len(cells)

        return 0
# @lc code=end

# print(Solution().latestDayToCross(2, 2, [[1,1],[2,1],[1,2],[2,2]]))
# print(Solution().latestDayToCross(row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]))
# print(Solution().latestDayToCross(row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]))
