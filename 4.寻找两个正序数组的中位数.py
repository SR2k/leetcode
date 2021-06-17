#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (40.27%)
# Likes:    4173
# Dislikes: 0
# Total Accepted:    426.2K
# Total Submissions: 1.1M
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
# 
# 
# 示例 3：
# 
# 
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
# 
# 
# 示例 4：
# 
# 
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
# 
# 
# 示例 5：
# 
# 
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
# 
# 
# 
# 
# 提示：
# 
# 
# nums1.length == m
# nums2.length == n
# 0 
# 0 
# 1 
# -10^6 
# 
# 
# 
# 
# 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
# 
#

# @lc code=start
import math

class Solution:
    @staticmethod
    def get_left_count(nums: list[int], left_max: int) -> tuple[int, int]:
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            middle = math.floor((left + right) / 2)

            if nums[middle] <= left_max:
                left = middle
            else:
                right = middle

        if nums[right] <= left_max: return (right, right + 1)
        if nums[left] <= left_max: return (left, right)
        return (left - 1, left)

    @staticmethod
    def arr_get(nums: list[int], index: int):
        if index < 0 or index >= len(nums):
            return None
        return nums[index]

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        count_1, count_2 = len(nums1), len(nums2)
        total_count = count_1 + count_2
        left_total_count = math.ceil(total_count / 2)

        # joint = None
        # if nums1[-1] >= nums2[0]: joint = nums1 + nums2
        # if nums2[-1] >= nums1[0]: joint = nums2 + nums1
        # if joint:
        #     i = total_count // 2
        #     return (joint[i] + joint[i - 1]) / 2 if total_count % 2 == 0 else 0.0 + joint[i]

        left_1, right_1 = 0, count_1 - 1
        while left_1 + 1 < right_1:
            middle = math.floor((left_1 + right_1) / 2)

            left_2, right_2 = Solution.get_left_count(nums2, nums1[middle])
            if middle + 1 + right_2 <= left_total_count:
                left_1 = middle
            else:
                right_1 = middle

        left_2, right_2 = Solution.get_left_count(nums2, nums1[left_1])

        if left_1 + 1 + left_2 + 1 < left_total_count:
            left_1, right_1 = right_1, right_1 + 1
            left_2, right_2 = Solution.get_left_count(nums2, nums1[right_1])

        if left_total_count % 2 == 1:
            return 

# @lc code=end

Solution().findMedianSortedArrays([0,0,0,0,1,2,3,4,5], [4,5,6,7,8])
