/*
 * @lc app=leetcode.cn id=29 lang=typescript
 *
 * [29] 两数相除
 *
 * https://leetcode.cn/problems/divide-two-integers/description/
 *
 * algorithms
 * Medium (22.22%)
 * Likes:    971
 * Dislikes: 0
 * Total Accepted:    181.4K
 * Total Submissions: 816.2K
 * Testcase Example:  '10\n3'
 *
 * 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
 *
 * 返回被除数 dividend 除以除数 divisor 得到的商。
 *
 * 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) =
 * -2
 *
 *
 *
 * 示例 1:
 *
 * 输入: dividend = 10, divisor = 3
 * 输出: 3
 * 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
 *
 * 示例 2:
 *
 * 输入: dividend = 7, divisor = -3
 * 输出: -2
 * 解释: 7/-3 = truncate(-2.33333..) = -2
 *
 *
 *
 * 提示：
 *
 *
 * 被除数和除数均为 32 位有符号整数。
 * 除数不为 0。
 * 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
 *
 *
 */

export
// @lc code=start
function divide(dividend: number, divisor: number): number {
  const sign = (dividend < 0 && divisor > 0) || (dividend > 0 && divisor < 0) ? -1 : 1

  dividend = Math.abs(dividend)
  divisor = Math.abs(divisor)

  if (dividend < divisor) return 0

  let currResult = 1
  let b = divisor

  while (dividend >= b + b) {
    currResult += currResult
    b += b
  }

  const nextResult = divide(dividend - b, divisor)

  let MAX_ABS = 2 ** 31
  if (sign > 0) MAX_ABS--

  if (currResult > MAX_ABS - nextResult) {
    return 2 ** 31 - 1
  }
  return sign * (currResult + nextResult)
}
// @lc code=end
