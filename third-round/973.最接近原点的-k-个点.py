#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#
# https://leetcode-cn.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (64.50%)
# Likes:    315
# Dislikes: 0
# Total Accepted:    74.5K
# Total Submissions: 115.5K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# 给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，并且是一个整数 k ，返回离原点 (0,0)
# 最近的 k 个点。
# 
# 这里，平面上两点之间的距离是 欧几里德距离（ √(x1 - x2)^2 + (y1 - y2)^2 ）。
# 
# 你可以按 任何顺序 返回答案。除了点坐标的顺序之外，答案 确保 是 唯一 的。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：points = [[1,3],[-2,2]], k = 1
# 输出：[[-2,2]]
# 解释： 
# (1, 3) 和原点之间的距离为 sqrt(10)，
# (-2, 2) 和原点之间的距离为 sqrt(8)，
# 由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
# 我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
# 
# 
# 示例 2：
# 
# 
# 输入：points = [[3,3],[5,-1],[-2,4]], k = 2
# 输出：[[3,3],[-2,4]]
# （答案 [[-2,4],[3,3]] 也会被接受。）
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= k <= points.length <= 10^4
# -10^4 < xi, yi < 10^4
# 
# 
#

# @lc code=start
from random import randrange


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        self.quick_select(points, self.cmp, 0, len(points) - 1, k)
        return points[:k]

    def quick_select(self, points: list[list[int]], cmp, left: int, right: int, k: int):
        if left >= right:
            return

        i = self.partition(points, cmp, left, right)
        target = left + k - 1
        if i < target:
            self.quick_select(points, cmp, i + 1, right, target - i)
        elif i > target:
            self.quick_select(points, cmp, left, i - 1, k)

    def partition(self, points: list[list[int]], cmp, left: int, right: int):
        rand_index = randrange(left, right + 1)
        points[left], points[rand_index] = points[rand_index], points[left]

        pivot_index = left
        i, j = left, right
        while i < j:
            while i < j and cmp(points[j], points[pivot_index]) > 0:
                j -= 1
            while i < j and cmp(points[i], points[pivot_index]) <= 0:
                i += 1
            points[i], points[j] = points[j], points[i]

        points[i], points[pivot_index] = points[pivot_index], points[i]
        return i

    def cmp(self, a: list[int], b: list[int]):
        xa, ya = a
        xb, yb = b
        return (xa * xa + ya * ya) - (xb * xb + yb * yb)
# @lc code=end
