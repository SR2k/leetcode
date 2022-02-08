#
# @lc app=leetcode.cn id=775 lang=python3
#
# [775] 全局倒置与局部倒置
#
# https://leetcode-cn.com/problems/global-and-local-inversions/description/
#
# algorithms
# Medium (45.93%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 10.2K
# Testcase Example:  '[1,0,2]'
#
# 给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。
# 
# 全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目：
# 
# 
# 0 
# nums[i] > nums[j]
# 
# 
# 局部倒置 的数目等于满足下述条件的下标 i 的数目：
# 
# 
# 0 
# nums[i] > nums[i + 1]
# 
# 
# 当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,0,2]
# 输出：true
# 解释：有 1 个全局倒置，和 1 个局部倒置。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,0]
# 输出：false
# 解释：有 2 个全局倒置，和 1 个局部倒置。
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 
# 0 
# nums 中的所有整数 互不相同
# nums 是范围 [0, n - 1] 内所有数字组成的一个排列
# 
# 
#

# @lc code=start
class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        len_n = len(nums)
        if len_n <= 2:
            return True

        m1, m2 = max(nums[0:2]), min(nums[0:2])
        for i in range(2, len_n):
            n = nums[i]
            if n < m2: # at least 2 global
                return False
            elif m2 < n < m1 and nums[i - 1] < n: # 1 global but no local
                return False
            elif m2 < n < m1:
                m1, m2 = m1, n
            else:
                m1, m2 = n, m1

        return True
# @lc code=end

