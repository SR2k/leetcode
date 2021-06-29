#
# @lc app=leetcode.cn id=286 lang=python3
#
# [286] 墙与门
#
# https://leetcode-cn.com/problems/walls-and-gates/description/
#
# algorithms
# Medium (50.34%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    10.1K
# Total Submissions: 20.1K
# Testcase Example:  '[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]'
#
# 你被给定一个 m × n 的二维网格 rooms ，网格中有以下三种可能的初始化值：
# 
# 
# -1 表示墙或是障碍物
# 0 表示一扇门
# INF 无限表示一个空的房间。然后，我们用 2^31 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647
# 的。
# 
# 
# 你要给每个空房间位上填上该房间到 最近门的距离 ，如果无法到达门，则填 INF 即可。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：rooms =
# [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# 输出：[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
# 
# 
# 示例 2：
# 
# 
# 输入：rooms = [[-1]]
# 输出：[[-1]]
# 
# 
# 示例 3：
# 
# 
# 输入：rooms = [[2147483647]]
# 输出：[[2147483647]]
# 
# 
# 示例 4：
# 
# 
# 输入：rooms = [[0]]
# 输出：[[0]]
# 
# 
# 
# 
# 提示：
# 
# 
# m == rooms.length
# n == rooms[i].length
# 1 
# rooms[i][j] 是 -1、0 或 2^31 - 1
# 
# 
#

# @lc code=start
from collections import deque

cell = tuple[int, int]

WALL, GATE, EMPTY = -1, 0, 2147483647
DIRECTIONS = (0, 1), (1, 0), (0, -1), (-1, 0)

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        queue: deque[cell] = deque()
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == GATE:
                    queue.append((i, j))
        step = 0

        while queue:
            level_length = len(queue)
            step += 1

            for _ in range(level_length):
                i, j = queue.popleft()

                for deltaI, deltaJ in DIRECTIONS:
                    next_i, next_j = i + deltaI, j + deltaJ
                    if not (0 <= next_i < m and 0 <= next_j < n):
                        continue
                    if rooms[next_i][next_j] != EMPTY:
                        continue
                    rooms[next_i][next_j] = step
                    queue.append((next_i, next_j))
# @lc code=end

# print(Solution().wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))

