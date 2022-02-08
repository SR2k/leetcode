#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#
# https://leetcode-cn.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (71.73%)
# Likes:    301
# Dislikes: 0
# Total Accepted:    113.8K
# Total Submissions: 158.6K
# Testcase Example:  '"A"'
#
# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。
# 
# 
# 
# 例如，
# 
# 
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# ⁠   ...
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: columnTitle = "A"
# 输出: 1
# 
# 
# 示例 2:
# 
# 
# 输入: columnTitle = "AB"
# 输出: 28
# 
# 
# 示例 3:
# 
# 
# 输入: columnTitle = "ZY"
# 输出: 701
# 
# 示例 4:
# 
# 
# 输入: columnTitle = "FXSHRXW"
# 输出: 2147483647
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= columnTitle.length <= 7
# columnTitle 仅由大写英文组成
# columnTitle 在范围 ["A", "FXSHRXW"] 内
# 
# 
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for char in columnTitle:
            result *= 26
            result += ord(char) - ord('A') + 1

        return result
# @lc code=end
