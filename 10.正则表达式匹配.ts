/*
 * @lc app=leetcode.cn id=10 lang=typescript
 *
 * [10] 正则表达式匹配
 *
 * https://leetcode.cn/problems/regular-expression-matching/description/
 *
 * algorithms
 * Hard (31.69%)
 * Likes:    3152
 * Dislikes: 0
 * Total Accepted:    306.1K
 * Total Submissions: 966K
 * Testcase Example:  '"aa"\n"a"'
 *
 * 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
 *
 *
 * '.' 匹配任意单个字符
 * '*' 匹配零个或多个前面的那一个元素
 *
 *
 * 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "aa", p = "a"
 * 输出：false
 * 解释："a" 无法匹配 "aa" 整个字符串。
 *
 *
 * 示例 2:
 *
 *
 * 输入：s = "aa", p = "a*"
 * 输出：true
 * 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "ab", p = ".*"
 * 输出：true
 * 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 20
 * 1 <= p.length <= 30
 * s 只包含从 a-z 的小写字母。
 * p 只包含从 a-z 的小写字母，以及字符 . 和 *。
 * 保证每次出现字符 * 时，前面都匹配到有效的字符
 *
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
        dp[i][j] = j === 0 || (p[pj] === '*' && dp[i][j - 2])
      } else if (j === 0) {
        dp[i][j] = false
      } else if (p[pj] === '*') {
        dp[i][j] = dp[i][j - 2] // match 0
          || (dp[i - 1][j] && isCharMatch(s[si], p[pj - 1])) // match 1+
      } else {
        dp[i][j] = dp[i - 1][j - 1] && isCharMatch(s[si], p[pj])
      }
    }
  }

  return dp[m][n]
}

function isCharMatch(char: string, patternChar: string) {
  return char === patternChar || patternChar === '.'
}

function generateArray<T>(n: number, generator: (i: number) => T) {
  return new Array(n).fill(0).map((_, i) => generator(i))
}
// @lc code=end

// console.log(isMatch('aa', 'a'))
// console.log(isMatch('aa', 'a*'))
// console.log(isMatch('ab', '.*'))

console.log(isMatch('ab', 'a.*b'))
console.log(isMatch('ab', 'aa.*b'))

// 'aa'
// 'a*'

// aa
// a*
