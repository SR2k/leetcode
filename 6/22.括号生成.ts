/*
 * @lc app=leetcode.cn id=22 lang=typescript
 *
 * [22] 括号生成
 *
 * https://leetcode.cn/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (77.47%)
 * Likes:    2724
 * Dislikes: 0
 * Total Accepted:    533K
 * Total Submissions: 688K
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
function generateParenthesis(n: number): string[] {
  const result: string[] = []

  const helper = (temp: string[], open: number) => {
    if (temp.length === 2 * n) {
      if (open === 0) {
        result.push(temp.join(''))
      }
      return
    }

    // can open
    const leftPos = n * 2 - temp.length
    if (leftPos - open >= 2) {
      temp.push('(')
      helper(temp, open + 1)
      temp.pop()
    }

    // can close
    if (open) {
      temp.push(')')
      helper(temp, open - 1)
      temp.pop()
    }
  }

  helper([], 0)
  return result
}
// @lc code=end
