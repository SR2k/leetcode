/*
 * @lc app=leetcode.cn id=69 lang=typescript
 *
 * [69] x 的平方根
 *
 * https://leetcode-cn.com/problems/sqrtx/description/
 *
 * algorithms
 * Easy (39.00%)
 * Likes:    894
 * Dislikes: 0
 * Total Accepted:    458.3K
 * Total Submissions: 1.2M
 * Testcase Example:  '4'
 *
 * 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
 *
 * 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
 *
 * 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：x = 4
 * 输出：2
 *
 *
 * 示例 2：
 *
 *
 * 输入：x = 8
 * 输出：2
 * 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= x <= 2^31 - 1
 *
 *
 */

export
// @lc code=start
function mySqrt(x: number): number {
  let left = 0
  let right = 46341

  while (left + 1 < right) {
    // eslint-disable-next-line no-bitwise
    const middle = (left + right) >> 1
    const middleSquared = middle * middle

    if (middleSquared === x) {
      return middle
    }
    if (middleSquared > x) {
      right = middle
    } else {
      left = middle
    }
  }

  if (right * right <= x) return right
  return left
}
// @lc code=end
