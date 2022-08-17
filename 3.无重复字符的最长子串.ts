/*
 * @lc app=leetcode.cn id=3 lang=typescript
 *
 * [3] 无重复字符的最长子串
 *
 * https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (38.97%)
 * Likes:    8012
 * Dislikes: 0
 * Total Accepted:    1.9M
 * Total Submissions: 4.9M
 * Testcase Example:  '"abcabcbb"'
 *
 * 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: s = "abcabcbb"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
 *
 *
 * 示例 2:
 *
 *
 * 输入: s = "bbbbb"
 * 输出: 1
 * 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
 *
 *
 * 示例 3:
 *
 *
 * 输入: s = "pwwkew"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
 * 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= s.length <= 5 * 10^4
 * s 由英文字母、数字、符号和空格组成
 *
 *
 */

export
// @lc code=start
function lengthOfLongestSubstring(s: string): number {
  const counter: Record<string, number | undefined> = {}

  let result = 0
  let begin = 0

  for (let end = 0; end < s.length; end++) {
    const char = s[end]
    counter[char] = (counter[char] || 0) + 1

    while (counter[char]! > 1) {
      const beginChar = s[begin]
      counter[beginChar]!--
      begin++
    }

    result = Math.max(end - begin + 1, result)
  }

  return result
}
// @lc code=end
