/*
 * @lc app=leetcode.cn id=1239 lang=typescript
 *
 * [1239] 串联字符串的最大长度
 *
 * https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
 *
 * algorithms
 * Medium (49.11%)
 * Likes:    194
 * Dislikes: 0
 * Total Accepted:    36.3K
 * Total Submissions: 73.8K
 * Testcase Example:  '["un","iq","ue"]'
 *
 * 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
 *
 * 请返回所有可行解 s 中最长长度。
 *
 *
 *
 * 示例 1：
 *
 * 输入：arr = ["un","iq","ue"]
 * 输出：4
 * 解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
 *
 *
 * 示例 2：
 *
 * 输入：arr = ["cha","r","act","ers"]
 * 输出：6
 * 解释：可能的解答有 "chaers" 和 "acters"。
 *
 *
 * 示例 3：
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
  const words = arr.map(getResp).filter((x) => x[0] > 0)
  let result = 0

  function helper(prev: number, prevLength: number, i: number) {
    if (i >= words.length) {
      result = Math.max(result, prevLength)
      return
    }

    helper(prev, prevLength, i + 1)

    const [bits, length] = words[i]
    if ((prev & bits) === 0) {
      helper(prev | bits, prevLength + length, i + 1)
    }
  }
  helper(0, 0, 0)

  return result
}

function getResp(word: string) {
  let result = 0
  for (const char of word) {
    const code = char.charCodeAt(0) - 'a'.charCodeAt(0) + 1
    const digit = 1 << code
    if (result & digit) return [-1, -1]
    result |= digit
  }
  return [result, word.length]
}
// @lc code=end
