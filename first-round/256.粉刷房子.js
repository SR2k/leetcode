/*
 * @lc app=leetcode.cn id=256 lang=javascript
 *
 * [256] 粉刷房子
 *
 * https://leetcode-cn.com/problems/paint-house/description/
 *
 * algorithms
 * Medium (60.74%)
 * Likes:    112
 * Dislikes: 0
 * Total Accepted:    8.7K
 * Total Submissions: 14.3K
 * Testcase Example:  '[[17,2,17],[16,16,5],[14,3,19]]'
 *
 * 假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
 * 
 * 当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的矩阵来表示的。
 * 
 * 例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1
 * 号房子粉刷成绿色的花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。
 * 
 * 注意：
 * 
 * 所有花费均为正整数。
 * 
 * 示例：
 * 
 * 输入: [[17,2,17],[16,16,5],[14,3,19]]
 * 输出: 10
 * 解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
 * 最少花费: 2 + 5 + 3 = 10。
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[][]} costs
 * @return {number}
 */
var minCost = function(costs) {
  const roomCount = costs.length
  if (!roomCount) return 0

  const dp = [costs[0]]
  // 前 i 个房子
  for (let i = 1; i <= roomCount - 1; i++) {
    dp[i] = []

    // 恰好以 j 的颜色涂完
    dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
  }

  return Math.min(...dp[roomCount - 1])
};
// @lc code=end
