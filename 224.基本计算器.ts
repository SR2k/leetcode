/*
 * @lc app=leetcode.cn id=224 lang=typescript
 *
 * [224] 基本计算器
 *
 * https://leetcode.cn/problems/basic-calculator/description/
 *
 * algorithms
 * Hard (42.12%)
 * Likes:    810
 * Dislikes: 0
 * Total Accepted:    100.1K
 * Total Submissions: 237.2K
 * Testcase Example:  '"1 + 1"'
 *
 * 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
 *
 * 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "1 + 1"
 * 输出：2
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = " 2-1 + 2 "
 * 输出：3
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "(1+(4+5+2)-3)+(6+8)"
 * 输出：23
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 3 * 10^5
 * s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
 * s 表示一个有效的表达式
 * '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
 * '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
 * 输入中不存在两个连续的操作符
 * 每个数字和运行的计算将适合于一个有符号的 32位 整数
 *
 *
 */

export
// @lc code=start
function calculate(s: string): number {
  let globalSign = 1
  let prevSign = 1
  let buffer = 0
  const signStack: number[] = []
  const nums: number[] = []

  for (let i = 0; i <= s.length; i++) {
    const char = i < s.length ? s[i] : '+'

    if (isNumeric(char)) {
      buffer = (buffer * 10) + s.charCodeAt(i) - CHAR_CODE_0
    } else if (isControlChar(char)) {
      if (buffer) {
        nums.push(globalSign * prevSign * buffer)
      }
      buffer = 0

      if (char === ControlChars.Add) {
        prevSign = 1
      } else if (char === ControlChars.Subtract) {
        prevSign = -1
      } else if (char === ControlChars.OpenBracket) {
        signStack.push(prevSign)
        globalSign *= prevSign
        prevSign = 1
      } else if (char === ControlChars.ClosingBracket) {
        globalSign *= signStack.pop()!
        prevSign = 1
      }
    }
  }

  return nums.reduce((prev, n) => prev + n, 0)
}

const CHAR_CODE_0 = '0'.charCodeAt(0)
const CHAR_CODE_9 = '9'.charCodeAt(0)

function isNumeric(char: string) {
  const c = char.charCodeAt(0)
  return c <= CHAR_CODE_9 && c >= CHAR_CODE_0
}

enum ControlChars {
  Add = '+',
  Subtract = '-',
  OpenBracket = '(',
  ClosingBracket = ')',
}

const controlCharSet = new Set<ControlChars>(Object.values(ControlChars))

const isControlChar = (char: string): char is ControlChars => controlCharSet.has(char as any)
// @lc code=end
