/*
 * @lc app=leetcode.cn id=322 lang=typescript
 *
 * [322] 零钱兑换
 *
 * https://leetcode.cn/problems/coin-change/description/
 *
 * algorithms
 * Medium (45.96%)
 * Likes:    2128
 * Dislikes: 0
 * Total Accepted:    522.3K
 * Total Submissions: 1.1M
 * Testcase Example:  '[1,2,5]\n11'
 *
 * 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
 *
 * 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
 *
 * 你可以认为每种硬币的数量是无限的。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：coins = [1, 2, 5], amount = 11
 * 输出：3
 * 解释：11 = 5 + 5 + 1
 *
 * 示例 2：
 *
 *
 * 输入：coins = [2], amount = 3
 * 输出：-1
 *
 * 示例 3：
 *
 *
 * 输入：coins = [1], amount = 0
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= coins.length <= 12
 * 1 <= coins[i] <= 2^31 - 1
 * 0 <= amount <= 10^4
 *
 *
 */

export
// @lc code=start
function coinChange(coins: number[], amount: number): number {
  const INVALID = Number.MAX_SAFE_INTEGER

  const dp: number[] = new Array(amount + 1).fill(INVALID)
  dp[0] = 0

  for (let i = 1; i <= amount; i++) {
    for (const coin of coins) {
      const prev = dp[i - coin] ?? INVALID
      if (prev === INVALID) continue
      dp[i] = Math.min(dp[i], prev + 1)
    }
  }

  const result = dp[amount]
  if (result === INVALID) {
    return -1
  }
  return result
}
// @lc code=end
