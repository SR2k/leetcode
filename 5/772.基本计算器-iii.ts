/*
 * @lc app=leetcode.cn id=772 lang=typescript
 *
 * [772] 基本计算器 III
 *
 * https://leetcode.cn/problems/basic-calculator-iii/description/
 *
 * algorithms
 * Hard (51.08%)
 * Likes:    119
 * Dislikes: 0
 * Total Accepted:    8.9K
 * Total Submissions: 17.5K
 * Testcase Example:  '"1+1"'
 *
 * 实现一个基本的计算器来计算简单的表达式字符串。
 *
 * 表达式字符串只包含非负整数，算符 +、-、*、/ ，左括号 ( 和右括号 ) 。整数除法需要 向下截断 。
 *
 * 你可以假定给定的表达式总是有效的。所有的中间结果的范围为 [-2^31, 2^31 - 1] 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "1+1"
 * 输出：2
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "6-4/2"
 * 输出：4
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "2*(5+5*2)/3+(6/2+8)"
 * 输出：21
 *
 *
 * 示例 4：
 *
 *
 * 输入：s = "(2+6*3+5-(3*14/7+2)*5)+3"
 * 输出：-12
 *
 *
 * 示例 5：
 *
 *
 * 输入：s = "0"
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * s 由整数、'+'、'-'、'*'、'/'、'(' 和 ')' 组成
 * s 是一个 有效的 表达式
 *
 *
 *
 *
 * 进阶：你可以在不使用内置库函数的情况下解决此问题吗？
 *
 */

// @lc code=start
const CHAR_CODE_0 = '0'.charCodeAt(0)
const CHAR_CODE_9 = '9'.charCodeAt(0)

const divide = (a: number, b: number) => {
  if ((a >= 0 && b > 0) || (a <= 0 && b < 0)) {
    return Math.floor(a / b)
  }
  return -Math.floor(Math.abs(a) / Math.abs(b))
}

const calculatePart = (s: string, begin: number): [number, number] => {
  let i = begin
  const nums: number[] = []

  let prevSign = '+'
  let buffer = 0

  const add2StackAndClear = () => {
    switch (prevSign) {
      case '+':
        nums.push(buffer)
        break
      case '-':
        nums.push(-buffer)
        break
      case '*':
        nums.push(nums.pop()! * buffer)
        break
      case '/':
        nums.push(divide(nums.pop()!, buffer))
    }

    buffer = 0
  }

  while (i < s.length) {
    const char = s[i]

    if (CHAR_CODE_0 <= char.charCodeAt(0) && char.charCodeAt(0) <= CHAR_CODE_9) {
      buffer = buffer * 10 + Number(char)
    } else if (char === '(') {
      [buffer, i] = calculatePart(s, i + 1)
    } else if (char === ')') {
      break
    } else {
      add2StackAndClear()
      prevSign = char
    }

    i++
  }

  add2StackAndClear()
  return [nums.reduce((sum, curr) => sum + curr, 0), i]
}

function calculate(s: string): number {
  return calculatePart(s, 0)[0]
}
// @lc code=end

console.log(calculate('(2+6*3+5-(3*14/7+2)*5)+3'), -12)
