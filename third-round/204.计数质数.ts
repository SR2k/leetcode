/*
 * @lc app=leetcode.cn id=204 lang=typescript
 *
 * [204] 计数质数
 *
 * https://leetcode-cn.com/problems/count-primes/description/
 *
 * algorithms
 * Medium (37.72%)
 * Likes:    831
 * Dislikes: 0
 * Total Accepted:    185.8K
 * Total Submissions: 492.7K
 * Testcase Example:  '10'
 *
 * 给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 10
 * 输出：4
 * 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 0
 * 输出：0
 *
 *
 * 示例 3：
 *
 *
 * 输入：n = 1
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= n <= 5 * 10^6
 *
 *
 */

export
// @lc code=start
function countPrimes(n: number): number {
  if (n <= 2) return 0

  const isPrimie = new Array(n).fill(true)
  let count = n - 2

  for (let i = 2; i <= n; i++) {
    if (!isPrimie[i]) continue

    let temp = i * 2
    while (temp < n) {
      if (isPrimie[temp]) {
        count -= 1
        isPrimie[temp] = false
      }
      temp += i
    }
  }

  return count
}
// @lc code=end
