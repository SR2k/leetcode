#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode.cn/problems/reverse-integer/description/
#
# algorithms
# Medium (35.28%)
# Likes:    3525
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 2.9M
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
MAX_NEG_ABS = 2 ** 31
MAX_POS_ABS = MAX_NEG_ABS - 1


class Solution:
    def reverse(self, x: int, max_abs = MAX_POS_ABS) -> int:
        if x == 0:
            return x
        if x < 0:
            return -self.reverse(-x, MAX_NEG_ABS)

        result = 0
        while x:
            d = x % 10
            x //= 10

            if result > (max_abs - d) / 10:
                return 0

            result = result * 10 + d

        return result
# @lc code=end

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(0))

print(-(2 ** 31), s.reverse(-(2 ** 31)))
print((2 ** 31), s.reverse((2 ** 31)))
