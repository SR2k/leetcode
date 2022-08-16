/*
 * @lc app=leetcode.cn id=76 lang=typescript
 *
 * [76] 最小覆盖子串
 *
 * https://leetcode.cn/problems/minimum-window-substring/description/
 *
 * algorithms
 * Hard (44.36%)
 * Likes:    1959
 * Dislikes: 0
 * Total Accepted:    304.9K
 * Total Submissions: 687.2K
 * Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
 *
 * 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
 * 。
 *
 *
 *
 * 注意：
 *
 *
 * 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
 * 如果 s 中存在这样的子串，我们保证它是唯一的答案。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "ADOBECODEBANC", t = "ABC"
 * 输出："BANC"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "a", t = "a"
 * 输出："a"
 *
 *
 * 示例 3:
 *
 *
 * 输入: s = "a", t = "aa"
 * 输出: ""
 * 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
 * 因此没有符合条件的子字符串，返回空字符串。
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * s 和 t 由英文字母组成
 *
 *
 *
 * 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
 */

export
// @lc code=start
function minWindow(s: string, t: string): string {
  const counter: Record<string, number> = {}
  const charSet = new Set<string>()
  for (let i = 0; i < t.length; i++) {
    counter[t[i]] = (counter[t[i]] || 0) + 1
    charSet.add(t[i])
  }
  let diffCount = charSet.size

  let result = [-1, s.length]
  let j = -1
  for (let i = 0; i < s.length; i++) {
    while (diffCount && j + 1 < s.length) {
      j++
      if (charSet.has(s[j]) && --counter[s[j]] === 0) {
        diffCount--
      }
    }

    if (diffCount === 0 && result[1] - result[0] > j - i) {
      result = [i, j]
    }

    if (charSet.has(s[i]) && ++counter[s[i]] === 1) {
      diffCount++
    }
  }

  if (result[0] < 0) return ''
  return s.slice(result[0], result[1] + 1)
}
// @lc code=end

console.log(minWindow('ADOBECODEBANC', 'ABC'))
console.log(minWindow('a', 'a'))
