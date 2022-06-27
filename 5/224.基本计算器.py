#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
# https://leetcode.cn/problems/basic-calculator/description/
#
# algorithms
# Hard (41.89%)
# Likes:    765
# Dislikes: 0
# Total Accepted:    89.7K
# Total Submissions: 213.9K
# Testcase Example:  '"1 + 1"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 
# 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "1 + 1"
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：s = " 2-1 + 2 "
# 输出：3
# 
# 
# 示例 3：
# 
# 
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 3 * 10^5
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
# '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
# '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
# 输入中不存在两个连续的操作符
# 每个数字和运行的计算将适合于一个有符号的 32位 整数
# 
# 
#

# @lc code=start
from inspect import stack


class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        sign = []

        prev_sign = global_sign = 1
        num_buffer = 0

        for char in (s + " "):
            if char.isnumeric():
                num_buffer = num_buffer * 10 + ord(char) - ord('0')
            elif num_buffer:
                nums.append(prev_sign * global_sign * num_buffer)
                num_buffer = 0

            if char == '+':
                prev_sign = 1
            elif char == '-':
                prev_sign = -1
            elif char == '(':
                global_sign *= prev_sign
                sign.append(prev_sign)
                prev_sign = 1
            elif char == ')':
                global_sign *= sign.pop()

        return sum(nums)
# @lc code=end


# "-(1-(4+5+2)-3)-(6+8)"

prev_sign = 1
global_sign = 1

nums = [4, 5, 2, 3, 6, 8]
sign = [-1]
