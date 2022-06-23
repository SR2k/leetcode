/*
 * @lc app=leetcode.cn id=264 lang=typescript
 *
 * [264] 丑数 II
 *
 * https://leetcode.cn/problems/ugly-number-ii/description/
 *
 * algorithms
 * Medium (58.49%)
 * Likes:    919
 * Dislikes: 0
 * Total Accepted:    128.2K
 * Total Submissions: 219.1K
 * Testcase Example:  '10'
 *
 * 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
 *
 * 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 10
 * 输出：12
 * 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：1
 * 解释：1 通常被视为丑数。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 *
 *
 */

export
// @lc code=start
function nthUglyNumber(n: number): number {
  const dp = [1]
  let p2 = 0, p3 = 0, p5 = 0

  while (dp.length <= n) {
    const r2 = dp[p2] * 2, r3 = dp[p3] * 3, r5 = dp[p5] * 5
    const next = Math.min(r2, r3, r5)

    if (dp[dp.length - 1] !== next) {
      dp.push(next)
    }

    if (next === r2) {
      p2++
    } else if (next === r3) {
      p3++
    } else {
      p5++
    }
  }

  return dp[n - 1]
}
// @lc code=end
