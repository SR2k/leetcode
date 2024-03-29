#
# @lc app=leetcode.cn id=356 lang=python3
#
# [356] 直线镜像
#
# https://leetcode-cn.com/problems/line-reflection/description/
#
# algorithms
# Medium (35.18%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 4.3K
# Testcase Example:  '[[1,1],[-1,1]]'
#
# 在一个二维平面空间中，给你 n 个点的坐标。问，是否能找出一条平行于 y 轴的直线，让这些点关于这条直线成镜像排布？
# 
# 注意：题目数据中可能有重复的点。
# 
# 
# 
# 进阶：你能找到比 O(n^2) 更优的解法吗?
# 
# 
# 
# 示例 1：
# 
# 
# 输入：points = [[1,1],[-1,1]]
# 输出：true
# 解释：可以找出 x = 0 这条线。
# 
# 
# 示例 2：
# 
# 
# 输入：points = [[1,1],[-1,-1]]
# 输出：false
# 解释：无法找出这样一条线。
# 
# 
# 
# 提示：
# 
# 
# n == points.length
# 1 
# -10^8 
# 
# 
#

# @lc code=start
class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        points.sort(points)
# @lc code=end

