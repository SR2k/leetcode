#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (44.96%)
# Likes:    862
# Dislikes: 0
# Total Accepted:    205.5K
# Total Submissions: 457.8K
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
        if num1 == '0' or num2 == '0':
            return '0'

        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                r = (ord(num1[-(i + 1)]) - ord('0')) * (ord(num2[-(j + 1)]) - ord('0'))
                result[i + j] += r

        carry = 0
        for i in range(len(result)):
            d = result[i] + carry
            carry = d // 10
            result[i] = str(d % 10)

        while result[-1] == '0':
            result.pop()

        result.reverse()
        return "".join(result)
# @lc code=end

print(Solution().multiply("2", "3"))
print(Solution().multiply("123", "456"))
