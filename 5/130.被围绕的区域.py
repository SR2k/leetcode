#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode.cn/problems/surrounded-regions/description/
#
# algorithms
# Medium (45.65%)
# Likes:    808
# Dislikes: 0
# Total Accepted:    177.9K
# Total Submissions: 389.6K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X'
# 填充。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 
# 
# 示例 2：
# 
# 
# 输入：board = [["X"]]
# 输出：[["X"]]
# 
# 
# 
# 
# 提示：
# 
# 
# m == board.length
# n == board[i].length
# 1 
# board[i][j] 为 'X' 或 'O'
# 
# 
# 
# 
#

# @lc code=start
from collections import deque
from re import L


Point = tuple[int, int]
DIRECTIONS = (1, 0), (-1, 0), (0, 1), (0, -1)


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        seen: set[Point] = set()
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] != 'O':
                    continue
                if Solution.check(board, (i, j), seen):
                    Solution.fill(board, i, j)

    @staticmethod
    def check(board: list[list[int]], entry: Point, seen: set[Point]):
        if entry in seen:
            return False

        m, n = len(board), len(board[0])
        result = True
        queue: deque[Point] = deque([entry])
        seen.add(entry)

        while queue:
            i, j = queue.popleft()

            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                result = False

            for di, dj in DIRECTIONS:
                ni, nj = i + di, j + dj
                p = (ni, nj)

                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if board[ni][nj] != 'O':
                    continue
                if p in seen:
                    continue

                seen.add(p)
                queue.append(p)

        return result

    @staticmethod
    def fill(board: list[list[int]], i: int, j: int):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return
        if board[i][j] != 'O':
            return

        board[i][j] = 'X'
        for di, dj in DIRECTIONS:
            Solution.fill(board, i + di, j + dj)
# @lc code=end
