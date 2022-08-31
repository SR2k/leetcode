/*
 * @lc app=leetcode.cn id=438 lang=typescript
 *
 * [438] 找到字符串中所有字母异位词
 *
 * https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/
 *
 * algorithms
 * Medium (54.76%)
 * Likes:    988
 * Dislikes: 0
 * Total Accepted:    223.5K
 * Total Submissions: 408.3K
 * Testcase Example:  '"cbaebabacd"\n"abc"'
 *
 * 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
 *
 * 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: s = "cbaebabacd", p = "abc"
 * 输出: [0,6]
 * 解释:
 * 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
 * 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 *
 *
 * 示例 2:
 *
 *
 * 输入: s = "abab", p = "ab"
 * 输出: [0,1,2]
 * 解释:
 * 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
 * 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
 * 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= s.length, p.length <= 3 * 10^4
 * s 和 p 仅包含小写字母
 *
 *
 */

export
// @lc code=start
function findAnagrams(s: string, p: string): number[] {
  const counter: Record<string, number> = {}
  let diff = 0
  for (const char of p) {
    if (!counter[char]) diff++
    counter[char] = (counter[char] || 0) - 1
  }

  const result: number[] = []
  for (let i = 0; i < s.length; i++) {
    const char = s[i]
    counter[char] = (counter[char] || 0) + 1
    if (!counter[char]) diff--
    if (counter[char] === 1) diff++

    if (i >= p.length) {
      const head = s[i - p.length]
      counter[head] = (counter[head] || 0) - 1
      if (!counter[head]) diff--
      if (counter[head] === -1) diff++
    }

    if (!diff) {
      result.push(i - p.length + 1)
    }
  }

  return result
}
// @lc code=end
