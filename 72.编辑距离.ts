/*
 * @lc app=leetcode.cn id=72 lang=typescript
 *
 * [72] 编辑距离
 *
 * https://leetcode.cn/problems/edit-distance/description/
 *
 * algorithms
 * Hard (62.67%)
 * Likes:    2554
 * Dislikes: 0
 * Total Accepted:    295.4K
 * Total Submissions: 471.3K
 * Testcase Example:  '"horse"\n"ros"'
 *
 * 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
 *
 * 你可以对一个单词进行如下三种操作：
 *
 *
 * 插入一个字符
 * 删除一个字符
 * 替换一个字符
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：word1 = "horse", word2 = "ros"
 * 输出：3
 * 解释：
 * horse -> rorse (将 'h' 替换为 'r')
 * rorse -> rose (删除 'r')
 * rose -> ros (删除 'e')
 *
 *
 * 示例 2：
 *
 *
 * 输入：word1 = "intention", word2 = "execution"
 * 输出：5
 * 解释：
 * intention -> inention (删除 't')
 * inention -> enention (将 'i' 替换为 'e')
 * enention -> exention (将 'n' 替换为 'x')
 * exention -> exection (将 'n' 替换为 'c')
 * exection -> execution (插入 'u')
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= word1.length, word2.length <= 500
 * word1 和 word2 由小写英文字母组成
 *
 *
 */

export
// @lc code=start
function minDistance(word1: string, word2: string): number {
  const len1 = word1.length, len2 = word2.length
  const dp = new Array(len1 + 1).fill(0).map(() => (
    new Array(len2 + 1).fill(0)
  ))

  for (let i = 0; i <= len1; i++) {
    for (let j = 0; j <= len2; j++) {
      if (i === 0 || j === 0) {
        dp[i][j] = i || j
      } else if (word1[i - 1] === word2[j - 1]) {
        dp[i][j] = Math.min(
          dp[i - 1][j - 1],
          dp[i][j - 1] + 1,
          dp[i - 1][j] + 1,
        )
      } else {
        dp[i][j] = 1 + Math.min(
          dp[i - 1][j - 1],
          dp[i][j - 1],
          dp[i - 1][j],
        )
      }
    }
  }

  return dp[len1][len2]
}
// @lc code=end
