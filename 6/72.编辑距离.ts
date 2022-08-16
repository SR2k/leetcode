/*
 * @lc app=leetcode.cn id=72 lang=typescript
 *
 * [72] 编辑距离
 *
 * https://leetcode.cn/problems/edit-distance/description/
 *
 * algorithms
 * Hard (62.40%)
 * Likes:    2447
 * Dislikes: 0
 * Total Accepted:    270.6K
 * Total Submissions: 433.7K
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
  let dp: number[] = new Array(word2.length + 1).fill(Number.MAX_SAFE_INTEGER)

  for (let i = 0; i <= word1.length; i++) {
    const curr = dp.map((x) => x)

    for (let j = 0; j <= word2.length; j++) {
      if (i === 0 || j === 0) {
        curr[j] = i || j
      } else if (word1[i - 1] === word2[j - 1]) {
        curr[j] = Math.min(dp[j - 1], dp[j] + 1, curr[j - 1] + 1)
      } else {
        curr[j] = Math.min(dp[j - 1] + 1, dp[j] + 1, curr[j - 1] + 1)
      }
    }

    dp = curr
  }

  return dp[word2.length]
}
// @lc code=end
