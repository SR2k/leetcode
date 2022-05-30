/*
 * @lc app=leetcode.cn id=166 lang=typescript
 *
 * [166] 分数到小数
 *
 * https://leetcode.cn/problems/fraction-to-recurring-decimal/description/
 *
 * algorithms
 * Medium (33.31%)
 * Likes:    383
 * Dislikes: 0
 * Total Accepted:    51.3K
 * Total Submissions: 154K
 * Testcase Example:  '1\n2'
 *
 * 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
 *
 * 如果小数部分为循环小数，则将循环的部分括在括号内。
 *
 * 如果存在多个答案，只需返回 任意一个 。
 *
 * 对于所有给定的输入，保证 答案字符串的长度小于 10^4 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：numerator = 1, denominator = 2
 * 输出："0.5"
 *
 *
 * 示例 2：
 *
 *
 * 输入：numerator = 2, denominator = 1
 * 输出："2"
 *
 *
 * 示例 3：
 *
 *
 * 输入：numerator = 4, denominator = 333
 * 输出："0.(012)"
 *
 *
 *
 *
 * 提示：
 *
 *
 * -2^31 <= numerator, denominator <= 2^31 - 1
 * denominator != 0
 *
 *
 */

// @lc code=start
function fractionToDecimal(numerator: number, denominator: number): string {
  if (numerator === 0) {
    return '0'
  }
  if ((numerator >= 0 && denominator < 0) || (numerator <= 0 && denominator > 0)) {
    return `-${fractionToDecimal(Math.abs(numerator), Math.abs(denominator))}`
  }

  const whole = String(Math.floor(numerator / denominator))
  numerator %= denominator

  const decimal = []
  const seen: Record<number, number> = {}
  let repeat = -1

  while (numerator) {
    numerator *= 10

    if (typeof seen[numerator] !== 'undefined') {
      repeat = seen[numerator]
      break
    }

    decimal.push(Math.floor(numerator / denominator))
    seen[numerator] = decimal.length - 1

    numerator %= denominator
  }

  if (!decimal.length) {
    return whole
  }
  if (repeat < 0) {
    return `${whole}.${decimal.join('')}`
  }

  return `${
    whole
  }.${
    decimal.slice(0, repeat).join('')
  }(${
    decimal.slice(repeat, decimal.length).join('')
  })`
}
// @lc code=end

console.log(fractionToDecimal(1, 2))
console.log(fractionToDecimal(2, 1))
console.log(fractionToDecimal(4, 333))
console.log(fractionToDecimal(1, -2))
console.log(fractionToDecimal(-2, 1))
console.log(fractionToDecimal(4, -333))
console.log(fractionToDecimal(4, 70))
console.log(fractionToDecimal(-4, 70))
console.log(fractionToDecimal(4, -70))
console.log(fractionToDecimal(0, -70))
