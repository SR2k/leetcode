#
# @lc app=leetcode.cn id=774 lang=python3
#
# [774] 最小化去加油站的最大距离
#
# https://leetcode-cn.com/problems/minimize-max-distance-to-gas-station/description/
#
# algorithms
# Hard (59.02%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    1.1K
# Total Submissions: 1.9K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10]\n9'
#
# 整数数组 stations 表示 水平数轴 上各个加油站的位置。给你一个整数 k 。
# 
# 请你在数轴上增设 k 个加油站，新增加油站可以位于 水平数轴 上的任意位置，而不必放在整数位置上。
# 
# 设 penalty() 是：增设 k 个新加油站后，相邻 两个加油站间的最大距离。
# 请你返回 penalty() 可能的最小值。与实际答案误差在 10^-6 范围内的答案将被视作正确答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：stations = [1,2,3,4,5,6,7,8,9,10], k = 9
# 输出：0.50000
# 
# 
# 示例 2：
# 
# 
# 输入：stations = [23,24,36,39,46,56,57,65,84,98], k = 1
# 输出：14.00000
# 
# 
# 
# 
# 提示：
# 
# 
# 10 
# 0 
# stations 按 严格递增 顺序排列
# 1 
# 
# 
#

# @lc code=start
from math import ceil


class Solution:
    @staticmethod
    def equals(a: float, b: float) -> bool:
        return abs(a - b) < 1e-6

    @staticmethod
    def check(gaps: list[int], k: int, gap: float) -> float:
        if gap == 0:
            return -1

        result = -float('inf')
        for i in range(len(gaps) - 1, -1, -1):
            if gaps[i] <= gap:
                return max(result, gaps[i])
            s_count = ceil(gaps[i] / gap)
            k -= s_count - 1
            result = max(result, gaps[i] / s_count)
            if k < 0:
                return -1
        return result

    def minmaxGasDist(self, stations: list[int], k: int) -> float:
        gaps = sorted([stations[i] - stations[i - 1] for i in range(1, len(stations))])
        left, right = 0, gaps[-1]

        while not Solution.equals(left, right):
            middle = (left + right) / 2
            middle_check = Solution.check(gaps, k, middle)

            if middle_check > 0:
                if Solution.equals(right, middle_check):
                    break
                right = middle_check
            else:
                if Solution.equals(left, middle):
                    break
                left = middle

        l = Solution.check(gaps, k, left)
        if l > 0:
            return l
        r = Solution.check(gaps, k, right)
        if r > 0:
            return r
# @lc code=end

s = Solution()
print(s.minmaxGasDist([1,2,3,4,5,6,7,8,9,10], k = 9))
print(s.minmaxGasDist([23,24,36,39,46,56,57,65,84,98], k = 1))
print(s.minmaxGasDist([3,6,12,19,33,44,67,72,89,95], 2))
print(s.minmaxGasDist([4,8,15,19,24,33,37,48,74,81], 22))
