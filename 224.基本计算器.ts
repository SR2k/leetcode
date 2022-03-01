/*
 * @lc app=leetcode.cn id=224 lang=typescript
 *
 * [224] 基本计算器
 *
 * https://leetcode-cn.com/problems/basic-calculator/description/
 *
 * algorithms
 * Hard (41.79%)
 * Likes:    711
 * Dislikes: 0
 * Total Accepted:    80.4K
 * Total Submissions: 192.4K
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
  let prevSign: 1 | -1 = 1
  let parSign: 1 | -1 = 1
  let buffer = 0
  const signStack: Array<1 | -1> = []
  const nums: number[] = []

  s += '+0'

  for (const char of s) {
    if (isNumeric(char)) {
      buffer = buffer * 10 + (+char)
    } else if (char === '+' || char === '-') {
      nums.push(buffer * prevSign * parSign)
      buffer = 0
      prevSign = char === '+' ? 1 : -1
    } else if (char === '(') {
      signStack.push(prevSign)
      parSign *= prevSign
      prevSign = 1
    } else if (char === ')') {
      nums.push(buffer * prevSign * parSign)
      buffer = 0
      parSign *= signStack.pop()!
    }
  }

  return nums.reduce((prev, curr) => prev + curr, 0)
}

function isNumeric(s: string) {
  return s.charCodeAt(0) >= '0'.charCodeAt(0) && s.charCodeAt(0) <= '9'.charCodeAt(0)
}
// @lc code=end

/*
q = '-(1+(4+5+2)-3)+(6+8)'

-1 -4 -5 -2 3 6 8
 */
