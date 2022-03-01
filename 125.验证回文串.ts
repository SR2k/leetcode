/*
 * @lc app=leetcode.cn id=125 lang=typescript
 *
 * [125] 验证回文串
 *
 * https://leetcode-cn.com/problems/valid-palindrome/description/
 *
 * algorithms
 * Easy (47.12%)
 * Likes:    460
 * Dislikes: 0
 * Total Accepted:    312.6K
 * Total Submissions: 663.4K
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
  let left = 0, right = s.length - 1
  while (left < right) {
    while (left < right && !isNumAlpha(s[left])) left++
    if (left === right) break

    while (left < right && !isNumAlpha(s[right])) right--
    if (left === right) break

    if (s[left].toLowerCase() !== s[right].toLowerCase()) {
      return false
    }
    left++
    right--
  }

  return true
}

const CharCodes = {
  a: 'a'.charCodeAt(0),
  z: 'z'.charCodeAt(0),
  A: 'A'.charCodeAt(0),
  Z: 'Z'.charCodeAt(0),
  0: '0'.charCodeAt(0),
  9: '9'.charCodeAt(0),
}

function isNumAlpha(char: string) {
  const charCode = char.charCodeAt(0)
  return (charCode >= CharCodes.a && charCode <= CharCodes.z)
    || (charCode >= CharCodes.A && charCode <= CharCodes.Z)
    || (charCode >= CharCodes['0'] && charCode <= CharCodes['9'])
}
// @lc code=end
