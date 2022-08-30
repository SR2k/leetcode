/*
 * @lc app=leetcode.cn id=14 lang=typescript
 *
 * [14] 最长公共前缀
 *
 * https://leetcode.cn/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (42.86%)
 * Likes:    2410
 * Dislikes: 0
 * Total Accepted:    917.4K
 * Total Submissions: 2.1M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * 编写一个函数来查找字符串数组中的最长公共前缀。
 *
 * 如果不存在公共前缀，返回空字符串 ""。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：strs = ["flower","flow","flight"]
 * 输出："fl"
 *
 *
 * 示例 2：
 *
 *
 * 输入：strs = ["dog","racecar","car"]
 * 输出：""
 * 解释：输入不存在公共前缀。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= strs.length <= 200
 * 0 <= strs[i].length <= 200
 * strs[i] 仅由小写英文字母组成
 *
 *
 */

// @lc code=start
function longestCommonPrefix(strs: string[]): string {
  let result = 0

  for (let i = 0; i < strs[0].length; i++) {
    const target = strs[0][i]

    for (const str of strs) {
      if (i >= str.length || str[i] !== target) {
        return strs[0].slice(0, result)
      }
    }

    result++
  }

  return strs[0].slice(0, result)
}
// @lc code=end
