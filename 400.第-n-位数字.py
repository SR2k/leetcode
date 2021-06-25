#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#
# https://leetcode-cn.com/problems/nth-digit/description/
#
# algorithms
# Medium (40.67%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    16.2K
# Total Submissions: 39.8K
# Testcase Example:  '3'
#
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 位数字。
# 
# 
# 
# 注意：n 是正数且在 32 位整数范围内（n < 2^31）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：3
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：11
# 输出：0
# 解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
# 
# 
#

# @lc code=start
class Solution:
    @staticmethod
    def get_count(n: int) -> int:
        if n == 0: return 0

        log_10 = -1
        x = n
        while x:
            x //= 10
            log_10 += 1

        ret = 0
        for i in range(log_10):
            ret += 9 * (10 ** i) * (i + 1)

        ret += (n - 10 ** log_10 + 1) * (log_10 + 1)
        return ret

    @staticmethod
    def get_n(num: int) -> int:
        left, right = 0, num

        while left + 1 < right:
            middle = (left + right) // 2
            curr_count = Solution.get_count(middle)

            if curr_count == num:
                return middle
            elif curr_count > num:
                right = middle
            else:
                left = middle

        # print(left, right, Solution.get_count(right))

        if Solution.get_count(left) < num: return right
        return left

    def findNthDigit(self, n: int) -> int:
        num = Solution.get_n(n)
        prev_count = Solution.get_count(num - 1)

        return int(str(num)[n - prev_count - 1])
# @lc code=end
