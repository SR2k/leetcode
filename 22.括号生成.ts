/*
 * @lc app=leetcode.cn id=22 lang=typescript
 *
 * [22] 括号生成
 *
 * https://leetcode.cn/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (77.51%)
 * Likes:    2809
 * Dislikes: 0
 * Total Accepted:    569.2K
 * Total Submissions: 734.3K
 * Testcase Example:  '3'
 *
 * 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 3
 * 输出：["((()))","(()())","(())()","()(())","()()()"]
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：["()"]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 8
 *
 *
 */

export
// @lc code=start
function generateParenthesis(n: number, curr: string[] = [], openCount = 0, result: string[] = []): string[] {
  if (curr.length === n * 2) {
    result.push(curr.join(''))
    return result
  }

  // can open
  const total = n * 2
  const emptyPositions = total - curr.length - openCount
  if (emptyPositions) {
    curr.push('(')
    generateParenthesis(n, curr, openCount + 1, result)
    curr.pop()
  }

  // can close
  if (openCount) {
    curr.push(')')
    generateParenthesis(n, curr, openCount - 1, result)
    curr.pop()
  }

  return result
}
// @lc code=end
