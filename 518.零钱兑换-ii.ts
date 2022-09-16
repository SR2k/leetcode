/*
 * @lc app=leetcode.cn id=518 lang=typescript
 *
 * [518] 零钱兑换 II
 *
 * https://leetcode.cn/problems/coin-change-2/description/
 *
 * algorithms
 * Medium (69.36%)
 * Likes:    917
 * Dislikes: 0
 * Total Accepted:    195.2K
 * Total Submissions: 281K
 * Testcase Example:  '5\n[1,2,5]'
 *
 * 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
 *
 * 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
 *
 * 假设每一种面额的硬币有无限个。
 *
 * 题目数据保证结果符合 32 位带符号整数。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：amount = 5, coins = [1, 2, 5]
 * 输出：4
 * 解释：有四种方式可以凑成总金额：
 * 5=5
 * 5=2+2+1
 * 5=2+1+1+1
 * 5=1+1+1+1+1
 *
 *
 * 示例 2：
 *
 *
 * 输入：amount = 3, coins = [2]
 * 输出：0
 * 解释：只用面额 2 的硬币不能凑成总金额 3 。
 *
 *
 * 示例 3：
 *
 *
 * 输入：amount = 10, coins = [10]
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 1
 * coins 中的所有值 互不相同
 * 0
 *
 *
 */

export
// @lc code=start
function change(amount: number, coins: number[]): number {
  const dp: number[][] = new Array(amount + 1).fill(0).map(() => (
    new Array(coins.length + 1).fill(0)
  ))

  for (let i = 0; i <= amount; i++) {
    for (let j = 0; j <= coins.length; j++) {
      if (i === 0) {
        dp[i][j] = 1
      } else if (j === 0) {
        dp[i][j] = 0
      } else {
        const coin = coins[j - 1]
        // console.log(`用前 ${coins.slice(0, j)} 拼 ${i}:`, '不用：', dp[i][j - 1], '用：', dp[i - coin]?.[j] ?? 0)
        dp[i][j] = dp[i][j - 1] + (dp[i - coin]?.[j] ?? 0)
      }
    }
  }

  // console.log(dp)
  return dp[amount][coins.length]
}
// @lc code=end
