/*
 * @lc app=leetcode.cn id=188 lang=javascript
 *
 * [188] 买卖股票的最佳时机 IV
 *
 * https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
 *
 * algorithms
 * Hard (37.43%)
 * Likes:    499
 * Dislikes: 0
 * Total Accepted:    70.6K
 * Total Submissions: 188.4K
 * Testcase Example:  '2\n[2,4,1]'
 *
 * 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
 * 
 * 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
 * 
 * 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：k = 2, prices = [2,4,1]
 * 输出：2
 * 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
 * 
 * 示例 2：
 * 
 * 
 * 输入：k = 2, prices = [3,2,6,5,0,3]
 * 输出：7
 * 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
 * ⁠    随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 =
 * 3 。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 
 * 0 
 * 0 
 * 
 * 
 */

// @lc code=start
/**
 * @param {number} k
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(k, prices) {
  if (!prices || prices.length <= 1) return 0

  const hold = [[]]
  const sold = [[]]

  let maxProfit = 0

  for (let i = 1; i <= k; i++) {
    hold[i] = []
    sold[i] = []

    for (let j = 2 * i - 2; j < prices.length; j++) {
      // console.log(`现在是第 ${j} 天，股票数 ${i}，今天股票价格 ${prices[j]}`)

      hold[i][j] = Math.max(
        (sold[i - 1][j - 1] || 0) - prices[j],
        typeof hold[i][j - 1] === 'number' ? hold[i][j - 1] :  Number.MIN_SAFE_INTEGER
      )

      if (j >= 2 * i - 1) {
        sold[i][j] = Math.max(
          hold[i][j - 1] + prices[j], 
          typeof sold[i][j - 1] === 'number' ? sold[i][j - 1] : Number.MIN_SAFE_INTEGER
        )
        maxProfit = Math.max(maxProfit, sold[i][j])
      }

      // console.log(`第 ${j} 天持有股票数 ${i}`, hold[i][j])
      // console.log(`第 ${j} 天卖出股票数 ${i}`, sold[i][j])
      // console.log()
    }
  }

  // console.log(sold)
  // console.log(hold)
  return maxProfit
};
// @lc code=end

// console.log(maxProfit(1, [-1, -2]))
