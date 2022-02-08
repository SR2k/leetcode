#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (45.74%)
# Likes:    797
# Dislikes: 0
# Total Accepted:    370.2K
# Total Submissions: 803.1K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 
# 
# 示例 2：
# 
# 
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 
# 
# 示例 3：
# 
# 
# 输入：digits = [0]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        d = 0
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += d
            d = digits[i] // 10
            digits[i] %= 10

        if d:
            return [1] + digits
        return digits
# @lc code=end

