#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (44.89%)
# Likes:    1670
# Dislikes: 0
# Total Accepted:    351.8K
# Total Submissions: 783.4K
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
# 示例 4：
# 
# 
# 输入：coins = [1], amount = 1
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：coins = [1], amount = 2
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0]

        for t in range(1, amount + 1):
            result = float('inf')

            for coin in coins:
                if t >= coin:
                    result = min(dp[t - coin] + 1, result)

            dp.append(result)

        return dp[-1] if dp[-1] != float('inf') else -1
# @lc code=end

s = Solution()
print(s.coinChange(coins = [1, 2, 5], amount = 11))
print(s.coinChange(coins = [2], amount = 3))
print(s.coinChange(coins = [1], amount = 0))
print(s.coinChange(coins = [1], amount = 1))
print(s.coinChange(coins = [1], amount = 2))

print(s.coinChange([156,265,40,280], 9109))
