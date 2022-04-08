#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.67%)
# Likes:    1553
# Dislikes: 0
# Total Accepted:    570.3K
# Total Submissions: 881.9K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 
# 
# 提示： 
# 
# 
# 1 
# -10^4 
# 
# 
#

# @lc code=start
from random import randrange


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        self.quick_select(nums, k, 0, len(nums) - 1)
        return nums[-k]


    @staticmethod
    def quick_select(nums: list[int], k: int, left: int, right: int):
        if left >= right:
            return

        i = Solution.partition(nums, left, right)
        target = right - k + 1

        if i > target:
            Solution.quick_select(nums, i - target, left, i - 1)
        elif i < target:
            Solution.quick_select(nums, k, i + 1, right)


    @staticmethod
    def partition(nums: list[int], left: int, right: int) -> int:
        rand = randrange(left, right + 1)
        Solution.swap(nums, left, rand)
        pivot_index = left
        i, j = left, right

        while i < j:
            while i < j and nums[j] > nums[pivot_index]:
                j -= 1
            while i < j and nums[i] <= nums[pivot_index]:
                i += 1
            Solution.swap(nums, i, j)

        Solution.swap(nums, i, pivot_index)
        return i


    @staticmethod
    def swap(nums: list[int], i: int, j: int):
        nums[i], nums[j] = nums[j], nums[i]
# @lc code=end
