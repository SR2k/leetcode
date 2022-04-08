/*
 * @lc app=leetcode.cn id=44 lang=typescript
 *
 * [44] 通配符匹配
 *
 * https://leetcode-cn.com/problems/wildcard-matching/description/
 *
 * algorithms
 * Hard (33.01%)
 * Likes:    824
 * Dislikes: 0
 * Total Accepted:    95.3K
 * Total Submissions: 288.6K
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
  const dp = new Array(s.length + 1).fill(0).map(() => new Array(p.length + 1).fill(false))

  for (let i = 0; i <= s.length; i++) {
    const charS = s[i - 1]

    for (let j = 0; j <= p.length; j++) {
      const charP = p[j - 1]

      if (j === 0) {
        dp[i][j] = i === 0
      } else if (i === 0) {
        dp[i][j] = dp[i][j - 1] && charP === '*'
      } else if (charP === '*') {
        dp[i][j] = dp[i][j - 1] || dp[i - 1][j - 1] || dp[i - 1][j]
      } else if (charP === '?') {
        dp[i][j] = dp[i - 1][j - 1]
      } else {
        dp[i][j] = charS === charP && dp[i - 1][j - 1]
      }
    }
  }

  return dp[s.length][p.length]
}
// @lc code=end

/*
p[i] === '*'
--> 不匹配 dp[i][j - 1]
--> 匹配1个 dp[i - 1][j - 1]
--> 匹配多个 dp[i - 1][j]

p[i] === '?'
--> 匹配 dp[i - 1][j - 1]
 */
