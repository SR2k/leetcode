/*
 * @lc app=leetcode.cn id=340 lang=typescript
 *
 * [340] 至多包含 K 个不同字符的最长子串
 *
 * https://leetcode.cn/problems/longest-substring-with-at-most-k-distinct-characters/description/
 *
 * algorithms
 * Medium (50.82%)
 * Likes:    209
 * Dislikes: 0
 * Total Accepted:    20.9K
 * Total Submissions: 41.2K
 * Testcase Example:  '"eceba"\n2'
 *
 * 给你一个字符串 s 和一个整数 k ，请你找出 至多 包含 k 个 不同 字符的最长子串，并返回该子串的长度。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "eceba", k = 2
 * 输出：3
 * 解释：满足题目要求的子串是 "ece" ，长度为 3 。
 *
 * 示例 2：
 *
 *
 * 输入：s = "aa", k = 1
 * 输出：2
 * 解释：满足题目要求的子串是 "aa" ，长度为 2 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 5 * 10^4
 * 0 <= k <= 50
 *
 *
 */

export
// @lc code=start
function lengthOfLongestSubstringKDistinct(s: string, k: number): number {
  const counter: Record<string, number> = {}
  let charCount = 0
  let result = 0

  let j = 0
  for (let i = 0; i < s.length; i++) {
    counter[s[i]] = counter[s[i]] || 0

    if (++counter[s[i]] === 1) {
      charCount++
    }

    while (charCount > k) {
      if (--counter[s[j]] === 0) {
        charCount--
      }
      j++
    }

    result = Math.max(result, i - j + 1)
  }

  return result
}
// @lc code=end
