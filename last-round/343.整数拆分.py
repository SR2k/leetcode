#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
# https://leetcode-cn.com/problems/integer-break/description/
#
# algorithms
# Medium (59.88%)
# Likes:    528
# Dislikes: 0
# Total Accepted:    89.7K
# Total Submissions: 149.8K
# Testcase Example:  '2'
#
# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
# 
# 示例 1:
# 
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 
# 示例 2:
# 
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 
# 说明: 你可以假设 n 不小于 2 且不大于 58。
# 
#

# @lc code=start
import math

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2: return 1

        dp = [1, 1, 2]

        for i in range(3, n + 1):
            temp = 1

            for j in range(2, math.ceil(i / 2) + 1):
                # print('i, j', i, j, 'curr', j * dp[i - j], 'prev', temp)
                # print('ret=', max(j * dp[i - j], temp))
                temp = max(j * dp[i - j], j * (i - j), temp)

            dp.append(temp)

        # print(dp)
        return dp[n]

# @lc code=end

print(Solution().integerBreak(4))
