#
# @lc app=leetcode.cn id=840 lang=python3
#
# [840] 矩阵中的幻方
#
# https://leetcode-cn.com/problems/magic-squares-in-grid/description/
#
# algorithms
# Medium (35.66%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    8.7K
# Total Submissions: 24.3K
# Testcase Example:  '[[4,3,8,4],[9,5,1,9],[2,7,6,2]]'
#
# 3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
# 
# 给定一个由整数组成的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。
# 
# 
# 
# 示例：
# 
# 输入: [[4,3,8,4],
# ⁠     [9,5,1,9],
# ⁠     [2,7,6,2]]
# 输出: 1
# 解释: 
# 下面的子矩阵是一个 3 x 3 的幻方：
# 438
# 951
# 276
# 
# 而这一个不是：
# 384
# 519
# 762
# 
# 总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
# 
# 
# 提示:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# 0 <= grid[i][j] <= 15
# 
# 
#

# @lc code=start
class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0

        def check(i0: int, j0: int):
            s = set()
            r, c = [0, 0, 0], [0, 0, 0]
            d, dr = 0, 0
            for i in range(3):
                for j in range(3):
                    val = grid[i0 + i][j0 + j]
                    if val <= 0 or val > 9:
                        return False
                    if val in s:
                        return False
                    r[i] += val
                    c[j] += val

                    if i == j:
                        d += val
                    if 2 - i == j:
                        dr += val
                    s.add(val)

            if d != dr:
                return False
            for x in r:
                if x != dr:
                    return False
            for x in c:
                if x != dr:
                    return False
            return True

        ret = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if check(i, j):
                    ret += 1

        return ret
# @lc code=end

