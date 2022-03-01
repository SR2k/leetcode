/*
 * @lc app=leetcode.cn id=273 lang=typescript
 *
 * [273] 整数转换英文表示
 *
 * https://leetcode-cn.com/problems/integer-to-english-words/description/
 *
 * algorithms
 * Hard (31.09%)
 * Likes:    199
 * Dislikes: 0
 * Total Accepted:    19.8K
 * Total Submissions: 56K
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
 * 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 *
 *
 * 示例 4：
 *
 *
 * 输入：num = 1234567891
 * 输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
 * Thousand Eight Hundred Ninety One"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0
 *
 *
 */

export
// @lc code=start
function numberToWords(num: number): string {
  const cut = []
  while (num) {
    cut.push(num % 1000)
    num = Math.floor(num / 1000)
  }

  let result: string[] = []
  cut.forEach((part, i) => {
    if (!part) return

    const temp: string[] = []
    partToEnglish(part, temp)
    temp.push(UNITS[i])

    result = temp.concat(result)
  })

  if (!result.length) return 'Zero'
  return result.filter(Boolean).join(' ')
}

const UNITS = ['', 'Thousand', 'Million', 'Billion']
const ONES = [
  '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
  'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
  'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
  'Eighteen', 'Nineteen',
]
const TENS = [
  '', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
  'Seventy', 'Eighty', 'Ninety',
]

function partToEnglish(n: number, result: string[]) {
  if (n >= 100) {
    const h = Math.floor(n / 100)
    result.push(ONES[h])
    result.push('Hundred')
    n %= 100
  }

  if (n <= 19) {
    result.push(ONES[n])
    return
  }

  const t = Math.floor(n / 10)
  const o = n % 10
  result.push(TENS[t])
  result.push(ONES[o])
}
// @lc code=end
