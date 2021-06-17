#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#
# https://leetcode-cn.com/problems/rectangle-overlap/description/
#
# algorithms
# Easy (47.74%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    35.4K
# Total Submissions: 74.4K
# Testcase Example:  '[0,0,2,2]\n[1,1,3,3]'
#
# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。矩形的上下边平行于 x
# 轴，左右边平行于 y 轴。
# 
# 如果相交的面积为 正 ，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
# 
# 给出两个矩形 rec1 和 rec2 。如果它们重叠，返回 true；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：rec1 = [0,0,1,1], rec2 = [2,2,3,3]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# rect1.length == 4
# rect2.length == 4
# -10^9 
# rec1[0]  且 rec1[1] 
# rec2[0]  且 rec2[1] 
# 
# 
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        l1, t1, r1, b1 = rec1
        l2, t2, r2, b2 = rec2

        x, y = False, False

        if l1 == r1 or t1 == b1 or l2 == r2 or t2 == b2: return False

        if l1 < l2:
            x = r1 > l2
        elif l2 <= l1 < r2:
            x = r1 > l1

        if t1 < t2:
            y = b1 > t2
        elif t2 <= t1 < b2:
            y = b1 > t1

        # print(x, y)

        return x and y


# @lc code=end

