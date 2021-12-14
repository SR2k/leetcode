#
# @lc app=leetcode.cn id=794 lang=python3
#
# [794] 有效的井字游戏
#
# https://leetcode-cn.com/problems/valid-tic-tac-toe-state/description/
#
# algorithms
# Medium (34.28%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    11.5K
# Total Submissions: 31.5K
# Testcase Example:  '["O  ","   ","   "]'
#
# 给你一个字符串数组 board 表示井字游戏的棋盘。当且仅当在井字游戏过程中，棋盘有可能达到 board 所显示的状态时，才返回 true 。
# 
# 井字游戏的棋盘是一个 3 x 3 数组，由字符 ' '，'X' 和 'O' 组成。字符 ' ' 代表一个空位。
# 
# 以下是井字游戏的规则：
# 
# 
# 玩家轮流将字符放入空位（' '）中。
# 玩家 1 总是放字符 'X' ，而玩家 2 总是放字符 'O' 。
# 'X' 和 'O' 只允许放置在空位中，不允许对已放有字符的位置进行填充。
# 当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
# 当所有位置非空时，也算为游戏结束。
# 如果游戏结束，玩家不允许再放置字符。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：board = ["O  ","   ","   "]
# 输出：false
# 解释：玩家 1 总是放字符 "X" 。
# 
# 
# 示例 2：
# 
# 
# 输入：board = ["XOX"," X ","   "]
# 输出：false
# 解释：玩家应该轮流放字符。
# 
# 示例 3：
# 
# 
# 输入：board = ["XXX","   ","OOO"]
# 输出：false
# 
# 
# Example 4:
# 
# 
# 输入：board = ["XOX","O O","XOX"]
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# board.length == 3
# board[i].length == 3
# board[i][j] 为 'X'、'O' 或 ' '
# 
# 
#

# @lc code=start
class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        count = { 'X': 0, 'O': 0, ' ': 0 }
        lines_count = { 'X': 0, 'O': 0, ' ': 0 }
        line_dots = { 'X': set(), 'O': set(), ' ': set() }
        intersections = { 'X': set(), 'O': set(), ' ': set() }

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                lines_count[board[i][0]] += 1

                for j in range(3):
                    if (i, j) in line_dots[board[i][0]]:
                        intersections[board[i][0]].add((i, j))
                    else:
                        line_dots[board[i][0]].add((i, j))

            if board[0][i] == board[1][i] == board[2][i]:
                lines_count[board[0][i]] += 1

                for j in range(3):
                    if (j, i) in line_dots[board[0][i]]:
                        intersections[board[0][i]].add((j, i))
                    else:
                        line_dots[board[0][i]].add((j, i))

            for j in range(3):
                count[board[i][j]] += 1

        if board[0][0] == board[1][1] == board[2][2]:
            lines_count[board[0][0]] += 1

            for i in range(3):
                if (i, i) in line_dots[board[0][0]]:
                    intersections[board[0][0]].add((i, i))
                else:
                    line_dots[board[0][0]].add((i, i))

        if board[0][2] == board[1][1] == board[2][0]:
            lines_count[board[0][2]] += 1

            for i in range(3):
                if (i, 3 - 1 - i) in line_dots[board[0][2]]:
                    intersections[board[0][2]].add((i, 3 - i - 1))
                else:
                    line_dots[board[0][2]].add((i, 3 - i - 1))

        if count['X'] != count['O'] and count['X'] != count['O'] + 1:
            return False

        if lines_count['X'] and count['X'] != count['O'] + 1:
            return False

        if lines_count['O'] and count['X'] != count['O']:
            return False

        if lines_count['X'] and lines_count['O']:
            return False

        if lines_count['X'] > 2 or lines_count['O'] > 2:
            return False

        if lines_count['X'] == 2 and not intersections['X']:
            return False

        if lines_count['O'] == 2 and not intersections['O']:
            return False

        return True
# @lc code=end

s = Solution()
print(s.validTicTacToe(board = ["O  ","   ","   "]))
print(s.validTicTacToe(board = ["XOX"," X ","   "]))
print(s.validTicTacToe(board = ["XXX","   ","OOO"]))
print(s.validTicTacToe(board = ["XOX","O O","XOX"]))

print(s.validTicTacToe(board = ["XXX","XOO","OO "]))
print(s.validTicTacToe(board = ["OXX","XOX","OXO"]))
