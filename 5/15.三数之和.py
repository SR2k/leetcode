#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (35.36%)
# Likes:    4740
# Dislikes: 0
# Total Accepted:    953.6K
# Total Submissions: 2.7M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
# 且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [0]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^5 
# 
# 
#

# @lc code=start
from random import randrange


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        self.quick_sort(nums, 0, len(nums) - 1)

        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            k = len(nums) - 1

            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                while j < k and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1

                if j == k:
                    break

                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

        return result


    def quick_sort(self, nums: list[int], left: int, right: int):
        if left >= right:
            return

        i = self.partition(nums, left, right)
        self.quick_sort(nums, left, i - 1)
        self.quick_sort(nums, i + 1, right)


    def partition(self, nums: list[int], left: int, right: int):
        rand = randrange(left, right + 1)
        self.swap(nums, left, rand)

        i, j = left, right
        pivot = nums[left]
        while i < j:
            while i < j and nums[j] > pivot:
                j -= 1
            while i < j and nums[i] <= pivot:
                i += 1
            self.swap(nums, i, j)

        self.swap(nums, i, left)
        return i


    def swap(self, nums: list[int], i: int, j: int):
        nums[i], nums[j] = nums[j], nums[i]
# @lc code=end
