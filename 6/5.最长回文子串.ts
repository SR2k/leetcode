/*
 * @lc app=leetcode.cn id=5 lang=typescript
 *
 * [5] 最长回文子串
 *
 * https://leetcode.cn/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (36.74%)
 * Likes:    5383
 * Dislikes: 0
 * Total Accepted:    1.1M
 * Total Submissions: 2.9M
 * Testcase Example:  '"babad"'
 *
 * 给你一个字符串 s，找到 s 中最长的回文子串。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "babad"
 * 输出："bab"
 * 解释："aba" 同样是符合题意的答案。
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "cbbd"
 * 输出："bb"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 1000
 * s 仅由数字和英文字母组成
 *
 *
 */

export
// @lc code=start
function longestPalindrome(s: string): string {
  let begin = 0, end = 0

  for (let i = 0; i < s.length; i++) {
    let [x, y] = expand(i, i, s)
    if (y - x > end - begin) {
      begin = x
      end = y
    }

    [x, y] = expand(i, i + 1, s)
    if (y - x > end - begin) {
      begin = x
      end = y
    }
  }

  return s.slice(begin, end + 1)
}

const expand = (i: number, j: number, s: string): [number, number] => {
  if (s[i] !== s[j] || i < 0 || j >= s.length) {
    return [s.length, -1]
  }
  while (i - 1 >= 0 && j + 1 < s.length && s[i - 1] === s[j + 1]) {
    i--
    j++
  }
  return [i, j]
}
// @lc code=end
