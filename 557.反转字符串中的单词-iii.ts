/*
 * @lc app=leetcode.cn id=557 lang=typescript
 *
 * [557] 反转字符串中的单词 III
 *
 * https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/description/
 *
 * algorithms
 * Easy (74.32%)
 * Likes:    400
 * Dislikes: 0
 * Total Accepted:    204.3K
 * Total Submissions: 274.9K
 * Testcase Example:  `"Let's take LeetCode contest"`
 *
 * 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "Let's take LeetCode contest"
 * 输出："s'teL ekat edoCteeL tsetnoc"
 *
 *
 * 示例 2:
 *
 *
 * 输入： s = "God Ding"
 * 输出："doG gniD"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 5 * 10^4
 * s 包含可打印的 ASCII 字符。
 * s 不包含任何开头或结尾空格。
 * s 里 至少 有一个词。
 * s 中的所有单词都用一个空格隔开。
 *
 *
 */

export
// @lc code=start
function reverseWords(s: string): string {
  const str = [...s]

  let i = 0, j = 0
  while (j < s.length) {
    while (j + 1 < s.length && s[j + 1] !== ' ') {
      j += 1
    }
    reverse(str, i, j)

    i = j + 2
    j += 2
  }

  return str.join('')
}

function reverse(arr: any[], left: number, right: number) {
  while (left < right) {
    [arr[left], arr[right]] = [arr[right], arr[left]]
    left += 1
    right -= 1
  }
}
// @lc code=end
