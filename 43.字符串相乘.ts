/*
 * @lc app=leetcode.cn id=43 lang=typescript
 *
 * [43] 字符串相乘
 *
 * https://leetcode.cn/problems/multiply-strings/description/
 *
 * algorithms
 * Medium (44.81%)
 * Likes:    1025
 * Dislikes: 0
 * Total Accepted:    250.4K
 * Total Submissions: 558.7K
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
  const l1 = num1.length, l2 = num2.length
  const result = new Array(l1 + l2).fill(0)

  for (let i = 0; i < l1; i++) {
    const d1 = l1 - i - 1
    const n1 = parseDigit(num1[d1])

    for (let j = 0; j < l2; j++) {
      const d2 = l2 - j - 1
      const n2 = parseDigit(num2[d2])

      result[i + j] += n1 * n2
    }
  }

  let carry = 0
  for (let i = 0; i < result.length; i++) {
    result[i] += carry
    carry = Math.floor(result[i] / 10)
    result[i] %= 10
  }
  while (result.length && result[result.length - 1] === 0) {
    result.pop()
  }

  result.reverse()
  return result.join('') || '0'
}

const parseDigit = (char: string) => char.charCodeAt(0) - '0'.charCodeAt(0)
// @lc code=end
