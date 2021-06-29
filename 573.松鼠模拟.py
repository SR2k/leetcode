#
# @lc app=leetcode.cn id=573 lang=python3
#
# [573] 松鼠模拟
#
# https://leetcode-cn.com/problems/squirrel-simulation/description/
#
# algorithms
# Medium (65.83%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    877
# Total Submissions: 1.3K
# Testcase Example:  '5\n7\n[2,2]\n[4,4]\n[[3,0], [2,5]]'
#
# 
# 现在有一棵树，一只松鼠和一些坚果。位置由二维网格的单元格表示。你的目标是找到松鼠收集所有坚果的最小路程，且坚果是一颗接一颗地被放在树下。松鼠一次最多只能携带一颗坚果，松鼠可以向上，向下，向左和向右四个方向移动到相邻的单元格。移动次数表示路程。
# 
# 输入 1:
# 
# 输入: 
# 高度 : 5
# 宽度 : 7
# 树的位置 : [2,2]
# 松鼠 : [4,4]
# 坚果 : [[3,0], [2,5]]
# 输出: 12
# 解释:
# ​​​​​
# 
# 
# 注意:
# 
# 
# 所有给定的位置不会重叠。
# 松鼠一次最多只能携带一颗坚果。
# 给定的坚果位置没有顺序。
# 高度和宽度是正整数。 3 <= 高度 * 宽度 <= 10,000。
# 给定的网格至少包含一颗坚果，唯一的一棵树和一只松鼠。
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, height: int, width: int, tree: list[int], squirrel: list[int], nuts: list[list[int]]) -> int:
        tx, ty = tree
        sx, sy = squirrel
        ret = 0
        min_t, min_s = -1, -1

        for nut_x, nut_y in nuts:
            td = abs(tx - nut_x) + abs(ty - nut_y)
            sd = abs(sx - nut_x) + abs(sy - nut_y)

            ret += td * 2

            if min_s < 0 or min_t - min_s < td - sd:
                min_t, min_s = td, sd

        return ret - min_t + min_s
# @lc code=end
