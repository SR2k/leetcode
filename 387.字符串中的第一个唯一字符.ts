/*
 * @lc app=leetcode.cn id=387 lang=typescript
 *
 * [387] 字符串中的第一个唯一字符
 *
 * https://leetcode.cn/problems/first-unique-character-in-a-string/description/
 *
 * algorithms
 * Easy (55.31%)
 * Likes:    587
 * Dislikes: 0
 * Total Accepted:    327.2K
 * Total Submissions: 591.3K
 * Testcase Example:  '"leetcode"'
 *
 * 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入: s = "leetcode"
 * 输出: 0
 *
 *
 * 示例 2:
 *
 *
 * 输入: s = "loveleetcode"
 * 输出: 2
 *
 *
 * 示例 3:
 *
 *
 * 输入: s = "aabb"
 * 输出: -1
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= s.length <= 10^5
 * s 只包含小写字母
 *
 *
 */

export
// @lc code=start
function firstUniqChar(s: string): number {
  const lastSeen = new Array(26).fill(0)
  const CHAR_CODE_SMALL_A = 'a'.charCodeAt(0)

  for (let i = 0; i < s.length; i++) {
    lastSeen[s.charCodeAt(i) - CHAR_CODE_SMALL_A]++
  }
  for (let i = 0; i < s.length; i++) {
    if (lastSeen[s.charCodeAt(i) - CHAR_CODE_SMALL_A] === 1) {
      return i
    }
  }
  return -1
}
// @lc code=end
