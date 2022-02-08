#
# @lc app=leetcode.cn id=1197 lang=python3
#
# [1197] 进击的骑士
#
# https://leetcode-cn.com/problems/minimum-knight-moves/description/
#
# algorithms
# Medium (35.79%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 11.3K
# Testcase Example:  '2\n1'
#
# 一个坐标可以从 -infinity 延伸到 +infinity 的 无限大的 棋盘上，你的 骑士 驻扎在坐标为 [0, 0] 的方格里。
# 
# 骑士的走法和中国象棋中的马相似，走 “日” 字：即先向左（或右）走 1 格，再向上（或下）走 2 格；或先向左（或右）走 2 格，再向上（或下）走 1
# 格。
# 
# 每次移动，他都可以按图示八个方向之一前进。
# 
# 
# 
# 现在，骑士需要前去征服坐标为 [x, y] 的部落，请你为他规划路线。
# 
# 最后返回所需的最小移动次数即可。本题确保答案是一定存在的。
# 
# 
# 
# 示例 1：
# 
# 输入：x = 2, y = 1
# 输出：1
# 解释：[0, 0] → [2, 1]
# 
# 
# 示例 2：
# 
# 输入：x = 5, y = 5
# 输出：4
# 解释：[0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
# 
# 
# 
# 
# 提示：
# 
# 
# |x| + |y| <= 300
# 
# 
#

# @lc code=start
from collections import deque

DIRECTIONS = (-1, -2), (-2, -1), (1, -2), (-2, 1), (-1, 2), (2, -1), (1, 2), (2, 1)

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = deque([(0, 0)])
        visited = set(queue)
        step = -1

        while queue:
            level_length = len(queue)
            step += 1

            for _ in range(level_length):
                curr = queue.popleft()
                if curr == (x, y): return step

                for deltaI, deltaJ in DIRECTIONS:
                    next = (curr[0] + deltaI, curr[1] + deltaJ)
 
                    if next not in visited:
                        visited.add(next)
                        queue.append(next)
# @lc code=end

