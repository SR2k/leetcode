#
# @lc app=leetcode.cn id=1496 lang=python3
#
# [1496] 判断路径是否相交
#
# https://leetcode-cn.com/problems/path-crossing/description/
#
# algorithms
# Easy (53.86%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    10.9K
# Total Submissions: 20.3K
# Testcase Example:  '"NES"'
#
# 给你一个字符串 path，其中 path[i] 的值可以是 'N'、'S'、'E' 或者 'W'，分别表示向北、向南、向东、向西移动一个单位。
# 
# 机器人从二维平面上的原点 (0, 0) 处开始出发，按 path 所指示的路径行走。
# 
# 如果路径在任何位置上出现相交的情况，也就是走到之前已经走过的位置，请返回 True ；否则，返回 False 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：path = "NES"
# 输出：false 
# 解释：该路径没有在任何位置相交。
# 
# 示例 2：
# 
# 
# 
# 输入：path = "NESWW"
# 输出：true
# 解释：该路径经过原点两次。
# 
# 
# 
# 提示：
# 
# 
# 1 <= path.length <= 10^4
# path 仅由 {'N', 'S', 'E', 'W} 中的字符组成
# 
# 
#

# @lc code=start
DIRECTIONS = {
    'N': (0, -1),
    'S': (0, 1),
    'W': (-1, 0),
    'E': (1, 0),
}


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = (0, 0)
        visited = set([curr])

        for p in path:
            d = DIRECTIONS[p]
            curr = (curr[0] + d[0], curr[1] + d[1])

            if curr in visited:
                return True
            visited.add(curr)

        return False
# @lc code=end

print(Solution().isPathCrossing('NESWW"'))
print(Solution().isPathCrossing('NWSE"'))
