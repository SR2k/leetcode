#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (42.32%)
# Likes:    1453
# Dislikes: 0
# Total Accepted:    212.5K
# Total Submissions: 502.3K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 
# 
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        prev_max, prev_min = 1, 1
        result = nums[0]

        for n in nums:
            s = [n, n * prev_max, n * prev_min]
            prev_max, prev_min = max(s), min(s)
            result = max(result, prev_max)

        return result
# @lc code=end

s = Solution()
print(s.maxProduct([2,3,-2,4]))
print(s.maxProduct([-2,0,-1]))
print(s.maxProduct([-2,3,-2,4]))
print(s.maxProduct([-4,-3,-2]))
