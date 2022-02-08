#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Medium (35.11%)
# Likes:    3353
# Dislikes: 0
# Total Accepted:    928K
# Total Submissions: 2.6M
# Testcase Example:  '123'
#
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 123
# 输出：321
# 
# 
# 示例 2：
# 
# 
# 输入：x = -123
# 输出：-321
# 
# 
# 示例 3：
# 
# 
# 输入：x = 120
# 输出：21
# 
# 
# 示例 4：
# 
# 
# 输入：x = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 
# 
# 
#

# @lc code=start
MIN, MAX = -(2 ** 31), 2 ** 31 - 1 


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x == 0:
            return result

        flag = x // abs(x)
        x = abs(x)

        abs_max = MAX if flag > 0 else -MIN

        while x:
            digit = x % 10
            if result > (abs_max - digit) / 10:
                return 0
            result = result * 10 + digit
            x //= 10

        return flag * result
# @lc code=end

print(Solution().reverse(-4545))
print(Solution().reverse(54786))
print(Solution().reverse(2147483648))
print(Solution().reverse(8463847412))
print(Solution().reverse(7463847412))
