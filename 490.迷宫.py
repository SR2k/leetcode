#
# @lc app=leetcode.cn id=490 lang=python3
#
# [490] 迷宫
#
# https://leetcode-cn.com/problems/the-maze/description/
#
# algorithms
# Medium (47.79%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 11.8K
# Testcase Example:  '[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\n[0,4]\n[4,4]'
#
# 由空地（用 0 表示）和墙（用 1 表示）组成的迷宫 maze 中有一个球。球可以途经空地向 上、下、左、右
# 四个方向滚动，且在遇到墙壁前不会停止滚动。当球停下时，可以选择向下一个方向滚动。
# 
# 
# 
# 给你一个大小为 m x n 的迷宫 maze ，以及球的初始位置 start 和目的地 destination ，其中 start =
# [startrow, startcol] 且 destination = [destinationrow, destinationcol]
# 。请你判断球能否在目的地停下：如果可以，返回 true ；否则，返回 false 。
# 
# 你可以 假定迷宫的边缘都是墙壁（参考示例）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
# start = [0,4], destination = [4,4]
# 输出：true
# 解释：一种可能的路径是 : 左 -> 下 -> 左 -> 下 -> 右 -> 下 -> 右。
# 
# 
# 示例 2：
# 
# 
# 输入：maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
# start = [0,4], destination = [3,2]
# 输出：false
# 解释：不存在能够使球停在目的地的路径。注意，球可以经过目的地，但无法在那里停驻。
# 
# 
# 示例 3：
# 
# 
# 输入：maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]],
# start = [4,3], destination = [0,1]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == maze.length
# n == maze[i].length
# 1 
# maze[i][j] is 0 or 1.
# start.length == 2
# destination.length == 2
# 0 row, destinationrow 
# 0 col, destinationcol 
# 球和目的地都在空地上，且初始时它们不在同一位置
# 迷宫 至少包括 2 块空地
# 
# 
# 
# 
# 
#

# @lc code=start
EMPTY, WALL = 0, 1
DIRECTIONS = (1, 0), (-1, 0), (0, 1), (0, -1)

class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        m, n = len(maze), len(maze[0])

        def check(i: int, j: int) -> bool:
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            return maze[i][j] != WALL

        queue = [(start[0], start[1])]
        visited = set(queue)

        while queue:
            i, j = queue.pop()
            for deltaI, deltaJ in DIRECTIONS:
                eI, eJ = i, j
                while check(eI + deltaI, eJ + deltaJ):
                    eI += deltaI
                    eJ += deltaJ

                if eI == destination[0] and eJ == destination[1]:
                    return True

                if not (eI, eJ) in visited:
                    visited.add((eI, eJ))
                    queue.append((eI, eJ))

        return False
# @lc code=end
