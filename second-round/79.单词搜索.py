#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (45.93%)
# Likes:    1121
# Dislikes: 0
# Total Accepted:    248K
# Total Submissions: 539.9K
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
directions = (0, 1), (0, -1), (1, 0), (-1, 0)


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def search(i: int, j: int, k: int, seen: set[tuple[int, int]]) -> bool:
            if (i, j) in seen:
                return False
            if not 0 <= i < m or not 0 <= j < n or word[k] != board[i][j]:
                return False

            if k == len(word) - 1:
                return True

            seen.add((i, j))
            for di, dj in directions:
                if search(i + di, j + dj, k + 1, seen):
                    return True
            seen.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if search(i, j, 0, set()):
                    return True
        return False
# @lc code=end

s = Solution()
print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
