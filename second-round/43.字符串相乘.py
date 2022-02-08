#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (44.98%)
# Likes:    817
# Dislikes: 0
# Total Accepted:    191.3K
# Total Submissions: 425.3K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 
# 示例 1:
# 
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 
# 示例 2:
# 
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 
# 说明：
# 
# 
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
# 
# 
#

# @lc code=start
class Solution:
    @staticmethod
    def multiply_by_digit(n1: str, n2: str, result: list[str]) -> list[int]:
        offset = 0
        i = len(n1) - 1
        n2 = int(n2)

        while i >= 0 or offset:
            digit = int(n1[i]) if i >= 0 else 0
            curr_result = digit * n2 + offset
            offset = curr_result // 10
            curr_result %= 10
            result.append(curr_result)
            i -= 1


    @staticmethod
    def sum(a: list[int], b: list[int]):
        m, n = len(a), len(b)
        i, size = 0, max(m, n)
        d = 0
        while i < size or d:
            na = a[i] if i < m else 0
            nb = b[i] if i < n else 0

            result = na + nb + d
            d = result // 10
            result %= 10

            if i < m:
                a[i] = result
            else:
                a.append(result)

            i += 1


    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        result = []
        for i, char2 in enumerate(num2):
            r = [0] * (len(num2) - i - 1)
            Solution.multiply_by_digit(num1, char2, r)
            Solution.sum(result, r)

        return "".join(str(i) for i in result[::-1])
# @lc code=end

s = Solution()
print(s.multiply(num1 = "2", num2 = "3"))
print(s.multiply(num1 = "123", num2 = "456"))
print(s.multiply(num1 = "123456", num2 = "456789"))
