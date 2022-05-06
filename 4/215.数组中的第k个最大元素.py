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
        Solution.quick_select(nums, 0, len(nums) - 1, k)
        return nums[-k]


    @staticmethod
    def quick_select(nums: list[int], left: int, right: int, k: int):
        if right <= left:
            return

        i = Solution.partition(nums, left, right)
        target = right - k + 1

        if i > target:
            Solution.quick_select(nums, left, i - 1, i - target)
        elif i < target:
            Solution.quick_select(nums, i + 1, right, k)


    @staticmethod
    def partition(nums: list[int], left: int, right: int):
        rand = randrange(left, right + 1)
        nums[left], nums[rand] = nums[rand], nums[left]

        i, j = left, right
        while i < j:
            while i < j and nums[j] > nums[left]:
                j -= 1
            while i < j and nums[i] <= nums[left]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[i] = nums[i], nums[left]
        return i
# @lc code=end
