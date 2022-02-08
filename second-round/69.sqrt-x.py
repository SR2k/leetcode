#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (39.05%)
# Likes:    867
# Dislikes: 0
# Total Accepted:    443.8K
# Total Submissions: 1.1M
# Testcase Example:  '4'
#
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
# 
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 4
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, 46340

        while left + 1 < right:
            middle = (left + right) // 2
            squared = middle * middle

            if squared == x:
                return middle
            elif squared > x:
                right = middle
            else:
                left = middle

        if right * right <= x:
            return right
        return left
# @lc code=end
