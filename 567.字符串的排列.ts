/*
 * @lc app=leetcode.cn id=567 lang=typescript
 *
 * [567] 字符串的排列
 *
 * https://leetcode.cn/problems/permutation-in-string/description/
 *
 * algorithms
 * Medium (44.16%)
 * Likes:    754
 * Dislikes: 0
 * Total Accepted:    218.7K
 * Total Submissions: 495.1K
 * Testcase Example:  '"ab"\n"eidbaooo"'
 *
 * 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
 *
 * 换句话说，s1 的排列之一是 s2 的 子串 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s1 = "ab" s2 = "eidbaooo"
 * 输出：true
 * 解释：s2 包含 s1 的排列之一 ("ba").
 *
 *
 * 示例 2：
 *
 *
 * 输入：s1= "ab" s2 = "eidboaoo"
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s1.length, s2.length <= 10^4
 * s1 和 s2 仅包含小写字母
 *
 *
 */

export
// @lc code=start
function checkInclusion(s1: string, s2: string): boolean {
  let diffCount = 0
  const counter: Record<string, number> = {}

  for (const char of s1) {
    counter[char] = (counter[char] || 0) + 1
    diffCount++
  }

  for (let i = 0; i < s2.length; i++) {
    const char = s2[i]
    if (counter[char] > 0) {
      diffCount--
    } else {
      diffCount++
    }
    counter[char] = (counter[char] || 0) - 1

    const prevBegin = i - s1.length
    if (prevBegin >= 0) {
      const prevChar = s2[prevBegin]
      if (counter[prevChar] < 0) {
        diffCount--
      } else {
        diffCount++
      }
      counter[prevChar] = (counter[prevChar] || 0) + 1
    }

    if (!diffCount) {
      return true
    }
  }

  return false
}
// @lc code=end
