/*
 * @lc app=leetcode.cn id=171 lang=typescript
 *
 * [171] Excel 表列序号
 *
 * https://leetcode-cn.com/problems/excel-sheet-column-number/description/
 *
 * algorithms
 * Easy (71.73%)
 * Likes:    301
 * Dislikes: 0
 * Total Accepted:    113.8K
 * Total Submissions: 158.6K
 * Testcase Example:  '"A"'
 *
 * 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。
 *
 *
 *
 * 例如，
 *
 *
 * ⁠   A -> 1
 * ⁠   B -> 2
 * ⁠   C -> 3
 * ⁠   ...
 * ⁠   Z -> 26
 * ⁠   AA -> 27
 * ⁠   AB -> 28
 * ⁠   ...
 *
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: columnTitle = "A"
 * 输出: 1
 *
 *
 * 示例 2:
 *
 *
 * 输入: columnTitle = "AB"
 * 输出: 28
 *
 *
 * 示例 3:
 *
 *
 * 输入: columnTitle = "ZY"
 * 输出: 701
 *
 * 示例 4:
 *
 *
 * 输入: columnTitle = "FXSHRXW"
 * 输出: 2147483647
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= columnTitle.length <= 7
 * columnTitle 仅由大写英文组成
 * columnTitle 在范围 ["A", "FXSHRXW"] 内
 *
 *
 */

export
// @lc code=start
function titleToNumber(columnTitle: string): number {
  let result = 0
  for (const c of columnTitle) {
    result *= 26
    result += char2Number(c)
  }
  return result
}

function char2Number(char: string) {
  return char.charCodeAt(0) - 'A'.charCodeAt(0) + 1
}
// @lc code=end
