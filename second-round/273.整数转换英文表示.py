#
# @lc app=leetcode.cn id=273 lang=python3
#
# [273] 整数转换英文表示
#
# https://leetcode-cn.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (31.09%)
# Likes:    199
# Dislikes: 0
# Total Accepted:    19.8K
# Total Submissions: 56K
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
ONES = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
TENS = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
ELEVEN_TO_NINETY = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

UNITS = ['', 'Thousand', 'Million', 'Billion']


class Solution:
    def humanize_part(self, num: int) -> str:
        if not num:
            return ''

        result = []
        if num >= 100:
            hundreds = num // 100
            result.append(ONES[hundreds])
            result.append('Hundred')
            num %= 100

        if 11 <= num <= 19:
            result.append(ELEVEN_TO_NINETY[num - 11])
        else:
            tens = num // 10
            ones = num % 10

            if tens:
                result.append(TENS[tens])
            if ones:
                result.append(ONES[ones])

        return result


    def numberToWords(self, num: int) -> str:
        result = []
        i = 0
        while num:
            partial = num % 1000
            partial_result = self.humanize_part(partial)
            if partial_result:
                if UNITS[i]:
                    partial_result.append(UNITS[i])
                result = partial_result + result
            num //= 1000
            i += 1

        return " ".join(result) if result else 'Zero'
# @lc code=end
