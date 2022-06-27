/*
 * @lc app=leetcode.cn id=43 lang=typescript
 *
 * [43] 字符串相乘
 *
 * https://leetcode.cn/problems/multiply-strings/description/
 *
 * algorithms
 * Medium (44.82%)
 * Likes:    962
 * Dislikes: 0
 * Total Accepted:    234K
 * Total Submissions: 522K
 * Testcase Example:  '"2"\n"3"'
 *
 * 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
 *
 * 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: num1 = "2", num2 = "3"
 * 输出: "6"
 *
 * 示例 2:
 *
 *
 * 输入: num1 = "123", num2 = "456"
 * 输出: "56088"
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= num1.length, num2.length <= 200
 * num1 和 num2 只能由数字组成。
 * num1 和 num2 都不包含任何前导零，除了数字0本身。
 *
 *
 */

export
// @lc code=start
function multiply(num1: string, num2: string): string {
  if (num1 === '0' || num2 === '0') {
    return '0'
  }

  const charCodeOfZero = '0'.charCodeAt(0)
  const result = new Array(num1.length + num2.length).fill(0)

  for (let i = 0; i < num1.length; i++) {
    const digit1 = num1.charCodeAt(num1.length - i - 1) - charCodeOfZero

    for (let j = 0; j < num2.length; j++) {
      const digit2 = num2.charCodeAt(num2.length - j - 1) - charCodeOfZero
      result[i + j] += digit1 * digit2
    }
  }

  let carry = 0
  for (let i = 0; i < result.length; i++) {
    result[i] += carry
    carry = Math.floor(result[i] / 10)
    result[i] %= 10
  }

  while (result[result.length - 1] === 0) {
    result.pop()
  }

  result.reverse()
  return result.join('')
}
// @lc code=end
