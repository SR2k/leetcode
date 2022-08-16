/*
 * @lc app=leetcode.cn id=273 lang=typescript
 *
 * [273] 整数转换英文表示
 *
 * https://leetcode.cn/problems/integer-to-english-words/description/
 *
 * algorithms
 * Hard (36.49%)
 * Likes:    282
 * Dislikes: 0
 * Total Accepted:    33.2K
 * Total Submissions: 91.1K
 * Testcase Example:  '123'
 *
 * 将非负整数 num 转换为其对应的英文表示。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：num = 123
 * 输出："One Hundred Twenty Three"
 *
 *
 * 示例 2：
 *
 *
 * 输入：num = 12345
 * 输出："Twelve Thousand Three Hundred Forty Five"
 *
 *
 * 示例 3：
 *
 *
 * 输入：num = 1234567
 * 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
 * Seven"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= num <= 2^31 - 1
 *
 *
 */

export
// @lc code=start
function numberToWords(num: number): string {
  return convert(num).filter(Boolean).join(' ') || ZERO
}

function convert(num: number): string[] {
  if (num === 0) return []
  if (num < ONES.length) return [ONES[num]]

  if (num < DIVIDERS[0]) {
    const tens = Math.floor(num / 10)
    return [TENS[tens], ...convert(num % 10)]
  }

  let result: string[] = []

  for (let i = 0; i < UNITS.length; i++) {
    const divider = DIVIDERS[i], unit = UNITS[i]
    if (!num) {
      break
    }

    const part = num % divider
    num = Math.floor(num / divider)

    const partResult = convert(part)
    if (partResult.length) {
      result = [...partResult, unit, ...result]
    }
  }

  return result
}

const ZERO = 'Zero'

const ONES = [
  '',
  'One', 'Two', 'Three', 'Four', 'Five',
  'Six', 'Seven', 'Eight', 'Nine', 'Ten',
  'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
  'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen',
]

const TENS = [
  '', '',
  'Twenty', 'Thirty', 'Forty', 'Fifty',
  'Sixty', 'Seventy', 'Eighty', 'Ninety',
]

const UNITS = [
  '', 'Hundred', 'Thousand', 'Million', 'Billion',
]

const DIVIDERS = [
  1e2, 1e1, 1e3, 1e3, 1e9,
]
// @lc code=end

console.log(numberToWords(0))
console.log(numberToWords(123))
console.log(numberToWords(12345))
console.log(numberToWords(1230007))
console.log(numberToWords(1_123_456_789))

// 123
// 1 23
