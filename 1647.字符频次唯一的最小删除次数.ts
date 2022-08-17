/*
 * @lc app=leetcode.cn id=1647 lang=typescript
 *
 * [1647] 字符频次唯一的最小删除次数
 *
 * https://leetcode.cn/problems/minimum-deletions-to-make-character-frequencies-unique/description/
 *
 * algorithms
 * Medium (53.55%)
 * Likes:    47
 * Dislikes: 0
 * Total Accepted:    10.3K
 * Total Submissions: 19.2K
 * Testcase Example:  '"aab"'
 *
 * 如果字符串 s 中 不存在 两个不同字符 频次 相同的情况，就称 s 是 优质字符串 。
 *
 * 给你一个字符串 s，返回使 s 成为 优质字符串 需要删除的 最小 字符数。
 *
 * 字符串中字符的 频次 是该字符在字符串中的出现次数。例如，在字符串 "aab" 中，'a' 的频次是 2，而 'b' 的频次是 1 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "aab"
 * 输出：0
 * 解释：s 已经是优质字符串。
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "aaabbbcc"
 * 输出：2
 * 解释：可以删除两个 'b' , 得到优质字符串 "aaabcc" 。
 * 另一种方式是删除一个 'b' 和一个 'c' ，得到优质字符串 "aaabbc" 。
 *
 * 示例 3：
 *
 *
 * 输入：s = "ceabaacb"
 * 输出：2
 * 解释：可以删除两个 'c' 得到优质字符串 "eabaab" 。
 * 注意，只需要关注结果字符串中仍然存在的字符。（即，频次为 0 的字符会忽略不计。）
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * s 仅含小写英文字母
 *
 *
 */

export
// @lc code=start
function minDeletions(s: string): number {
  const counter = new Array(26).fill(0)
  for (const c of s) {
    counter[c.charCodeAt(0) - 'a'.charCodeAt(0)]++
  }
  const freqCounter: Record<number, number> = {}
  const freqSet = new Set<number>()
  for (const count of counter) {
    freqCounter[count] = (freqCounter[count] || 0) + 1
    freqSet.add(count)
  }
  const freq = [...freqSet]
  freq.sort((a, b) => a - b)

  let result = 0
  while (freq.length) {
    const currFreq = freq.pop()!
    const currCount = freqCounter[currFreq] || 0
    if (currFreq <= 0 || currCount <= 1) continue

    const nextFreq = currFreq - 1
    result += currCount - 1

    if (currCount > 1) {
      if (!freqCounter[nextFreq]) {
        freq.push(nextFreq)
        freqCounter[nextFreq] = 0
      }
      freqCounter[nextFreq] += currCount - 1
    }
  }

  return result
}
// @lc code=end
