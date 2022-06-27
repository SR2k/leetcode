#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode.cn/problems/add-strings/description/
#
# algorithms
# Easy (54.77%)
# Likes:    563
# Dislikes: 0
# Total Accepted:    203.2K
# Total Submissions: 371.1K
# Testcase Example:  '"11"\n"123"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
# 
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num1 = "11", num2 = "123"
# 输出："134"
# 
# 
# 示例 2：
# 
# 
# 输入：num1 = "456", num2 = "77"
# 输出："533"
# 
# 
# 示例 3：
# 
# 
# 输入：num1 = "0", num2 = "0"
# 输出："0"
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= num1.length, num2.length <= 10^4
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len = max(len(num1), len(num2))
        result = []
        carry = 0

        for i in range(1, max_len + 1):
            n1 = (ord(num1[-i]) - ord('0')) if i <= len(num1) else 0
            n2 = (ord(num2[-i]) - ord('0')) if i <= len(num2) else 0

            d = n1 + n2 + carry
            carry = d // 10
            d %= 10

            result.append(d)

        if carry:
            result.append(carry)

        result.reverse()
        return "".join(str(x) for x in result) or '0'
# @lc code=end
