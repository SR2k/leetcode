#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#
# https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/description/
#
# algorithms
# Easy (50.79%)
# Likes:    180
# Dislikes: 0
# Total Accepted:    30.2K
# Total Submissions: 59.4K
# Testcase Example:  '[1,0,0]'
#
# 有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
# 
# 现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
# 
# 示例 1:
# 
# 
# 输入: 
# bits = [1, 0, 0]
# 输出: True
# 解释: 
# 唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# bits = [1, 1, 1, 0]
# 输出: False
# 解释: 
# 唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
# 
# 
# 注意:
# 
# 
# 1 <= len(bits) <= 1000.
# bits[i] 总是0 或 1.
# 
# 
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n, cnt = 0, len(bits)
        while n < cnt - 1:
            n += 2 if bits[n] == 1 else 1
        return n == cnt - 1
# @lc code=end

