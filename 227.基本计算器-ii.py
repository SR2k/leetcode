#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
# https://leetcode-cn.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (43.82%)
# Likes:    552
# Dislikes: 0
# Total Accepted:    107.2K
# Total Submissions: 244.4K
# Testcase Example:  '"3+2*2"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 
# 整数除法仅保留整数部分。
# 
# 你可以假设给定的表达式总是有效的。所有中间结果将在 [-2^31, 2^31 - 1] 的范围内。
# 
# 注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "3+2*2"
# 输出：7
# 
# 
# 示例 2：
# 
# 
# 输入：s = " 3/2 "
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：s = " 3+5 / 2 "
# 输出：5
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 3 * 10^5
# s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
# s 表示一个 有效表达式
# 表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
# 题目数据保证答案是一个 32-bit 整数
# 
# 
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        buffer = 0
        sign = '+'
        nums = []
        s += '+'

        for char in s:
            if char.isnumeric():
                buffer = buffer * 10 + int(char)
            elif char == ' ':
                pass
            else:
                if sign == '+' or sign == '-':
                   nums.append(buffer * (1 if sign == '+' else -1))
                elif sign == '*':
                    nums[-1] *= buffer
                else:
                    nums[-1] = self.div(nums[-1], buffer)

                buffer = 0
                sign = char

        return sum(nums)


    def div(self, a: int, b: int) -> int:
        ret = abs(a) // abs(b)

        if (a >= 0 and b > 0) or (a <= 0 and b < 0):
            return ret
        return -ret
# @lc code=end


s = Solution()
print(s.calculate(" 3-5 / 2 "))
