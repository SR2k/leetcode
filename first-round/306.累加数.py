#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#
# https://leetcode-cn.com/problems/additive-number/description/
#
# algorithms
# Medium (33.57%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    15K
# Total Submissions: 44.6K
# Testcase Example:  '"112358"'
#
# 累加数是一个字符串，组成它的数字可以形成累加序列。
# 
# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
# 
# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
# 
# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
# 
# 示例 1:
# 
# 输入: "112358"
# 输出: true 
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 
# 
# 示例 2:
# 
# 输入: "199100199"
# 输出: true 
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
# 
# 进阶:
# 你如何处理一个溢出的过大的整数输入?
# 
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def helper(a0: int, a1: int, b0: int, b1: int) -> bool:
            if num[a0] == '0' and a1 > a0:
                return False
            if num[b0] == '0' and b1 > b0:
                return False

            n1, n2 = int(num[a0:a1 + 1]), int(num[b0:b1 + 1])
            n3 = str(n1 + n2)
            c0, c1 = b1 + 1, b1 + len(n3)

            if num[c0:c1 + 1] != n3:
                return False
            if c1 == len(num) - 1:
                return True

            return helper(b0, b1, c0, c1)

        for l1 in range(len(num) - 1):
            for r1 in range(l1 + 1, len(num)):
                if helper(0, l1, l1 + 1, r1):
                    return True
        return False
# @lc code=end
