#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (54.39%)
# Likes:    1014
# Dislikes: 0
# Total Accepted:    193.4K
# Total Submissions: 355.1K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 
# 示例 2：
# 
# 
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)

        max_length = 0
        for n in nums:
            curr_length = 1

            if n - 1 in nums:
                continue

            while n + 1 in nums:
                n = n + 1
                curr_length += 1

            max_length = max(curr_length, max_length)

        return max_length
# @lc code=end

