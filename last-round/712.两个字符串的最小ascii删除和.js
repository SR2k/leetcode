/*
 * @lc app=leetcode.cn id=712 lang=javascript
 *
 * [712] 两个字符串的最小ASCII删除和
 *
 * https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
 *
 * algorithms
 * Medium (66.01%)
 * Likes:    214
 * Dislikes: 0
 * Total Accepted:    11.3K
 * Total Submissions: 17.1K
 * Testcase Example:  '"sea"\n"eat"'
 *
 * 给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。
 * 
 * 示例 1:
 * 
 * 
 * 输入: s1 = "sea", s2 = "eat"
 * 输出: 231
 * 解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
 * 在 "eat" 中删除 "t" 并将 116 加入总和。
 * 结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: s1 = "delete", s2 = "leet"
 * 输出: 403
 * 解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
 * 将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
 * 结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
 * 如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
 * 
 * 
 * 注意:
 * 
 * 
 * 0 < s1.length, s2.length <= 1000。
 * 所有字符串中的字符ASCII值在[97, 122]之间。
 * 
 * 
 */

// @lc code=start
/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var minimumDeleteSum = function(s1, s2) {
  const m = s1.length, n = s2.length

  let r
  if (!m) r = s2
  if (!n) r = s1
  if (r) {
    let sum = 0
    for (const c of r) sum += c.charCodeAt(0)
    return sum
  }

  const dp = []
  for (let i = 0; i < m; i++) {
    dp[i] = []

    for (let j = 0; j < n; j++) {
      if (i === 0 && j === 0) {
        dp[i][j] = s1[i] === s2[j] ? s1.charCodeAt(i) : 0
      } else if (i === 0) {
        dp[i][j] = s1[i] === s2[j] ? s1.charCodeAt(i) : dp[i][j - 1]
      } else if (j === 0) {
        dp[i][j] = s1[i] === s2[j] ? s1.charCodeAt(i) : dp[i - 1][j]
      } else if (s1[i] === s2[j]) {
        dp[i][j] = dp[i - 1][j - 1] + s1.charCodeAt(i)
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1])
      }
    }
  }

  let sum = 0
  for (const c of s1) sum += c.charCodeAt(0)
  for (const c of s2) sum += c.charCodeAt(0)

  return sum - dp[m - 1][n - 1] * 2
};
// @lc code=end
