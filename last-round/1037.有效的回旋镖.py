#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#
# https://leetcode-cn.com/problems/valid-boomerang/description/
#
# algorithms
# Easy (44.17%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    8.9K
# Total Submissions: 20.1K
# Testcase Example:  '[[1,1],[2,3],[3,2]]'
#
# 回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。
# 
# 给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。
# 
# 
# 
# 示例 1：
# 
# 输入：[[1,1],[2,3],[3,2]]
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：[[1,1],[2,2],[3,3]]
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# points.length == 3
# points[i].length == 2
# 0 <= points[i][j] <= 100
# 
# 
#

# @lc code=start
def div(a: int, b: int) -> float:
    if b == 0:
        return float('inf')
    return a / b


class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        p1, p2, p3 = points
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        s = set()
        s.add(div(y3 - y2, x3 - x2))
        s.add(div(y2 - y1, x2 - x1))
        s.add(div(y3 - y1, x3 - x1))

        return len(s) == 3
# @lc code=end

# Solution().isBoomerang([[0,0],[1,1],[1,1]])

