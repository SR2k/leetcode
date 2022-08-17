/*
 * @lc app=leetcode.cn id=5 lang=typescript
 *
 * [5] 最长回文子串
 *
 * https://leetcode.cn/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (37.02%)
 * Likes:    5583
 * Dislikes: 0
 * Total Accepted:    1.2M
 * Total Submissions: 3.1M
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
  if (!s.length) return ''

  let result = [0, 0]
  for (let i = 0; i + 1 < s.length; i++) {
    const j = i + 1

    const [singleBegin, singleEnd] = check(s, i, i)
    if (singleEnd - singleBegin > result[1] - result[0]) {
      result = [singleBegin, singleEnd]
    }

    const [doubleBegin, doubleEnd] = check(s, j, i)
    if (doubleEnd - doubleBegin > result[1] - result[0]) {
      result = [doubleBegin, doubleEnd]
    }
  }

  return s.slice(result[0], result[1] + 1)
}

function check(s: string, i: number, j: number): [number, number] {
  if (s[i] !== s[j]) return [-1, -1]

  while (i - 1 >= 0 && j + 1 < s.length && s[i - 1] === s[j + 1]) {
    i--
    j++
  }
  return [i, j]
}
// @lc code=end
