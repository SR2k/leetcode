/*
 * @lc app=leetcode.cn id=14 lang=typescript
 *
 * [14] 最长公共前缀
 *
 * https://leetcode-cn.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (41.75%)
 * Likes:    2036
 * Dislikes: 0
 * Total Accepted:    731.8K
 * Total Submissions: 1.8M
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

export
// @lc code=start
function longestCommonPrefix(strs: string[]): string {
  const minLength = Math.min(...strs.map((x) => x.length))

  for (let i = 0; i < minLength; i++) {
    const char = strs[0][i]
    for (const s of strs) {
      if (s[i] !== char) {
        return strs[0].slice(0, i)
      }
    }
  }

  return strs[0].slice(0, minLength)
}
// @lc code=end
