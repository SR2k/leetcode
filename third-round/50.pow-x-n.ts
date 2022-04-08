/*
 * @lc app=leetcode.cn id=50 lang=typescript
 *
 * [50] Pow(x, n)
 *
 * https://leetcode-cn.com/problems/powx-n/description/
 *
 * algorithms
 * Medium (37.81%)
 * Likes:    878
 * Dislikes: 0
 * Total Accepted:    256.4K
 * Total Submissions: 678.1K
 * Testcase Example:  '2.00000\n10'
 *
 * 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n^ ）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：x = 2.00000, n = 10
 * 输出：1024.00000
 *
 *
 * 示例 2：
 *
 *
 * 输入：x = 2.10000, n = 3
 * 输出：9.26100
 *
 *
 * 示例 3：
 *
 *
 * 输入：x = 2.00000, n = -2
 * 输出：0.25000
 * 解释：2^-2 = 1/2^2 = 1/4 = 0.25
 *
 *
 *
 *
 * 提示：
 *
 *
 * -100.0 < x < 100.0
 * -2^31 <= n <= 2^31-1
 * -10^4 <= x^n <= 10^4
 *
 *
 */

export
// @lc code=start
function myPow(x: number, n: number): number {
  if (x === 0 || x === 1) return x

  if (n < 0) return 1 / myPow(x, -n)
  if (n === 0) return 1
  if (n === 1) return x

  const half = myPow(x, Math.floor(n / 2))
  if (n % 2 === 1) {
    return half * half * x
  }
  return half * half
}
// @lc code=end
