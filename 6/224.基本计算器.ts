/*
 * @lc app=leetcode.cn id=224 lang=typescript
 *
 * [224] 基本计算器
 *
 * https://leetcode.cn/problems/basic-calculator/description/
 *
 * algorithms
 * Hard (41.97%)
 * Likes:    784
 * Dislikes: 0
 * Total Accepted:    93K
 * Total Submissions: 221.7K
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
  let buffer = 0
  let currSign = 1, globalSign = 1
  const signs: number[] = []
  const parts: number[] = []

  const CHAR_CODE_ZERO = '0'.charCodeAt(0)

  for (let i = 0; i <= s.length; i++) {
    const char = i < s.length ? s[i] : '+'

    if (char >= '0' && char <= '9') {
      buffer = buffer * 10 + char.charCodeAt(0) - CHAR_CODE_ZERO
      continue
    }

    if (buffer) {
      parts.push(currSign * globalSign * buffer)
      buffer = 0
    }

    if (char === '+') {
      currSign = 1
    } else if (char === '-') {
      currSign = -1
    } else if (char === '(') {
      signs.push(currSign)
      globalSign *= currSign
      currSign = 1
    } else if (char === ')') {
      globalSign *= signs.pop()!
      currSign = 1
    }
  }

  return parts.reduce((prev, curr) => prev + curr, 0)
}
// @lc code=end
