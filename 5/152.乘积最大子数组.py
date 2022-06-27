#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
# https://leetcode.cn/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (42.55%)
# Likes:    1659
# Dislikes: 0
# Total Accepted:    264.9K
# Total Submissions: 622.2K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 
# 测试用例的答案是一个 32-位 整数。
# 
# 子数组 是数组的连续子序列。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数
# 
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        prev_max = prev_min = 1
        result = nums[0]

        for n in nums:
            prev_max, prev_min = max(prev_max * n, prev_min * n, n), min(prev_max * n, prev_min * n, n)
            result = max(prev_max, result)

        return result
# @lc code=end
