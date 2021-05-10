/*
 * @lc app=leetcode.cn id=309 lang=javascript
 *
 * [309] 最佳买卖股票时机含冷冻期
 *
 * https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
 *
 * algorithms
 * Medium (58.74%)
 * Likes:    764
 * Dislikes: 0
 * Total Accepted:    87.8K
 * Total Submissions: 149.5K
 * Testcase Example:  '[1,2,3,0,2]'
 *
 * 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
 * 
 * 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
 * 
 * 
 * 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
 * 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
 * 
 * 
 * 示例:
 * 
 * 输入: [1,2,3,0,2]
 * 输出: 3 
 * 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
 * 
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  if (!prices || !prices.length) return 0

  // 买入 - 计作负收益
  // 卖出 - 计作正收益

  // dp[i] 表示第 i 天交易为以下状态的最大收益
  // dp[i][0] 卖出
  // dp[i][1] 不买不卖
  // dp[i][2] 持有（包括买入和之前持有）
  const dp = new Array(prices.length).fill(0).map(() => [0, 0, 0])

  dp[0] = [0, 0, 0 - prices[0]]

  for (let i = 1; i < prices.length; i++) {
    // 卖出：前一天的最大持有收益 + 今天卖掉得到的钱
    dp[i][0] = dp[i - 1][2] + prices[i]
    // 不买不卖
    dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0])
    // 持有：前一天持有或今天买入
    dp[i][2] = Math.max(dp[i - 1][1] - prices[i], dp[i - 1][2])
  }

  return Math.max(...dp[prices.length - 1])
};
// @lc code=end

// console.log(maxProfit([1,2,3,0,2]))
