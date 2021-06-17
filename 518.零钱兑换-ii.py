#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
# https://leetcode-cn.com/problems/coin-change-2/description/
#
# algorithms
# Medium (59.33%)
# Likes:    437
# Dislikes: 0
# Total Accepted:    64.7K
# Total Submissions: 106.3K
# Testcase Example:  '5\n[1,2,5]'
#
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
# 
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# 示例 2:
# 
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
# 
# 
# 示例 3:
# 
# 输入: amount = 10, coins = [10] 
# 输出: 1
# 
# 
# 
# 
# 注意:
# 
# 你可以假设：
# 
# 
# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数
# 
# 
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        count = len(coins)
        dp = []

        for i in range(count):
            coin = coins[i]
            dp.append([])

            for j in range(amount + 1):
                dp[i].append(0)

                if i == 0:
                    dp[i][j] = 1 if j % coin == 0 else 0
                elif j == 0:
                    dp[i][j] = 1
                else:
                    for k in range(j // coin + 1):
                        if j >= k * coin: dp[i][j] += dp[i - 1][j - k * coin]

        return dp[count - 1][amount]

# @lc code=end

