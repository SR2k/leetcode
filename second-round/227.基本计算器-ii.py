#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
# https://leetcode-cn.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (43.77%)
# Likes:    518
# Dislikes: 0
# Total Accepted:    96.6K
# Total Submissions: 220.5K
# Testcase Example:  '"3+2*2"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 
# 整数除法仅保留整数部分。
# 
# 
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
# 1 
# s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
# s 表示一个 有效表达式
# 表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
# 题目数据保证答案是一个 32-bit 整数
# 
# 
# 
# 
#

# @lc code=start
from math import ceil, floor


class Solution:
    def calculate(self, s: str) -> int:
        nums = [0]

        sign = '+'
        temp = 0

        s = s + '+0'

        for char in s:
            if char.isnumeric():
                temp = temp * 10 + (ord(char) - ord('0'))
                continue
            if char == ' ':
                continue

            if sign == '+':
                nums.append(temp)
            elif sign == '-':
                nums.append(-temp)
            elif sign == '*':
                nums[-1] *= temp
            else:
                nums[-1] = ceil(nums[-1] / temp) if nums[-1] < 0 else nums[-1] // temp

            temp = 0
            sign = char

        return sum(nums)
# @lc code=end

s = Solution()
# print(s.calculate(s = "3+2*2"))
print(s.calculate(s = " 3/2 "))
# print(s.calculate(s = " 3+5 / 2 "))
print(s.calculate("14-3/2"))
