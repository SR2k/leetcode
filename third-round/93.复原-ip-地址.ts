/*
 * @lc app=leetcode.cn id=93 lang=typescript
 *
 * [93] 复原 IP 地址
 *
 * https://leetcode-cn.com/problems/restore-ip-addresses/description/
 *
 * algorithms
 * Medium (55.22%)
 * Likes:    799
 * Dislikes: 0
 * Total Accepted:    186K
 * Total Submissions: 336.7K
 * Testcase Example:  '"25525511135"'
 *
 * 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
 *
 *
 * 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
 * 和 "192.168@1.1" 是 无效 IP 地址。
 *
 *
 * 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能
 * 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "25525511135"
 * 输出：["255.255.11.135","255.255.111.35"]
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "0000"
 * 输出：["0.0.0.0"]
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "101023"
 * 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 20
 * s 仅由数字组成
 *
 *
 */

export
// @lc code=start
function restoreIpAddresses(s: string): string[] {
  const result: string[] = []

  function helper(prev: string[], i: number) {
    if (i >= s.length) {
      if (prev.length === 4) {
        result.push(prev.join('.'))
      }
      return
    }

    // 将当前段落单端划分为一段
    // 要求：前一次段落数 < 4
    if (prev.length < 4) {
      prev.push(s[i])
      helper(prev, i + 1)
      prev.pop()
    }

    // 将当前段落拼接到上一段
    // 要求：上一段不为 0
    if (prev.length && prev[prev.length - 1] !== '0') {
      const prevLast = prev[prev.length - 1]
      if (+(prevLast + s[i]) <= 255) {
        prev[prev.length - 1] += s[i]
        helper(prev, i + 1)
        prev[prev.length - 1] = prevLast
      }
    }
  }
  helper([], 0)

  return result
}
// @lc code=end
