/*
 * @lc app=leetcode.cn id=316 lang=typescript
 *
 * [316] 去除重复字母
 *
 * https://leetcode-cn.com/problems/remove-duplicate-letters/description/
 *
 * algorithms
 * Medium (47.80%)
 * Likes:    662
 * Dislikes: 0
 * Total Accepted:    77.6K
 * Total Submissions: 162.2K
 * Testcase Example:  '"bcabc"'
 *
 * 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "bcabc"
 * 输出："abc"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "cbacdcbc"
 * 输出："acdb"
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^4
 * s 由小写英文字母组成
 *
 *
 *
 *
 * 注意：该题与 1081
 * https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
 * 相同
 *
 */

export
// @lc code=start
function removeDuplicateLetters(s: string): string {
  const counter: Record<string, number> = {}
  for (const char of s) {
    counter[char] = (counter[char] || 0) + 1
  }

  const seen = new Set<string>()
  const stack: number[] = []
  for (let i = 0; i < s.length; i++) {
    const char = s[i]

    if (!seen.has(char)) {
      while (stack.length && s[stack[stack.length - 1]] > char && counter[s[stack[stack.length - 1]]]) {
        const prev = stack.pop()!
        seen.delete(s[prev])
      }
      stack.push(i)
      seen.add(char)
    }

    counter[char]--
  }

  return stack.map((i) => s[i]).join('')
}
// @lc code=end
