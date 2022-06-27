/*
 * @lc app=leetcode.cn id=273 lang=typescript
 *
 * [273] 整数转换英文表示
 *
 * https://leetcode.cn/problems/integer-to-english-words/description/
 *
 * algorithms
 * Hard (36.49%)
 * Likes:    276
 * Dislikes: 0
 * Total Accepted:    33K
 * Total Submissions: 90.3K
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
  const result = helper(num)
  if (!result.length) {
    return DIGIT_MAP[0]
  }

  return result.join(' ')
}

const DIGIT_MAP = [
  'Zero',
  'One', 'Two', 'Three', 'Four', 'Five',
  'Six', 'Seven', 'Eight', 'Nine', 'Ten',
  'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
  'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen',
]

const TENS_MAP = [
  '',
  'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty',
  'Sixty', 'Seventy', 'Eighty', 'Ninety',
]

const UNITS_MAP: Record<number, string> = {
  [10 ** 9]: 'Billion',
  [10 ** 6]: 'Million',
  [10 ** 3]: 'Thousand',
  [10 ** 2]: 'Hundred',
}

const SPLIT_POINTS = [10 ** 9, 10 ** 6, 10 ** 3, 10 ** 2]

function helper(num: number): string[] {
  if (!num) return []

  if (num <= 19) {
    return [DIGIT_MAP[num]]
  }

  if (num < 100) {
    const tens = TENS_MAP[Math.floor(num / 10)]
    return [tens, ...helper(num % 10)]
  }

  const result = []
  for (const splitPoint of SPLIT_POINTS) {
    if (num < splitPoint) {
      continue
    }

    const higher = Math.floor(num / splitPoint)
    result.push(...helper(higher), UNITS_MAP[splitPoint], ...helper(num % splitPoint))
    break
  }

  return result
}
// @lc code=end

console.log(numberToWords(0))
console.log(numberToWords(123), '\nOne Hundred Twenty Three')
console.log(numberToWords(12345), '\nTwelve Thousand Three Hundred Forty Five')
console.log(numberToWords(1234567), '\nOne Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven')
