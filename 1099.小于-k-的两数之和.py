#
# @lc app=leetcode.cn id=1099 lang=python3
#
# [1099] 小于 K 的两数之和
#
# https://leetcode-cn.com/problems/two-sum-less-than-k/description/
#
# algorithms
# Easy (58.05%)
# Likes:    51
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 8.4K
# Testcase Example:  '[34,23,1,24,75,33,54,8]\n60'
#
# 给你一个整数数组 nums 和整数 k ，返回最大和 sum ，满足存在 i < j 使得 nums[i] + nums[j] = sum 且 sum <
# k 。如果没有满足此等式的 i,j 存在，则返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [34,23,1,24,75,33,54,8], k = 60
# 输出：58
# 解释：
# 34 和 24 相加得到 58，58 小于 60，满足题意。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [10,20,30], k = 15
# 输出：-1
# 解释：
# 我们无法找到和小于 15 的两个元素。
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

# @lc code=start
class Solution:
    def b_find(nums: list[int], left: int, max_target: int) -> int:
        right = len(nums) - 1

        while left + 1 < right:
            middle = (left + right) // 2
            num_middle = nums[middle]

            if num_middle >= max_target:
                right = middle
            else:
                left = middle

        if nums[right] < max_target:
            return nums[right]
        if nums[left] < max_target:
            return nums[left]
        return -1


    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        if len(nums) <= 1:
            return -1

        nums.sort()
        result = -1

        for i in range(len(nums) - 1):
            n = nums[i]

            if n >= k:
                return result

            max_target = k - n
            target = Solution.b_find(nums, i + 1, max_target)
            if target >= 0:
                result = max(n + target, result)

        return result
# @lc code=end
