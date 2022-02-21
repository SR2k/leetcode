/*
 * @lc app=leetcode.cn id=227 lang=typescript
 *
 * [227] 基本计算器 II
 *
 * https://leetcode-cn.com/problems/basic-calculator-ii/description/
 *
 * algorithms
 * Medium (43.77%)
 * Likes:    518
 * Dislikes: 0
 * Total Accepted:    96.6K
 * Total Submissions: 220.5K
 * Testcase Example:  '"3+2*2"'
 *
 * 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
 *
 * 整数除法仅保留整数部分。
 *
 *
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
 * 1
 * s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
 * s 表示一个 有效表达式
 * 表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
 * 题目数据保证答案是一个 32-bit 整数
 *
 *
 *
 *
 */

export
// @lc code=start
function calculate(s: string): number {
  const stack: number[] = [0]
  let prevFlag = '+'
  let numTemp = 0

  s += '+0'

  for (const char of s) {
    if (char === ' ') {
      // nothing to do...
    } else if (isNumeric(char)) {
      numTemp = numTemp * 10 + Number(char)
    } else {
      if (prevFlag === '+') {
        stack.push(numTemp)
      } if (prevFlag === '-') {
        stack.push(-1 * numTemp)
      } else if (prevFlag === '*') {
        stack[stack.length - 1] *= numTemp
      } else if (prevFlag === '/') {
        stack[stack.length - 1] = wholeDivide(stack[stack.length - 1], numTemp)
      }

      numTemp = 0
      prevFlag = char
    }
  }

  return stack.reduce((prev, curr) => prev + curr, 0)
}

const CHAR_CODE_0 = '0'.charCodeAt(0)
const CHAR_CODE_9 = '9'.charCodeAt(0)

function isNumeric(char: string) {
  const charCode = char.charCodeAt(0)
  return charCode >= CHAR_CODE_0 && charCode <= CHAR_CODE_9
}

function wholeDivide(a: number, b: number) {
  if ((a > 0 && b > 0) || (a < 0 && b < 0)) {
    return Math.floor(a / b)
  }
  return Math.ceil(a / b)
}
// @lc code=end
