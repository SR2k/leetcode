#
# @lc app=leetcode.cn id=1271 lang=python3
#
# [1271] 十六进制魔术数字
#
# https://leetcode-cn.com/problems/hexspeak/description/
#
# algorithms
# Easy (50.23%)
# Likes:    8
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 4.6K
# Testcase Example:  '"257"'
#
# 你有一个十进制数字，请按照此规则将它变成「十六进制魔术数字」：首先将它变成字母大写的十六进制字符串，然后将所有的数字 0 变成字母 O ，将数字 1
# 变成字母 I 。
# 
# 如果一个数字在转换后只包含 {"A", "B", "C", "D", "E", "F", "I", "O"} ，那么我们就认为这个转换是有效的。
# 
# 给你一个字符串 num ，它表示一个十进制数 N，如果它的十六进制魔术数字转换是有效的，请返回转换后的结果，否则返回 "ERROR" 。
# 
# 
# 
# 示例 1：
# 
# 输入：num = "257"
# 输出："IOI"
# 解释：257 的十六进制表示是 101 。
# 
# 
# 示例 2：
# 
# 输入：num = "3"
# 输出："ERROR"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 10^12
# 给定字符串不会有前导 0 。
# 结果中的所有字母都应该是大写字母。
# 
# 
#

# @lc code=start
HEX_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
VALID_DIGITS = ("A", "B", "C", "D", "E", "F", "I", "O")
MAP = { '0': 'O', '1': 'I' }
ERROR = 'ERROR'

class Solution:
    def toHexspeak(self, num: str) -> str:
        n = int(num)
        ret = ""
        while n:
            digit = HEX_DIGITS[n % 16]
            if digit in MAP:
                digit = MAP[digit]
            if digit not in VALID_DIGITS:
                return ERROR
            ret = digit + ret
            n //= 16

        return ret
# @lc code=end
