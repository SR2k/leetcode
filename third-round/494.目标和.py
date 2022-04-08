#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
# https://leetcode-cn.com/problems/target-sum/description/
#
# algorithms
# Medium (49.09%)
# Likes:    1125
# Dislikes: 0
# Total Accepted:    199.1K
# Total Submissions: 405.7K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 target 。
# 
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 
# 
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 
# 
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1], target = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 0 
# -1000 
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        sum_n = sum(nums)

        if not -sum_n <= target <= sum_n:
            return 0

        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            n = nums[i - 1]

            for j in range(-sum_n, sum_n + 1):
                dp[i][j] = dp[i - 1][j - n] + dp[i - 1][j + n]

        return dp[-1][target]
# @lc code=end

s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], target = 3))
print(s.findTargetSumWays([1,1,0,1,1], target = 4))
print(s.findTargetSumWays([1], target = 1))
  