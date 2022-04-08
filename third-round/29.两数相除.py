#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# https://leetcode-cn.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (22.14%)
# Likes:    846
# Dislikes: 0
# Total Accepted:    148.8K
# Total Submissions: 672.1K
# Testcase Example:  '10\n3'
#
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) =
# -2
# 
# 
# 
# 示例 1:
# 
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
# 
# 示例 2:
# 
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2
# 
# 
# 
# 提示：
# 
# 
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
# 
# 
#

# @lc code=start
CORNER_CASE = (-1 * (2 ** 31), -1)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend, divisor) == CORNER_CASE:
            return 2 ** 31 - 1

        flag = True
        if dividend < 0:
            dividend = -dividend
            flag = not flag
        if divisor < 0:
            divisor = -divisor
            flag = not flag

        if dividend < divisor:
            return 0

        result = 1
        curr = divisor
        while curr + curr <= dividend:
            curr += curr
            result += result

        result += self.divide(dividend - curr, divisor)
        return result if flag else -result
# @lc code=end

s = Solution()
print(s.divide(dividend = 10, divisor = 3))
print(s.divide(dividend = 7, divisor = -3))
print(s.divide(dividend = 9, divisor = -3))
print(s.divide(dividend = 81, divisor = -3))
print(s.divide(-2147483648, -1))
