/*
 * @lc app=leetcode.cn id=1239 lang=typescript
 *
 * [1239] 串联字符串的最大长度
 *
 * https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
 *
 * algorithms
 * Medium (48.90%)
 * Likes:    204
 * Dislikes: 0
 * Total Accepted:    37.6K
 * Total Submissions: 76.9K
 * Testcase Example:  '["un","iq","ue"]'
 *
 * 给定一个字符串数组 arr，字符串 s 是将 arr 的含有 不同字母 的 子序列 字符串 连接 所得的字符串。
 *
 * 请返回所有可行解 s 中最长长度。
 *
 * 子序列 是一种可以从另一个数组派生而来的数组，通过删除某些元素或不删除元素而不改变其余元素的顺序。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：arr = ["un","iq","ue"]
 * 输出：4
 * 解释：所有可能的串联组合是：
 * - ""
 * - "un"
 * - "iq"
 * - "ue"
 * - "uniq" ("un" + "iq")
 * - "ique" ("iq" + "ue")
 * 最大长度为 4。
 *
 *
 * 示例 2：
 *
 *
 * 输入：arr = ["cha","r","act","ers"]
 * 输出：6
 * 解释：可能的解答有 "chaers" 和 "acters"。
 *
 *
 * 示例 3：
 *
 *
 * 输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
 * 输出：26
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= arr.length <= 16
 * 1 <= arr[i].length <= 26
 * arr[i] 中只含有小写英文字母
 *
 *
 */

export
// @lc code=start
function maxLength(arr: string[]): number {
  const resp = arr.map(getMask)
  let result = 0

  function helper(i: number, curr = 0, length = 0) {
    if (i >= arr.length) {
      result = Math.max(result, length)
      return
    }

    helper(i + 1, curr, length)

    if (resp[i] !== 0 && (curr & resp[i]) === 0) {
      helper(
        i + 1,
        curr ^ resp[i],
        length + arr[i].length,
      )
    }
  }

  helper(0)
  return result
}

const CHAR_CODE_A = 'a'.charCodeAt(0)

const getMask = (word: string) => {
  let result = 0
  for (let i = 0; i < word.length; i++) {
    const digit = 1 << (word.charCodeAt(i) - CHAR_CODE_A)
    if (result & digit) {
      return 0
    }
    result |= digit
  }
  return result
}
// @lc code=end
