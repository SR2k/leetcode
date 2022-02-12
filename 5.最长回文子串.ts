/*
 * @lc app=leetcode.cn id=5 lang=typescript
 *
 * [5] 最长回文子串
 *
 * https://leetcode-cn.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (35.79%)
 * Likes:    4577
 * Dislikes: 0
 * Total Accepted:    844.7K
 * Total Submissions: 2.3M
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
 * 示例 3：
 *
 *
 * 输入：s = "a"
 * 输出："a"
 *
 *
 * 示例 4：
 *
 *
 * 输入：s = "ac"
 * 输出："a"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * s 仅由数字和英文字母（大写和/或小写）组成
 *
 *
 */

export
// @lc code=start
function longestPalindrome(s: string): string {
  let result = [0, 0]

  function expand(l: number, r: number) {
    while (l >= 0 && r < s.length && s[l] === s[r]) {
      if (r - l > result[1] - result[0]) {
        result = [l, r]
      }

      l -= 1
      r += 1
    }
  }

  for (let i = 0; i < s.length; i++) {
    expand(i, i)
    if (i + 1 < s.length && s[i] === s[i + 1]) expand(i, i + 1)
  }

  return s.slice(result[0], result[1] + 1)
}
// @lc code=end
