#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
# https://leetcode-cn.com/problems/basic-calculator/description/
#
# algorithms
# Hard (41.64%)
# Likes:    571
# Dislikes: 0
# Total Accepted:    60.5K
# Total Submissions: 145.3K
# Testcase Example:  '"1 + 1"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
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
# 1 
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
# 
# 
#

# @lc code=start
class Solution:
    @staticmethod
    def readInt(i: int, s: str) -> tuple[int, int]:
        tmp = ''
        while i < len(s) and s[i].isdigit():
            tmp += s[i]
            i += 1
        return (i - 1, int(tmp))

    def calculate(self, s: str) -> int:
        tmp = []
        parentheses = []
        operator = '+'
        reverse = False

        i = 0
        while i < len(s):
            char = s[i]

            if char == '(':
                parentheses.append(operator)
                if operator == '-': reverse = not reverse
                operator = '+'
            elif char == ')':
                parenthese = parentheses.pop()
                if parenthese == '-': reverse = not reverse
            elif char == '+' or char == '-':
                operator = char
            elif char == ' ':
                pass
            else:
                i, n = Solution.readInt(i, s)
                if reverse:
                    tmp.append(n if operator == '-' else -n)
                else:
                    tmp.append(n if operator == '+' else -n)

            i += 1
        
        print(tmp)
        return sum(tmp)
# @lc code=end

print(Solution().calculate("- (3 + (4 + 5))"))
# print(Solution().calculate("1 + 1"))
# print(Solution().calculate(" 2-1 + 2 "))
# print(Solution().calculate( "(1+(4+5+2)-3)+(6+8)"))
# print(Solution().calculate("+48 + -48"))
