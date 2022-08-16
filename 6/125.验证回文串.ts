/*
 * @lc app=leetcode.cn id=125 lang=typescript
 *
 * [125] 验证回文串
 *
 * https://leetcode.cn/problems/valid-palindrome/description/
 *
 * algorithms
 * Easy (46.93%)
 * Likes:    540
 * Dislikes: 0
 * Total Accepted:    373.9K
 * Total Submissions: 796.8K
 * Testcase Example:  '"A man, a plan, a canal: Panama"'
 *
 * 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
 *
 * 说明：本题中，我们将空字符串定义为有效的回文串。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: "A man, a plan, a canal: Panama"
 * 输出: true
 * 解释："amanaplanacanalpanama" 是回文串
 *
 *
 * 示例 2:
 *
 *
 * 输入: "race a car"
 * 输出: false
 * 解释："raceacar" 不是回文串
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 字符串 s 由 ASCII 字符组成
 *
 *
 */

export
// @lc code=start
function isPalindrome(s: string): boolean {
  let i = 0, j = s.length - 1

  while (i < j) {
    while (i < j && !isAlphaNum(s[i])) {
      i++
    }
    while (i < j && !isAlphaNum(s[j])) {
      j--
    }

    if (i >= j) break
    if (!isSame(s[i], s[j])) {
      return false
    }

    i++
    j--
  }

  return true
}

const isAlphaNum = (char: string) => (char <= 'z' && char >= 'a')
    || (char <= 'Z' && char >= 'A')
    || (char <= '9' && char >= '0')

const isSame = (a: string, b: string) => a.toLowerCase() === b.toLowerCase()
// @lc code=end
