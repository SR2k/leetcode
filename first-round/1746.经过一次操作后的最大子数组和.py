#
# @lc app=leetcode.cn id=1746 lang=python3
#
# [1746] 经过一次操作后的最大子数组和
#
# https://leetcode-cn.com/problems/maximum-subarray-sum-after-one-operation/description/
#
# algorithms
# Medium (58.87%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    648
# Total Submissions: 1.1K
# Testcase Example:  '[2,-1,-4,-3]'
#
# 你有一个整数数组 nums。你只能将一个元素 nums[i] 替换为 nums[i] * nums[i]。
# 
# 返回替换后的最大子数组和。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,-1,-4,-3]
# 输出：17
# 解释：你可以把-4替换为16(-4*(-4))，使nums = [2,-1,16,-3]. 现在，最大子数组和为 2 + -1 + 16 = 17.
# 
# 示例 2：
# 
# 
# 输入：nums = [1,-1,1,1,-1,-1,1]
# 输出：4
# 解释：你可以把第一个-1替换为1，使 nums = [1,1,1,1,-1,-1,1]. 现在，最大子数组和为 1 + 1 + 1 + 1 =
# 4.
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
class Solution:
    def maxSumAfterOperation(self, nums: list[int]) -> int:
        dp = [0, 0]
        result = float('-inf')

        for n in nums:
            next = [dp[0], dp[1]]
            next[0] = max(dp[0] + n, n)
            next[1] = max(dp[0] + n * n, n * n, dp[1] + n, n)

            dp = next
            result = max(dp[0], dp[1], result)

        return result

# @lc code=end

