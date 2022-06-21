#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode.cn/problems/coin-change/description/
#
# algorithms
# Medium (45.66%)
# Likes:    1982
# Dislikes: 0
# Total Accepted:    458.1K
# Total Submissions: 1M
# Testcase Example:  '[1,2,5]\n11'
#
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
# 
# 你可以认为每种硬币的数量是无限的。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1
# 
# 示例 2：
# 
# 
# 输入：coins = [2], amount = 3
# 输出：-1
# 
# 示例 3：
# 
# 
# 输入：coins = [1], amount = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
# 
# 
#

# @lc code=start
INF = float('inf')


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [INF for _ in range(amount + 1)]
        dp[0] = 0
        coins.sort()

        for i in range(1, amount + 1):
            for c in coins:
                if c > i:
                    break
                dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[amount] == INF:
            return -1

        return dp[amount]
# @lc code=end

# dp[i] = min([dp[i - c] for c in coins])
