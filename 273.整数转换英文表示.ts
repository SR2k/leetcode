/*
 * @lc app=leetcode.cn id=273 lang=typescript
 *
 * [273] 整数转换英文表示
 *
 * https://leetcode.cn/problems/integer-to-english-words/description/
 *
 * algorithms
 * Hard (36.47%)
 * Likes:    291
 * Dislikes: 0
 * Total Accepted:    34.9K
 * Total Submissions: 95.7K
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

// @lc code=start
const ONES = [
  '',
  'One', 'Two', 'Three', 'Four', 'Five',
  'Six', 'Seven', 'Eight', 'Nine', 'Ten',
  'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
  'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen',
]

const TENS = [
  '', '', 'Twenty', 'Thirty', 'Forty', 'Fifty',
  'Sixty', 'Seventy', 'Eighty', 'Ninety',
]

const UNITS = ['Billion', 'Million', 'Thousand', 'Hundred']
const UNIT_SCALES = [1e9, 1e6, 1e3, 100]

function numberToWords(num: number): string {
  return helper(num).join(' ') || 'Zero'
}

function helper(n: number): string[] {
  const result: string[] = []

  for (let i = 0; i < UNIT_SCALES.length; i++) {
    const unit = UNITS[i], scale = UNIT_SCALES[i]
    if (n < scale) {
      continue
    }

    const currResult = helper((n / scale) | 0)

    if (currResult.length) {
      result.push(...currResult, unit)
    }

    n %= scale
  }

  if (n >= 20) {
    result.push(TENS[(n / 10) | 0])
    n %= 10
  }
  result.push(ONES[n])

  return result.filter(Boolean)
}
// @lc code=end

export {}
