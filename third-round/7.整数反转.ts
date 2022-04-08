/*
 * @lc app=leetcode.cn id=7 lang=typescript
 *
 * [7] 整数反转
 *
 * https://leetcode-cn.com/problems/reverse-integer/description/
 *
 * algorithms
 * Medium (35.14%)
 * Likes:    3382
 * Dislikes: 0
 * Total Accepted:    940.9K
 * Total Submissions: 2.7M
 * Testcase Example:  '123'
 *
 * 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
 *
 * 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
 * 假设环境不允许存储 64 位整数（有符号或无符号）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：x = 123
 * 输出：321
 *
 *
 * 示例 2：
 *
 *
 * 输入：x = -123
 * 输出：-321
 *
 *
 * 示例 3：
 *
 *
 * 输入：x = 120
 * 输出：21
 *
 *
 * 示例 4：
 *
 *
 * 输入：x = 0
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * -2^31
 *
 *
 */

export
// @lc code=start
function reverse(x: number): number {
  if (x === 0) return 0

  const sign = x > 0 ? 1 : -1
  x = Math.abs(x)

  let result = 0
  while (x) {
    const digit = x % 10
    x = Math.floor(x / 10)
    if (willExceed(result, digit, sign)) {
      return 0
    }
    result = result * 10 + digit
  }

  return sign * result
}

const MAX_NEGATIVE_ABSOLUTE = 2 ** 31
const MAX_POSITIVE_ABSOLUTE = MAX_NEGATIVE_ABSOLUTE - 1

function willExceed(curr: number, digit: number, sign: 1 | -1) {
  const target = sign > 0 ? MAX_POSITIVE_ABSOLUTE : MAX_NEGATIVE_ABSOLUTE

  if (curr > (target - digit) / 10) {
    return true
  }
  return false
}
// @lc code=end
