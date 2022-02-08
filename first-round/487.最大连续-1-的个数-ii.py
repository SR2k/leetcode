#
# @lc app=leetcode.cn id=487 lang=python3
#
# [487] 最大连续1的个数 II
#
# https://leetcode-cn.com/problems/max-consecutive-ones-ii/description/
#
# algorithms
# Medium (57.94%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    3.6K
# Total Submissions: 6.3K
# Testcase Example:  '[1,0,1,1,0]'
#
# 给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。
# 
# 示例 1：
# 
# 输入：[1,0,1,1,0]
# 输出：4
# 解释：翻转第一个 0 可以得到最长的连续 1。
# 当翻转以后，最大连续 1 的个数为 4。
# 
# 
# 
# 
# 注：
# 
# 
# 输入数组只包含 0 和 1.
# 输入数组的长度为正整数，且不超过 10,000
# 
# 
# 
# 
# 进阶：
# 如果输入的数字是作为 无限流 逐个输入如何处理？换句话说，内存不能存储下所有从流中输入的数字。您可以有效地解决吗？
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        prev_0_index = -1
        ret = 1

        for right in range(len(nums)):
            n = nums[right]

            if n == 1:
                pass
            elif prev_0_index < 0:
                prev_0_index = right
            else:
                left = prev_0_index + 1
                prev_0_index = right

            ret = max(right - left + 1, ret)

        return ret
# @lc code=end

