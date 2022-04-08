#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (54.78%)
# Likes:    1032
# Dislikes: 0
# Total Accepted:    155.5K
# Total Submissions: 283.6K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 
# 
# 示例 1:
# 
# 
# 输入：prices = [3,3,5,0,0,3,1,4]
# 输出：6
# 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 
# 示例 2：
# 
# 
# 输入：prices = [1,2,3,4,5]
# 输出：4
# 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
# 。   
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 
# 
# 示例 3：
# 
# 
# 输入：prices = [7,6,4,3,1] 
# 输出：0 
# 解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
# 
# 示例 4：
# 
# 
# 输入：prices = [1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
NEG_INF = -float('inf')


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [NEG_INF] * 4

        for i, price in enumerate(prices):
            b1, s1, b2, s2 = dp
            b1 = max(-price, b1)

            if i >= 1:
                s1 = max(s1, dp[0] + price)
            if i >= 2:
                b2 = max(b2, dp[1] - price)
            if i >= 3:
                s2 = max(s2, dp[2] + price)

            dp = [b1, s1, b2, s2]

        return max(max(dp), 0)
# @lc code=end

#    [3, 3, 5, 0, 0,3,1,4]
# b1 -3 -3 -3  0
# s1 0  0  2   2
# b2 0  0  -3
# s2 0  0  0
#

print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1] ))
print(Solution().maxProfit([1]))
