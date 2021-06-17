/*
 * @lc app=leetcode.cn id=131 lang=javascript
 *
 * [131] 分割回文串
 *
 * https://leetcode-cn.com/problems/palindrome-partitioning/description/
 *
 * algorithms
 * Medium (72.53%)
 * Likes:    724
 * Dislikes: 0
 * Total Accepted:    107.3K
 * Total Submissions: 148K
 * Testcase Example:  '"aab"'
 *
 * 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
 * 
 * 回文串 是正着读和反着读都一样的字符串。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "aab"
 * 输出：[["a","a","b"],["aa","b"]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "a"
 * 输出：[["a"]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * s 仅由小写英文字母组成
 * 
 * 
 */

// @lc code=start
/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
  const ret = []

  const dp = []
  for (let i = s.length - 1; i >= 0; i--) {
    dp[i] = []

    for (let j = i; j < s.length; j++) {
      if (i === j) {
        dp[i][j] = true
      } else if (j - i === 1) {
        dp[i][j] = s[i] === s[j]
      } else {
        dp[i][j] = (dp[i + 1][j - 1] && s[i] === s[j]) || false
      }
    }
  }

  const dfs = (fromIndex, index, currentPalindromes) => {
    if (index === s.length && fromIndex === s.length) ret.push(currentPalindromes)
    if (index >= s.length) return

    // 取
    const subString = s.slice(fromIndex, index + 1)
    if (dp[fromIndex][index]) {
      dfs(index + 1, index + 1, [...currentPalindromes, subString])
    }

    // 不取
    dfs(fromIndex, index + 1, currentPalindromes)
  }
  dfs(0, 0, [])

  return ret
};
// @lc code=end

