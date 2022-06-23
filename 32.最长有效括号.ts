/*
 * @lc app=leetcode.cn id=32 lang=typescript
 *
 * [32] 最长有效括号
 *
 * https://leetcode.cn/problems/longest-valid-parentheses/description/
 *
 * algorithms
 * Hard (36.54%)
 * Likes:    1873
 * Dislikes: 0
 * Total Accepted:    280.1K
 * Total Submissions: 765.3K
 * Testcase Example:  '"(()"'
 *
 * 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "(()"
 * 输出：2
 * 解释：最长有效括号子串是 "()"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = ")()())"
 * 输出：4
 * 解释：最长有效括号子串是 "()()"
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = ""
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0
 * s[i] 为 '(' 或 ')'
 *
 *
 *
 *
 */

export
// @lc code=start
function longestValidParentheses(s: string): number {
  const dp = new Array(s.length + 1).fill(0)
  let result = 0

  for (let i = 2; i <= s.length; i++) {
    const char = s[i - 1]

    if (char === ')') {
      const prevToMatch = i - 1 - dp[i - 1]
      if (s[prevToMatch - 1] === '(') {
        dp[i] = dp[i - 1] + 2 + dp[prevToMatch - 1]
      }
    }

    result = Math.max(result, dp[i])
  }

  return result
}
// @lc code=end

console.log(longestValidParentheses('(()'))
console.log(longestValidParentheses('()))())))(())('))
console.log(longestValidParentheses(')()())'))
console.log(longestValidParentheses(''))
