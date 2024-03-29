/*
 * @lc app=leetcode.cn id=151 lang=typescript
 *
 * [151] 翻转字符串里的单词
 *
 * https://leetcode-cn.com/problems/reverse-words-in-a-string/description/
 *
 * algorithms
 * Medium (49.24%)
 * Likes:    433
 * Dislikes: 0
 * Total Accepted:    197.8K
 * Total Submissions: 401.6K
 * Testcase Example:  '"the sky is blue"'
 *
 * 给你一个字符串 s ，逐个翻转字符串中的所有 单词 。
 *
 * 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
 *
 * 请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。
 *
 * 说明：
 *
 *
 * 输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
 * 翻转后单词间应当仅用一个空格分隔。
 * 翻转后的字符串中不应包含额外的空格。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "the sky is blue"
 * 输出："blue is sky the"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "  hello world  "
 * 输出："world hello"
 * 解释：输入字符串可以在前面或者后面包含多余的空格，但是翻转后的字符不能包括。
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "a good   example"
 * 输出："example good a"
 * 解释：如果两个单词间有多余的空格，将翻转后单词间的空格减少到只含一个。
 *
 *
 * 示例 4：
 *
 *
 * 输入：s = "  Bob    Loves  Alice   "
 * 输出："Alice Loves Bob"
 *
 *
 * 示例 5：
 *
 *
 * 输入：s = "Alice does not even like bob"
 * 输出："bob like even not does Alice"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * s 包含英文大小写字母、数字和空格 ' '
 * s 中 至少存在一个 单词
 *
 *
 *
 *
 *
 *
 *
 * 进阶：
 *
 *
 * 请尝试使用 O(1) 额外空间复杂度的原地解法。
 *
 *
 */

export
// @lc code=start
function reverseWords(_s: string): string {
  const str = [..._s]
  str.reverse()

  let p = 0; let
    end = 0
  let tail = 0
  while (end < str.length) {
    while (end < str.length && str[end] === ' ') {
      end += 1
    }
    if (end >= str.length) {
      break
    }

    while (end < str.length && str[end] !== ' ') {
      tail = p
      str[p] = str[end]
      p += 1
      end += 1
    }

    if (p + 1 < str.length) {
      str[p] = ' '
      p += 1
    }

    end += 1
  }
  str.length = tail + 1

  let i = 0
  while (i < str.length) {
    let wordEnd = i
    while (wordEnd + 1 < str.length && str[wordEnd + 1] !== ' ') {
      wordEnd += 1
    }

    let j = wordEnd
    while (i < j) {
      [str[i], str[j]] = [str[j], str[i]]
      i += 1
      j -= 1
    }

    i = wordEnd + 2
  }

  return str.join('')
}
// @lc code=end
