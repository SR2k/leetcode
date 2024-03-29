#
# @lc app=leetcode.cn id=273 lang=python3
#
# [273] 整数转换英文表示
#
# https://leetcode-cn.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (30.37%)
# Likes:    156
# Dislikes: 0
# Total Accepted:    10.7K
# Total Submissions: 35.1K
# Testcase Example:  '123'
#
# 将非负整数 num 转换为其对应的英文表示。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num = 123
# 输出："One Hundred Twenty Three"
# 
# 
# 示例 2：
# 
# 
# 输入：num = 12345
# 输出："Twelve Thousand Three Hundred Forty Five"
# 
# 
# 示例 3：
# 
# 
# 输入：num = 1234567
# 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# 
# 
# 示例 4：
# 
# 
# 输入：num = 1234567891
# 输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# 
# 
#

# @lc code=start
MAP_1 = [ \
    None, 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', \
    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen' \
]

MAP_2 = [None, None, 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

UNITS = [None, 'Thousand', 'Million', 'Billion']

class Solution:

    @staticmethod
    def convert_num_part(num: int) -> str:
        if num == 0:
            return ""

        result = []

        hundreds = num // 100
        num %= 100
        tens, ones = num // 10, num % 10

        if hundreds:
            result.append(MAP_1[hundreds])
            result.append('Hundred')

        if tens >= 2 and ones:
            result.append(MAP_2[tens])
            result.append(MAP_1[ones])
        elif tens >= 2:
            result.append(MAP_2[tens])
        elif num:
            result.append(MAP_1[num])

        return " ".join(result)

    def numberToWords(self, num: int) -> str:
        parts = []
        while num:
            parts.append(num % 1000)
            num //= 1000

        result = []
        for i, p in enumerate(parts):
            digit = Solution.convert_num_part(p)

            if not digit:
                continue

            if UNITS[i]:
                result.append(f"{digit} {UNITS[i]}")
            else:
                result.append(digit)

        return " ".join(result[::-1]) or 'Zero'
# @lc code=end

s = Solution()
# print(s.numberToWords(0))
# print(s.numberToWords(100))
# print(s.numberToWords(123))
# print(s.numberToWords(123456789))
# print(s.numberToWords(123000789))
# print(s.numberToWords(123010789))
# print(s.numberToWords(123001789))
# print(s.numberToWords(123001000))
# print(s.numberToWords(123001001))

# MAP_1 = [ \
#     None, 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', \
#     'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen' \
# ]

# MAP_2 = [None, None, 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

# UNITS = [None, 'Thousand', 'Million', 'Billion']

# class Solution:
#     @staticmethod
#     def join(a: str, b: str) -> str:
#         if not a and not b: return ''
#         if not a: return b
#         if not b: return a
#         return a + ' ' + b

#     @staticmethod
#     def partsToWords(num: int, unit: str = None) -> str:
#         if num == 0: return ''

#         if num <= 19:
#             ret = MAP_1[num]
#         elif num <= 99:
#             ret = Solution.join( MAP_2[num // 10], MAP_1[num % 10])
#         else:
#             ret = Solution.join(MAP_1[num // 100] + ' Hundred', Solution.partsToWords(num % 100))

#         if unit: return ret + ' ' + unit
#         return ret

#     def numberToWords(self, num: int) -> str:
#         ret = ''
#         unitP = 0
#         while num > 0:
#             part = num % 1000
#             ret = Solution.join(Solution.partsToWords(part, UNITS[unitP]), ret)
#             num //= 1000
#             unitP += 1

#         return ret if ret else 'Zero'
