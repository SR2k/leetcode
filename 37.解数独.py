#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# https://leetcode-cn.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (67.23%)
# Likes:    1203
# Dislikes: 0
# Total Accepted:    133.3K
# Total Submissions: 198.1K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过填充空格来解决数独问题。
# 
# 数独的解法需 遵循如下规则：
# 
# 
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 
# 
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：board =
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# 
# 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# board.length == 9
# board[i].length == 9
# board[i][j] 是一位数字或者 '.'
# 题目数据 保证 输入数独仅有一个解
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        zones = [set() for _ in range(9)]


        for i in range(9):
            for j in range(9):
                z = Solution.ij_2_zone(i, j)
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                zones[z].add(board[i][j])


        def helper(i: int, j: int):
            if i == 9:
                return True

            if board[i][j] != '.':
                ni, nj = Solution.get_next(i, j)
                return helper(ni, nj)

            for _n in range(1, 9 + 1):
                z = Solution.ij_2_zone(i, j)
                ni, nj = Solution.get_next(i, j)
                n = str(_n)

                if n in rows[i] or n in cols[j] or n in zones[z]:
                    continue

                board[i][j] = n
                rows[i].add(n)
                cols[j].add(n)
                zones[z].add(n)

                if helper(ni, nj):
                    return True

                board[i][j] = '.'
                rows[i].remove(n)
                cols[j].remove(n)
                zones[z].remove(n)

        helper(0, 0)


    @staticmethod
    def ij_2_zone(i: int, j: int):
        return i // 3 * 3 + j // 3


    @staticmethod
    def get_next(i: int, j: int):
        if j == 8:
            return i + 1, 0
        return i, j + 1
# @lc code=end
