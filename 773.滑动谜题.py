#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#
# https://leetcode-cn.com/problems/sliding-puzzle/description/
#
# algorithms
# Hard (64.32%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    13.7K
# Total Submissions: 19.9K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
# 
# 一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
# 
# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
# 
# 给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
# 
# 示例：
# 
# 
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
# 
# 
# 
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
# 
# 
# 
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
# 
# 
# 
# 输入：board = [[3,2,4],[1,5,0]]
# 输出：14
# 
# 
# 提示：
# 
# 
# board 是一个如上所述的 2 x 3 的数组.
# board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.
# 
# 
#

# @lc code=start
# from typing import Optional
grid = tuple[int, int, int, int, int, int]


def swapped(curr: grid, i: int, j: int) -> grid:
    l = list(curr)
    l[i], l[j] = l[j], l[i]
    return tuple(l)


def add(curr: grid, result: list[grid], visited: set[grid]):
    if curr in visited:
        return
    visited.add(curr)
    result.append(curr)


def get_next(curr: grid, visited: set[grid]) -> list[grid]:
    result = []
    i = curr.index(0)

    if i > 2:
        up = swapped(curr, i - 3, i)
        add(up, result, visited)
    else:
        down = swapped(curr, i + 3, i)
        add(down, result, visited)
    if i % 3 != 0:
        left = swapped(curr, i - 1, i)
        add(left, result, visited)
    if i % 3 != 2:
        right = swapped(curr, i + 1, i)
        add(right, result, visited)

    return result


RESULT = (1, 2, 3, 4, 5, 0)


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        visited: set[grid] = set()
        queue: list[grid] = [(board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2])]
        level = 0

        if queue[0] == RESULT:
            return 0

        while queue:
            level_length = len(queue)
            level += 1

            for _ in range(level_length):
                curr = queue.pop(0)
                next = get_next(curr, visited)

                for n in next:
                    if n == RESULT:
                        return level
                    queue.append(n)

        return -1
# @lc code=end
