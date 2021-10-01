#
# @lc app=leetcode.cn id=1401 lang=python3
#
# [1401] 圆和矩形是否有重叠
#
# https://leetcode-cn.com/problems/circle-and-rectangle-overlapping/description/
#
# algorithms
# Medium (41.76%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 9.4K
# Testcase Example:  '1\n0\n0\n1\n-1\n3\n1'
#
# 给你一个以 (radius, x_center, y_center) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2)，其中 (x1,
# y1) 是矩形左下角的坐标，(x2, y2) 是右上角的坐标。
# 
# 如果圆和矩形有重叠的部分，请你返回 True ，否则返回 False 。
# 
# 换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
# 输出：true
# 解释：圆和矩形有公共点 (1,0) 
# 
# 
# 示例 2：
# 
# 
# 
# 输入：radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 
# 输入：radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
# 输出：true
# 
# 
# 示例 4：
# 
# 输入：radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= radius <= 2000
# -10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
# x1 < x2
# y1 < y2
# 
# 
#

# @lc code=start
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 <= x_center <= x2 and y1 <= y_center <= y2:
            return True

        x, y = x_center, y_center

        if x_center <= x1 and y_center <= y1:
            x, y = x1, y1
        elif x_center <= x1 and y1 < y_center < y2:
            x, y = x1, y_center
        elif x_center <= x1 and y_center >= y2:
            x, y = x1, y2
        elif x1 < x_center < x2 and y_center <= y1:
            x, y = x_center, y1
        elif x1 < x_center < x2 and y_center >= y2:
            x, y = x_center, y2
        elif x_center >= x2 and y_center <= y1:
            x, y = x2, y1
        elif x_center >= x2 and y1 < y_center < y2:
            x, y = x2, y_center
        else:
            x, y = x2, y2

        return (x - x_center) ** 2 + (y - y_center) ** 2 <= radius ** 2
# @lc code=end

s = Solution()
# print(s.checkOverlap(radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1))
# print(s.checkOverlap(radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1))
# print(s.checkOverlap(radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3))
# print(s.checkOverlap(radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1))
print(s.checkOverlap(4, 102, 50, 0, 0, 100, 100))
