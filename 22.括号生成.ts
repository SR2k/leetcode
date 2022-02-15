/*
 * @lc app=leetcode.cn id=22 lang=typescript
 *
 * [22] 括号生成
 *
 * https://leetcode-cn.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (77.34%)
 * Likes:    2355
 * Dislikes: 0
 * Total Accepted:    420.5K
 * Total Submissions: 543.7K
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
  if (n === 0) return ['']
  if (n === 1) return ['()']
  if (cache[n]) return cache[n]

  const result = []
  for (let i = 0; i < n; i++) {
    const j = n - i - 1
    const resultI = generateParenthesis(i); const
      resultJ = generateParenthesis(j)

    for (const si of resultI) {
      for (const sj of resultJ) {
        result.push(`(${si})${sj}`)
      }
    }
  }

  cache[n] = result
  return result
}

const cache: Record<number, string[]> = {}
// @lc code=end
