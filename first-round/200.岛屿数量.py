#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (56.18%)
# Likes:    1434
# Dislikes: 0
# Total Accepted:    359.8K
# Total Submissions: 640.5K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 的值为 '0' 或 '1'
# 
# 
#

# @lc code=start
DIRECTIONS = (0, 1), (0, -1), (1, 0), (-1, 0)


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
 
        def helper(i: int, j: int):
            if not (0 <= i < m) or not (0 <= j < n):
                return
            if grid[i][j] != '1':
                return
            grid[i][j] = '0'
            for deltaI, deltaJ in DIRECTIONS:
                helper(i + deltaI, j + deltaJ)

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    helper(i, j)

        return result
# @lc code=end

s = Solution()
print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
