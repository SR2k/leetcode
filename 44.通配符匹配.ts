/*
 * @lc app=leetcode.cn id=44 lang=typescript
 *
 * [44] 通配符匹配
 *
 * https://leetcode-cn.com/problems/wildcard-matching/description/
 *
 * algorithms
 * Hard (32.24%)
 * Likes:    690
 * Dislikes: 0
 * Total Accepted:    71.9K
 * Total Submissions: 222.8K
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

// @lc code=start
const isCharMatch = (char: string, patternChar: string) => {
  if (patternChar === '?') return true
  return char === patternChar
}

function isMatch(s: string, p: string): boolean {
  const dp: boolean[][] = []

  for (let i = 0; i <= s.length; i++) {
    const char = s[i - 1]
    dp[i] = []

    for (let j = 0; j <= p.length; j++) {
      const patternChar = p[j - 1]

      if (i === 0 && j === 0) {
        dp[i][j] = true
      } else if (j === 0) {
        dp[i][j] = false
      } else if (i === 0) {
        dp[i][j] = patternChar === '*' && dp[i][j - 1]
      } else if (patternChar === '*') {
        dp[i][j] = dp[i][j - 1] || dp[i - 1][j - 1] || dp[i - 1][j] 
      } else {
        dp[i][j] = dp[i - 1][j - 1] && isCharMatch(char, patternChar)
      }
    }
  }

  // console.log(dp)
  return dp[s.length][p.length]
};
// @lc code=end

// console.log(isMatch('aa', '*'))
