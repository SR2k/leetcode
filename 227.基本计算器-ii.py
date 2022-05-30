#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
# https://leetcode.cn/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (43.94%)
# Likes:    572
# Dislikes: 0
# Total Accepted:    113.4K
# Total Submissions: 257.7K
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
        prev_sign = '+'
        stack = [0]
        buffer = 0

        for char in (s + '+0'):
            if char.isnumeric():
                buffer = buffer * 10 + ord(char) - ord('0')
                continue

            if char == ' ':
                continue

            if prev_sign == '+':
                stack.append(buffer)
            elif prev_sign == '-':
                stack.append(-buffer)
            elif prev_sign == '*':
                stack.append(stack.pop() * buffer)
            elif prev_sign == '/':
                stack.append(Solution.div(stack.pop(), buffer))

            buffer = 0
            prev_sign = char

        return sum(stack)

    @staticmethod
    def div(a: int, b: int):
        if (a > 0 and b > 0) or (a < 0 and b < 0):
            return a // b
        return -(abs(a) // abs(b))
# @lc code=end
