/*
 * @lc app=leetcode.cn id=541 lang=typescript
 *
 * [541] 反转字符串 II
 *
 * https://leetcode-cn.com/problems/reverse-string-ii/description/
 *
 * algorithms
 * Easy (60.06%)
 * Likes:    252
 * Dislikes: 0
 * Total Accepted:    90.9K
 * Total Submissions: 151.3K
 * Testcase Example:  '"abcdefg"\n2'
 *
 * 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
 *
 *
 * 如果剩余字符少于 k 个，则将剩余字符全部反转。
 * 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "abcdefg", k = 2
 * 输出："bacdfeg"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "abcd", k = 2
 * 输出："bacd"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^4
 * s 仅由小写英文组成
 * 1 <= k <= 10^4
 *
 *
 */

export
// @lc code=start
function reverseStr(s: string, k: number): string {
  const str = [...s]

  for (let i = 0; i < s.length; i += 2 * k) {
    reverse(str, i, i + k - 1)
  }

  return str.join('')
}

function reverse(s: string[], l: number, r: number) {
  r = Math.min(s.length - 1, r)
  while (l < r) {
    [s[l], s[r]] = [s[r], s[l]]
    l += 1
    r -= 1
  }
}
// @lc code=end
