#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (73.93%)
# Likes:    1268
# Dislikes: 0
# Total Accepted:    201.2K
# Total Submissions: 272.1K
# Testcase Example:  '4'
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
# 
# 
# 
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：[["Q"]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 9
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []

        rows = cols = diag = revr = 0
        curr = [['.' for _ in range(n)] for _ in range(n)]


        def helper(i: int, j: int, cnt: int):
            if i == n:
                if cnt == n:
                    result.append(["".join(row) for row in curr])
                return

            ni, nj = Solution.get_next(i, j, n)

            if n - ni + 1 < n - cnt:
                return

            helper(ni, nj, cnt)

            diag_repr = Solution.get_diag_repr(i, j, n)
            revr_repr = Solution.get_revr_repr(i, j, n)

            nonlocal rows, cols, diag, revr
            if rows & 1 << i or cols & 1 << j or diag & 1 << diag_repr or revr & 1 << revr_repr:
                return

            rows ^= 1 << i
            cols ^= 1 << j
            diag ^= 1 << diag_repr
            revr ^= 1 << revr_repr
            curr[i][j] = 'Q'

            helper(ni, nj, cnt + 1)

            rows ^= 1 << i
            cols ^= 1 << j
            diag ^= 1 << diag_repr
            revr ^= 1 << revr_repr
            curr[i][j] = '.'


        helper(0, 0, 0)
        return result


    @staticmethod
    def get_next(i: int, j: int, n: int):
        if j + 1 == n:
            return i + 1, 0
        return i, j + 1


    @staticmethod
    def get_diag_repr(i: int, j: int, n: int):
        d = abs(i - j)

        if i >= j:
            return d
        return n + d


    @staticmethod
    def get_revr_repr(i: int, j: int, n: int):
        return Solution.get_diag_repr(i, n - 1 - j, n)
# @lc code=end

#  x x x x
#  x x x x
#  x x x x
#  x x x x
