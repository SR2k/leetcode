#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (43.45%)
# Likes:    509
# Dislikes: 0
# Total Accepted:    99.1K
# Total Submissions: 228.2K
# Testcase Example:  '1'
#
# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
# 
# 例如：
# 
# 
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：columnNumber = 1
# 输出："A"
# 
# 
# 示例 2：
# 
# 
# 输入：columnNumber = 28
# 输出："AB"
# 
# 
# 示例 3：
# 
# 
# 输入：columnNumber = 701
# 输出："ZY"
# 
# 
# 示例 4：
# 
# 
# 输入：columnNumber = 2147483647
# 输出："FXSHRXW"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber:
            d = columnNumber % 26
            if d == 0:
                d = 26
            result = chr(d + ord('A') - 1) + result
            columnNumber -= d
            columnNumber //= 26

        return result
# @lc code=end

print(Solution().convertToTitle(columnNumber = 1)) # "A"
print(Solution().convertToTitle(columnNumber = 28)) #"AB"
print(Solution().convertToTitle(columnNumber = 701)) #"ZY"
print(Solution().convertToTitle(columnNumber = 2147483647)) #"FXSHRXW"
