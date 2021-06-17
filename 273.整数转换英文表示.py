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
    def join(a: str, b: str) -> str:
        if not a and not b: return ''
        if not a: return b
        if not b: return a
        return a + ' ' + b

    @staticmethod
    def partsToWords(num: int, unit: str = None) -> str:
        if num == 0: return ''

        if num <= 19:
            ret = MAP_1[num]
        elif num <= 99:
            ret = Solution.join( MAP_2[num // 10], MAP_1[num % 10])
        else:
            ret = Solution.join(MAP_1[num // 100] + ' Hundred', Solution.partsToWords(num % 100))

        if unit: return ret + ' ' + unit
        return ret

    def numberToWords(self, num: int) -> str:
        ret = ''
        unitP = 0
        while num > 0:
            part = num % 1000
            ret = Solution.join(Solution.partsToWords(part, UNITS[unitP]), ret)
            num //= 1000
            unitP += 1

        return ret if ret else 'Zero'
# @lc code=end

