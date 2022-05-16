#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (54.90%)
# Likes:    4842
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 1.8M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
#
#
#
# 示例 1：
#
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [5,4,-1,7,8]
# 输出：23
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# 
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        result = nums[0]
        min_sum = prev_sum = nums[0]

        for n in nums:
            prev_sum += n
            result = max(result, prev_sum - min_sum)
            min_sum = min(min_sum, prev_sum)

        return result
# @lc code=end
