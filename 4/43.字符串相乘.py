#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (44.87%)
# Likes:    900
# Dislikes: 0
# Total Accepted:    215.6K
# Total Submissions: 480.6K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 
# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 
# 示例 2:
# 
# 
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 
# 
# 
# 提示：
# 
# 
# 1 <= num1.length, num2.length <= 200
# num1 和 num2 只能由数字组成。
# num1 和 num2 都不包含任何前导零，除了数字0本身。
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        result = [0 for _ in range(l1 + l2)]

        for i in range(l1):
            for j in range(l2):
                d = l1 - i - 1 + l2 - j - 1
                result[d] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

        carry = 0
        for i in range(l1 + l2):
            result[i] += carry
            carry = result[i] // 10
            result[i] %= 10

        result_str = ''
        for i in range(l1 + l2 - 1, -1, -1):
            if result[i] == 0 and not result_str:
                continue
            result_str += str(result[i])

        return result_str or '0'
# @lc code=end

s = Solution()
print(s.multiply('999', '321'), str(999 * 321))
print(s.multiply('999', '321'), str(999 * 321))
print(s.multiply('999', '10'), str(999 * 10))
print(s.multiply('999', '99'), str(999 * 99))
print(s.multiply('0', '99'), str(0))
print(s.multiply('0', '0'), str(0))
