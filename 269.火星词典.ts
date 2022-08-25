/*
 * @lc app=leetcode.cn id=269 lang=typescript
 *
 * [269] 火星词典
 *
 * https://leetcode.cn/problems/alien-dictionary/description/
 *
 * algorithms
 * Hard (35.96%)
 * Likes:    242
 * Dislikes: 0
 * Total Accepted:    10.4K
 * Total Submissions: 28.8K
 * Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
 *
 * 现有一种使用英语字母的火星语言，这门语言的字母顺序与英语顺序不同。
 *
 * 给你一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。
 *
 * 请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中
 * 任意一种 顺序即可。
 *
 * 字符串 s 字典顺序小于 字符串 t 有两种情况：
 *
 *
 * 在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
 * 如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t
 * 。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：words = ["wrt","wrf","er","ett","rftt"]
 * 输出："wertf"
 *
 *
 * 示例 2：
 *
 *
 * 输入：words = ["z","x"]
 * 输出："zx"
 *
 *
 * 示例 3：
 *
 *
 * 输入：words = ["z","x","z"]
 * 输出：""
 * 解释：不存在合法字母顺序，因此返回 "" 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 1
 * words[i] 仅由小写英文字母组成
 *
 *
 */

export
// @lc code=start
function alienOrder(words: string[]): string {
  const degrees: Record<string, number> = {}
  const children: Record<string, Set<string>> = {}
  const charSet = new Set<string>()

  for (const w of words) {
    for (const c of w) {
      charSet.add(c)
    }
  }

  for (let i = 0; i < words.length - 1; i++) {
    for (let j = i + 1; j < words.length; j++) {
      const diff = getDiff(words[i], words[j])
      if (diff instanceof Error) return ''
      if (!diff) continue
      const [a, b] = diff

      if (!children[a]?.has(b)) {
        children[a] = children[a] || new Set()
        children[a].add(b)
        degrees[b] = (degrees[b] || 0) + 1
      }
    }
  }

  const stack = [...charSet].filter((x) => !degrees[x])
  const result: string[] = []

  while (stack.length) {
    const char = stack.pop()!
    result.push(char)

    for (const c of (children[char] || [])) {
      if (--degrees[c] === 0) {
        stack.push(c)
      }
    }
  }

  if (result.length === charSet.size) {
    return result.join('')
  }
  return ''
}

function getDiff(a: string, b: string): [string, string] | null | Error {
  let i = 0
  while (i < a.length && i < b.length) {
    if (a[i] !== b[i]) {
      return [a[i], b[i]]
    }
    i++
  }

  if (a.length <= b.length) {
    return null
  }
  return new Error()
}
// @lc code=end
