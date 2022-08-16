/*
 * @lc app=leetcode.cn id=227 lang=typescript
 *
 * [227] 基本计算器 II
 *
 * https://leetcode.cn/problems/basic-calculator-ii/description/
 *
 * algorithms
 * Medium (44.07%)
 * Likes:    585
 * Dislikes: 0
 * Total Accepted:    117.7K
 * Total Submissions: 267.1K
 * Testcase Example:  '"3+2*2"'
 *
 * 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
 *
 * 整数除法仅保留整数部分。
 *
 * 你可以假设给定的表达式总是有效的。所有中间结果将在 [-2^31, 2^31 - 1] 的范围内。
 *
 * 注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "3+2*2"
 * 输出：7
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = " 3/2 "
 * 输出：1
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = " 3+5 / 2 "
 * 输出：5
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 3 * 10^5
 * s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
 * s 表示一个 有效表达式
 * 表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
 * 题目数据保证答案是一个 32-bit 整数
 *
 *
 */

export
// @lc code=start
function calculate(s: string): number {
  const stack: number[] = []

  let buffer = 0
  let prevSign = Sign.Add

  for (let i = 0; i <= s.length; i++) {
    const char = i === s.length ? Sign.Add : s[i];

    if (isNumeric(char)) {
      buffer = buffer * 10 + s.charCodeAt(i) - CHAR_CODE_ZERO;
    } else if (isSign(char)) {
      if (prevSign === Sign.Add) {
        stack.push(buffer)
      } else if (prevSign === Sign.Subtract) {
        stack.push(-buffer)
      } else if (prevSign === Sign.Multiple) {
        stack.push(stack.pop()! * buffer)
      } else {
        stack.push(divide(stack.pop()!, buffer))
      }

      buffer = 0
      prevSign = char as Sign
    }
  }

  return stack.reduce((prev, curr) => prev + curr, 0)
}

const divide = (a: number, b: number) => {
  const result = Math.floor(Math.abs(a) / Math.abs(b))
  if ((a <= 0 && b < 0) || (a >= 0 && b > 0)) {
    return result
  }
  return -result
}

const isNumeric = (s: string) => (s >= '0' && s <= '9')

const isSign = (s: string) => signs.includes(s as any)

const CHAR_CODE_ZERO = '0'.charCodeAt(0)

enum Sign {
  Add = '+',
  Subtract = '-',
  Multiple = '*',
  Divide = '/',
}

const signs = Object.values(Sign)
// @lc code=end
