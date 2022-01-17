#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# https://leetcode-cn.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (20.55%)
# Likes:    587
# Dislikes: 0
# Total Accepted:    94K
# Total Submissions: 457.2K
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
NEG_INT_MAX = 2 ** 31
POS_INT_MAX = NEG_INT_MAX - 1

class Solution:
    def helper(self, dividend: int, divisor: int) -> int:
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            return -self.helper(abs(dividend), abs(divisor))

        dividend, divisor = abs(dividend), abs(divisor)

        if dividend < divisor:
            return 0

        temp, result = divisor, 1
        while temp + temp < dividend:
            temp += temp
            result += result

        return result + self.helper(dividend - temp, divisor)

    def divide(self, dividend: int, divisor: int) -> int:
        return min(max(self.helper(dividend, divisor), -NEG_INT_MAX), POS_INT_MAX)
# @lc code=end

s = Solution()
# print(s.divide(-2147483648, -2147483648))
# print(s.divide(-2147483648, -2147483648))
# print(s.divide(-2147483648, -1))
print(s.divide(-2147483648, 1))
# print(s.divide(-2147483648, -20))
# print(s.divide(10, -20))
# print(s.divide(10, 3))
# print(s.divide(7, -3))

# NEG_INT_MAX = 2 ** 31
# POS_INT_MAX = NEG_INT_MAX - 1

# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         if dividend == 0: return 0

#         is_negative = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
#         abs_max = NEG_INT_MAX if is_negative else POS_INT_MAX
#         dividend = dividend if dividend > 0 else -dividend
#         divisor = divisor if divisor > 0 else -divisor
#         temp_arr, count_arr = [0], [0]

#         while temp_arr[-1] < dividend:
#             if temp_arr[-1] == 0:
#                 temp_arr.append(divisor)
#                 count_arr.append(1)
#             else:
#                 temp_arr.append(temp_arr[-1] + temp_arr[-1])
#                 count_arr.append(count_arr[-1] + count_arr[-1])

#         temp_num, ret = 0, 0
#         for i in range(len(temp_arr) - 1, 0, -1):
#             while temp_num <= dividend - temp_arr[i]:
#                 if ret > abs_max - count_arr[i]:
#                     return POS_INT_MAX
#                 temp_num += temp_arr[i]
#                 ret += count_arr[i]

#         return -ret if is_negative else ret
