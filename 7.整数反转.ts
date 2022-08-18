/*
 * @lc app=leetcode.cn id=7 lang=typescript
 *
 * [7] 整数反转
 *
 * https://leetcode.cn/problems/reverse-integer/description/
 *
 * algorithms
 * Medium (35.37%)
 * Likes:    3598
 * Dislikes: 0
 * Total Accepted:    1.1M
 * Total Submissions: 3M
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
  const sign = x >= 0 ? 1 : -1
  x = Math.abs(x)

  let maxAbs = 2 ** 31
  if (sign > 0) maxAbs -= 1

  let result = 0
  while (x) {
    const d = x % 10
    if (result > (maxAbs - d) / 10) return 0
    result = result * 10 + d
    x = Math.floor(x / 10)
  }

  return result * sign
}
// @lc code=end
