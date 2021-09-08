#
# @lc app=leetcode.cn id=1219 lang=python3
#
# [1219] 黄金矿工
#
# https://leetcode-cn.com/problems/path-with-maximum-gold/description/
#
# algorithms
# Medium (63.11%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    11.7K
# Total Submissions: 18.6K
# Testcase Example:  '[[0,6,0],[5,8,7],[0,9,0]]'
#
# 你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid
# 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。
# 
# 为了使收益最大化，矿工需要按以下规则来开采黄金：
# 
# 
# 每当矿工进入一个单元，就会收集该单元格中的所有黄金。
# 矿工每次可以从当前位置向上下左右四个方向走。
# 每个单元格只能被开采（进入）一次。
# 不得开采（进入）黄金数目为 0 的单元格。
# 矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
# 输出：24
# 解释：
# [[0,6,0],
# ⁠[5,8,7],
# ⁠[0,9,0]]
# 一种收集最多黄金的路线是：9 -> 8 -> 7。
# 
# 
# 示例 2：
# 
# 输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# 输出：28
# 解释：
# [[1,0,7],
# ⁠[2,0,6],
# ⁠[3,4,5],
# ⁠[0,3,0],
# ⁠[9,0,20]]
# 一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length, grid[i].length <= 15
# 0 <= grid[i][j] <= 100
# 最多 25 个单元格中有黄金。
# 
# 
#

# @lc code=start
DIRECTIONS = (1, 0), (-1, 0), (0, 1), (0, -1)


class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0

        def helper(i: int, j: int, prev_result: int, visited: set[tuple[int]]):
            if grid[i][j] == 0:
                return

            curr_result = prev_result + grid[i][j]
            nonlocal result
            result = max(result, curr_result)

            visited.add((i, j))

            for delta_i, delta_j in DIRECTIONS:
                next_i, next_j = delta_i + i, delta_j + j
                if (next_i, next_j) in visited:
                    continue
                if not (0 <= next_i < m and 0 <= next_j < n):
                    continue
                helper(delta_i + i, delta_j + j, curr_result, visited)

            visited.remove((i, j))

        for i in range(m):
            for j in range(n):
                helper(i, j, 0, set())

        return result
# @lc code=end

