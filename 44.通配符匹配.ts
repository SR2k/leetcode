/*
 * @lc app=leetcode.cn id=44 lang=typescript
 *
 * [44] 通配符匹配
 *
 * https://leetcode.cn/problems/wildcard-matching/description/
 *
 * algorithms
 * Hard (33.56%)
 * Likes:    930
 * Dislikes: 0
 * Total Accepted:    116.8K
 * Total Submissions: 348.1K
 * Testcase Example:  '"aa"\n"a"'
 *
 * 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
 *
 * '?' 可以匹配任何单个字符。
 * '*' 可以匹配任意字符串（包括空字符串）。
 *
 *
 * 两个字符串完全匹配才算匹配成功。
 *
 * 说明:
 *
 *
 * s 可能为空，且只包含从 a-z 的小写字母。
 * p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
 *
 *
 * 示例 1:
 *
 * 输入:
 * s = "aa"
 * p = "a"
 * 输出: false
 * 解释: "a" 无法匹配 "aa" 整个字符串。
 *
 * 示例 2:
 *
 * 输入:
 * s = "aa"
 * p = "*"
 * 输出: true
 * 解释: '*' 可以匹配任意字符串。
 *
 *
 * 示例 3:
 *
 * 输入:
 * s = "cb"
 * p = "?a"
 * 输出: false
 * 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
 *
 *
 * 示例 4:
 *
 * 输入:
 * s = "adceb"
 * p = "*a*b"
 * 输出: true
 * 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
 *
 *
 * 示例 5:
 *
 * 输入:
 * s = "acdcb"
 * p = "a*c?b"
 * 输出: false
 *
 */

export
// @lc code=start
function isMatch(s: string, p: string): boolean {
  const m = s.length, n = p.length
  const dp = generateArray(
    m + 1,
    () => generateArray(n + 1, () => false),
  )

  for (let i = 0; i <= m; i++) {
    const si = i - 1

    for (let j = 0; j <= n; j++) {
      const pj = j - 1

      if (i === 0) {
        dp[i][j] = j === 0 || (dp[i][j - 1] && p[pj] === '*')
      } else if (j === 0) {
        dp[i][j] = false
      } else if (p[pj] === '*') {
        dp[i][j] = dp[i][j - 1] // match 0
          || dp[i - 1][j] // match 1+
      } else {
        dp[i][j] = dp[i - 1][j - 1] && isCharMatch(s[si], p[pj])
      }
    }
  }

  return dp[m][n]
}

function isCharMatch(c: string, p: string) {
  return c === p || p === '?'
}

function generateArray<T>(n: number, generator: (i: number) => T) {
  return new Array(n).fill(0).map((_, i) => generator(i))
}
// @lc code=end

console.log(isMatch('aa', 'a'))
console.log(isMatch('aa', '*'))
console.log(isMatch('cb', '?a'))
console.log(isMatch('adceb', '*a*b'))
console.log(isMatch('acdcb', 'a*c?b'))
