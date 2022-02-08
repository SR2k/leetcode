#
# @lc app=leetcode.cn id=361 lang=python3
#
# [361] 轰炸敌人
#
# https://leetcode-cn.com/problems/bomb-enemy/description/
#
# algorithms
# Medium (55.34%)
# Likes:    56
# Dislikes: 0
# Total Accepted:    2.8K
# Total Submissions: 5K
# Testcase Example:  '[["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]'
#
# 想象一下炸弹人游戏，在你面前有一个二维的网格来表示地图，网格中的格子分别被以下三种符号占据：
# 
# 
# 'W' 表示一堵墙
# 'E' 表示一个敌人
# '0'（数字 0）表示一个空位
# 
# 
# 
# 
# 请你计算一个炸弹最多能炸多少敌人。
# 
# 由于炸弹的威力不足以穿透墙体，炸弹只能炸到同一行和同一列没被墙体挡住的敌人。
# 
# 注意：你只能把炸弹放在一个空的格子里
# 
# 示例:
# 
# 输入: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# 输出: 3 
# 解释: 对于如下网格
# 
# 0 E 0 0 
# E 0 W E 
# 0 E 0 0
# 
# 假如在位置 (1,1) 放置炸弹的话，可以炸到 3 个敌人
# 
# 
#

# @lc code=start
WALL = 'W'
ENEMY = 'E'
EMPTY = '0'

class Solution:
    def maxKilledEnemies(self, grid: list[list[str]]) -> int:
        dp_top: list[list[int]] = []
        dp_left: list[list[int]] = []
        m, n = len(grid), len(grid[0])

        for i in range(m):
            dp_top.append([])
            dp_left.append([])

            for j in range(n):
                prev_top, prev_left = 0, 0
                if i != 0 and grid[i][j] != WALL:
                    prev_top = dp_top[i - 1][j]
                if j != 0 and grid[i][j] != WALL:
                    prev_left = dp_left[i][j - 1]


                if grid[i][j] == ENEMY:
                    dp_top[i].append(prev_top + 1)
                    dp_left[i].append(prev_left + 1)
                else:
                    dp_top[i].append(prev_top)
                    dp_left[i].append(prev_left)

        dp_right, dp_bottom = [[0 for _ in range(n)] for __ in range(m)], [[0 for _ in range(n)] for __ in range(m)]
        ret = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i != m - 1 and grid[i][j] != WALL:
                    dp_bottom[i][j] = dp_bottom[i + 1][j]
                if j != n - 1 and grid[i][j] != WALL:
                    dp_right[i][j] = dp_right[i][j + 1]
 
                if grid[i][j] == ENEMY:
                    dp_bottom[i][j] += 1
                    dp_right[i][j] += 1

                if grid[i][j] == EMPTY:
                    ret = max(dp_top[i][j] + dp_left[i][j] + dp_right[i][j] + dp_bottom[i][j], ret)
                    # print(i, j, 'top', dp_top[i][j], 'lft', dp_left[i][j], 'rig', prev_right, 'btm', prev_bottom, ret)

        return ret

# @lc code=end

# print(Solution().maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))
g = [ \
    ["0","0","0","0","0","0","0","0","0","0"], \
    ["E","E","E","E","E","E","E","E","E","E"], \
    ["W","W","W","W","W","W","W","W","W","W"] \
]
print(Solution().maxKilledEnemies(g))
