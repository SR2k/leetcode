#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Medium (69.61%)
# Likes:    1574
# Dislikes: 0
# Total Accepted:    563.4K
# Total Submissions: 809.1K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组 prices ，其中 prices[i] 表示股票第 i 天的价格。
# 
# 在每一天，你可能会决定购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以购买它，然后在 同一天 出售。
# 返回 你能获得的 最大 利润 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: prices = [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 
# 
# 示例 2:
# 
# 
# 输入: prices = [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 
# 
# 示例 3:
# 
# 
# 输入: prices = [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
# 
# 提示：
# 
# 
# 1 <= prices.length <= 3 * 10^4
# 0 <= prices[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [-prices[0], 0]

        for i in range(len(prices)):
            hold = max(dp[1] - prices[i], dp[0])
            sold = max(dp[0] + prices[i], dp[1])
            dp = [hold, sold]

        return max(dp)
# @lc code=end
