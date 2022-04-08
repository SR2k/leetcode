#
# @lc app=leetcode.cn id=286 lang=python3
#
# [286] 墙与门
#
# https://leetcode-cn.com/problems/walls-and-gates/description/
#
# algorithms
# Medium (52.28%)
# Likes:    196
# Dislikes: 0
# Total Accepted:    14.1K
# Total Submissions: 27K
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


WALL, GATE, DOOR = -1, 0, 2147483647
DIRECTIONS = (1, 0), (-1, 0), (0, 1), (0, -1)


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        m, n = len(rooms), len(rooms[0])
        queue: deque[tuple[int, int]] = deque()
        seen: set[tuple[int, int]] = set()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == GATE:
                    queue.append((i, j))
                    seen.add((i, j))

        level = 0
        while queue:
            level_length = len(queue)
            level += 1

            for _ in range(level_length):
                i, j  = queue.popleft()

                for di, dj in DIRECTIONS:
                    ni, nj = i + di, j + dj

                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if rooms[ni][nj] == WALL:
                        continue
                    if (ni, nj) in seen:
                        continue

                    rooms[ni][nj] = min(level, rooms[ni][nj])

                    seen.add((ni, nj))
                    queue.append((ni, nj))
# @lc code=end
