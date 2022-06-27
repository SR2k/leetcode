#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode.cn/problems/word-search/description/
#
# algorithms
# Medium (46.30%)
# Likes:    1318
# Dislikes: 0
# Total Accepted:    320.2K
# Total Submissions: 691.4K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCCED"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "SEE"
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCB"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == board.length
# n = board[i].length
# 1 
# 1 
# board 和 word 仅由大小写英文字母组成
# 
# 
# 
# 
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
# 
#

# @lc code=start
DIRECTIONS = (1, 0), (-1, 0), (0, 1), (0, -1)


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])


        def find(i: int, x: int, y: int, seen: set = None):
            if i == len(word):
                return True

            seen = seen or set()

            if not (0 <= x < m and 0 <= y < n):
                return False
            if board[x][y] != word[i]:
                return False
            if (x, y) in seen:
                return False

            seen.add((x, y))
            for dx, dy in DIRECTIONS:
                if find(i + 1, x + dx, y + dy, seen):
                    return True
            seen.remove((x, y))
            return False


        for i in range(m):
            for j in range(n):
                if find(0, i, j):
                    return True

        return False
# @lc code=end

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
