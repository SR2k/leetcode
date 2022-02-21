/*
 * @lc app=leetcode.cn id=43 lang=typescript
 *
 * [43] 字符串相乘
 *
 * https://leetcode-cn.com/problems/multiply-strings/description/
 *
 * algorithms
 * Medium (44.99%)
 * Likes:    833
 * Dislikes: 0
 * Total Accepted:    197.3K
 * Total Submissions: 438.7K
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
  if (num1 === '0' || num2 === '0') return '0'
  const result = new Array(num1.length + num2.length).fill(0)

  const n1 = [...num1].reverse()
  const n2 = [...num2].reverse()
  n1.forEach((d1, i) => {
    n2.forEach((d2, j) => {
      result[i + j] += (+d1) * (+d2)
    })
  })

  let carry = 0
  result.forEach((d, i) => {
    const r = carry + d
    result[i] = r % 10
    carry = Math.floor(r / 10)
  })

  while (result[result.length - 1] === 0) {
    result.pop()
  }
  return result.reverse().join('')
}
// @lc code=end

// 49 * 85 = 4165

// [0, 32, 92, 45]
// [4, 1, 6, 5]
