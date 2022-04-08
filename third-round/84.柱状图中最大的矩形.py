#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (43.94%)
# Likes:    1835
# Dislikes: 0
# Total Accepted:    227.6K
# Total Submissions: 518.1K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入： heights = [2,4]
# 输出： 4
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        len_heights = len(heights)
        right = [len_heights for _ in heights]
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                right[stack.pop()] = i
            stack.append(i)

        left = [-1 for _ in heights]
        stack = []
        for i in range(len_heights - 1, -1, -1):
            h = heights[i]
            while stack and heights[stack[-1]] > h:
                left[stack.pop()] = i
            stack.append(i)

        # print(left, right)

        return max([(right[i] - left[i] - 1) * heights[i] for i in range(len_heights)])
# @lc code=end

# l = [-1, -1, -1, -1, -1, -1]
# s = [2#0, 1#1, 5#2, 6#3, 2#4, 3#5]
# 递增栈
#

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
print(s.largestRectangleArea([2]))
print(s.largestRectangleArea([555]))
