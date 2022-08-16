/*
 * @lc app=leetcode.cn id=171 lang=typescript
 *
 * [171] Excel 表列序号
 *
 * https://leetcode.cn/problems/excel-sheet-column-number/description/
 *
 * algorithms
 * Easy (71.64%)
 * Likes:    335
 * Dislikes: 0
 * Total Accepted:    135.1K
 * Total Submissions: 188.6K
 * Testcase Example:  '"A"'
 *
 * 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。
 *
 * 例如：
 *
 *
 * A -> 1
 * B -> 2
 * C -> 3
 * ...
 * Z -> 26
 * AA -> 27
 * AB -> 28
 * ...
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

  for (let i = 0; i < columnTitle.length; i++) {
    result *= SCALE
    result += (columnTitle.charCodeAt(i) - CHAR_CODE_A + 1)
  }

  return result
}

const CHAR_CODE_A = 'A'.charCodeAt(0)
const SCALE = 26
// @lc code=end
