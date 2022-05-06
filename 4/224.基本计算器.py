#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
# https://leetcode-cn.com/problems/basic-calculator/description/
#
# algorithms
# Hard (41.80%)
# Likes:    743
# Dislikes: 0
# Total Accepted:    85.1K
# Total Submissions: 203.5K
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
class Solution:
    def calculate(self, s: str) -> int:
        global_sign = curr_sign = 1
        buffer = 0
        nums = []
        sign_stack = []

        s += ' '

        for char in s:
            if char.isnumeric():
                buffer = buffer * 10 + int(char)
            elif buffer:
                nums.append(global_sign * curr_sign * buffer)
                buffer = 0

            if char == '+':
                curr_sign = 1
            elif char == '-':
                curr_sign = -1
            elif char == '(':
                sign_stack.append(curr_sign)
                global_sign *= curr_sign
                curr_sign = 1
            elif char == ')':
                global_sign *= sign_stack.pop()

        return sum(nums)
# @lc code=end

s = Solution()
print(s.calculate( "1 + 1"))
print(s.calculate(" 2-1 + 2 "))
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
print(s.calculate("-(1-(4+5+2)-3)+(6+8)"))

#     |
# -(1-(4+5+2)-3)+(6+8)

# global = -1
# curr = -1
# buffer = 0

# nums = [-1]
# signs = [-1]


