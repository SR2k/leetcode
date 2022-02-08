#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (73.82%)
# Likes:    1156
# Dislikes: 0
# Total Accepted:    176.1K
# Total Submissions: 238.6K
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
    @staticmethod
    def i_j_to_diagonal(i: int, j: int, n: int) -> tuple[int, int]:
        if i <= j:
            b_j = j - i
            b = n - 1 + b_j
        else:
            b_i = i - j
            b = n - 1 - b_i

        if i <= n - 1 - j:
            b_j = j + i
            bd = b_j
        else:
            b_i = i - (n - 1 - j)
            bd = n - 1 + b_i

        return b, bd


    @staticmethod
    def grid_2_result(grid: list[list[bool]]) -> list[str]:
        result = ["".join("Q" if cell else "." for cell in row) for row in grid]
        return result


    def solveNQueens(self, n: int) -> list[list[str]]:
        grid = [[False for _ in range(n)] for __ in range(n)]
        rows, cols, diagonal, back_diagonal = 0, 0, 0, 0
        result = []
        def helper(i: int, j: int, cnt: int):
            if cnt == n:
                result.append(Solution.grid_2_result(grid))
                return

            if i >= n:
                return

            # 不放
            next_j = j + 1
            next_i = i + next_j // n
            helper(next_i, next_j % n, cnt)

            # 能放则放
            nonlocal rows, cols, diagonal, back_diagonal
            d, bd = Solution.i_j_to_diagonal(i, j, n)
            resp_i, resp_j, resp_d, resp_bd = 1 << (i + 1), 1 << (j + 1), 1 << (d + 1), 1 << (bd + 1)
            if (rows & resp_i) or (cols & resp_j) or (diagonal & resp_d) or (back_diagonal & resp_bd):
                pass
            else:
                grid[i][j] = True
                rows ^= resp_i
                cols ^= resp_j
                diagonal ^= resp_d
                back_diagonal ^= resp_bd

                next_j = j + 1
                next_i = i + next_j // n
                helper(next_i, next_j % n, cnt + 1)

                grid[i][j] = False
                rows ^= resp_i
                cols ^= resp_j
                diagonal ^= resp_d
                back_diagonal ^= resp_bd

        helper(0, 0, 0)
        return result
# @lc code=end

s = Solution()
print(s.solveNQueens(1))
print(s.solveNQueens(2))
print(s.solveNQueens(3))
print(s.solveNQueens(4))
# print(s.solveNQueens(5))
# print(s.solveNQueens(6))
# print(s.solveNQueens(7))
# print(s.solveNQueens(8))

# for i in range(4):
#     for j in range(4):
#         print(i, j, '-->', Solution.i_j_to_diagonal(i, j, 4))
# print(Solution.i_j_to_diagonal(2, 2, 4))
# print(Solution.i_j_to_diagonal(3, 1, 4))
