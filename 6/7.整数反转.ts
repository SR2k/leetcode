/*
 * @lc app=leetcode.cn id=7 lang=typescript
 *
 * [7] 整数反转
 *
 * https://leetcode.cn/problems/reverse-integer/description/
 *
 * algorithms
 * Medium (35.30%)
 * Likes:    3544
 * Dislikes: 0
 * Total Accepted:    1M
 * Total Submissions: 2.9M
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
  if (x === 0) return x

  const flag = x > 0 ? 1 : -1
  x = Math.abs(x)

  let result = 0
  while (x) {
    const d = x % 10
    if (willExceed(result, d, flag)) {
      return 0
    }
    result = result * 10 + d
    x = Math.floor(x / 10)
  }

  return flag * result
}

const willExceed = (curr: number, digit: number, sign: number) => {
  const edge = sign > 0 ? MAX_POS_ABS : MAX_NEG_ABS
  return curr >= (edge - digit) / 10
}

const MAX_NEG_ABS = 2 ** 31
const MAX_POS_ABS = MAX_NEG_ABS - 1
// @lc code=end
