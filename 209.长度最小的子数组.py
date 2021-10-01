#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (47.00%)
# Likes:    758
# Dislikes: 0
# Total Accepted:    185.4K
# Total Submissions: 394.1K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr]
# ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 
# 
# 示例 2：
# 
# 
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# 
# 
# 
# 
# 进阶：
# 
# 
# 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
# 
# 
#

# @lc code=start
class Solution:
    def b_find(self, nums: list[int], target: int, left: int, right: int):
        left = 0

        while left + 1 < right:
            middle = (right - left) // 2 + left
            num_middle = nums[middle]

            if num_middle == target:
                return middle
            elif num_middle > target:
                right = middle
            else:
                left = middle

        if nums[right] <= target:
            return right
        if nums[left] <= target:
            return left
        return -1


    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)

        prev_left = 0
        result = float('inf')
        for right in range(1, len(prefix_sum)):
            left = self.b_find(prefix_sum, prefix_sum[right] - target, prev_left, right)

            if left >= 0:
                prev_left = left
                result = min(right - left, result)

        return result if result <= len(nums) else 0
# @lc code=end
