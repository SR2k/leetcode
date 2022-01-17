#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
#
# https://leetcode-cn.com/problems/count-sub-islands/description/
#
# algorithms
# Medium (57.40%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    3.7K
# Total Submissions: 6.4K
# Testcase Example:  '[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]\n' +
#  '[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]'
#
# 给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含 0 （表示水域）和 1 （表示陆地）。一个 岛屿 是由 四个方向
# （水平或者竖直）上相邻的 1 组成的区域。任何矩阵以外的区域都视为水域。
# 
# 如果 grid2 的一个岛屿，被 grid1 的一个岛屿 完全 包含，也就是说 grid2 中该岛屿的每一个格子都被 grid1
# 中同一个岛屿完全包含，那么我们称 grid2 中的这个岛屿为 子岛屿 。
# 
# 请你返回 grid2 中 子岛屿 的 数目 。
# 
# 
# 
# 示例 1：
# 
# 输入：grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# 输出：3
# 解释：如上图所示，左边为 grid1 ，右边为 grid2 。
# grid2 中标红的 1 区域是子岛屿，总共有 3 个子岛屿。
# 
# 
# 示例 2：
# 
# 输入：grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
# grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# 输出：2 
# 解释：如上图所示，左边为 grid1 ，右边为 grid2 。
# grid2 中标红的 1 区域是子岛屿，总共有 2 个子岛屿。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] 和 grid2[i][j] 都要么是 0 要么是 1 。
# 
# 
#

# @lc code=start
DIRECTIONS = (1, 0), (-1, 0), (0, 1), (0, -1)


def find(grid1: list[list[int]], grid2: list[list[int]], m: int, n: int, i: int, j: int):
    if (not (0 <= i < m and 0 <= j < n)) or grid2[i][j] == 0:
        return True

    grid2[i][j] = 0
    ret = grid1[i][j] == 1

    for di, dj in DIRECTIONS:
        ret = find(grid1, grid2, m, n, i + di, j + dj) and ret

    return ret


class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        ret = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and find(grid1, grid2, m, n, i, j):
                    ret += 1

        return ret
# @lc code=end

Solution().countSubIslands( [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])

