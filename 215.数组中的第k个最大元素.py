#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.66%)
# Likes:    1652
# Dislikes: 0
# Total Accepted:    616.4K
# Total Submissions: 952.9K
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


    def quick_select(self, nums: list[int], k: int, left: int, right: int):
        if left >= right:
            return

        i = self.partition(nums, left, right)
        target = right - k + 1

        if i < target:
            self.quick_select(nums, k, i + 1, right)
        elif i > target:
            self.quick_select(nums, i - target, left, i - 1)

    def partition(self, nums: list[int], left: int, right: int):
        rand = randrange(left, right + 1)
        nums[left], nums[rand] = nums[rand], nums[left]

        i, j = left, right
        pivot = nums[left]
        while i < j:
            # Move right side first to prevent this:
            # [3, 2, 1, 5, 6, 4] -> [5, 2, 1, 3, 6, 4], i = 3
            # j moves first to ensure that when i and j met (i == j),
            # nums[i] <= pivot, because if nums[j] > pivot, j wil -1.
            # And finally swap i and left will get the true result.
            while i < j and nums[j] > pivot:
                j -= 1

            # <= to ensure left is passed
            while i < j and nums[i] <= pivot:
                i += 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[i], nums[left] = nums[left], nums[i]
        return i
# @lc code=end

Solution().findKthLargest([3,2,1,5,6,4], 2)

p = 3
       j
[3, 2, 1, 5, 6, 4]
       i
