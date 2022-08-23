/*
 * @lc app=leetcode.cn id=243 lang=typescript
 *
 * [243] 最短单词距离
 *
 * https://leetcode.cn/problems/shortest-word-distance/description/
 *
 * algorithms
 * Easy (66.55%)
 * Likes:    93
 * Dislikes: 0
 * Total Accepted:    13.3K
 * Total Submissions: 20.1K
 * Testcase Example:  '["practice", "makes", "perfect", "coding", "makes"]\n"coding"\n"practice"'
 *
 * 给定一个字符串数组 wordDict 和两个已经存在于该数组中的不同的字符串 word1 和 word2 。返回列表中这两个单词之间的最短距离。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 =
 * "coding", word2 = "practice"
 * 输出: 3
 *
 *
 * 示例 2:
 *
 *
 * 输入: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 =
 * "makes", word2 = "coding"
 * 输出: 1
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= wordsDict.length <= 3 * 10^4
 * 1 <= wordsDict[i].length <= 10
 * wordsDict[i] 由小写英文字母组成
 * word1 和 word2 在 wordsDict 中
 * word1 != word2
 *
 *
 */

export
// @lc code=start
function shortestDistance(wordsDict: string[], word1: string, word2: string): number {
  const positions: Record<string, number[]> = {}
  wordsDict.forEach((w, i) => {
    positions[w] = positions[w] || []
    positions[w].push(i)
  })

  const pos1 = positions[word1]
  const pos2 = positions[word2]

  pos1.unshift(Number.MIN_SAFE_INTEGER)
  pos1.push(Number.MAX_SAFE_INTEGER)

  let result = Number.MAX_SAFE_INTEGER
  let i = 0
  for (let j = 0; j < pos2.length; j++) {
    while (pos1[i + 1] < pos2[j]) {
      i++
    }

    result = Math.min(
      pos1[i + 1] - pos2[j],
      pos2[j] - pos1[i],
      result,
    )
  }

  return result
}
// @lc code=end
