#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode.cn/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (55.15%)
# Likes:    1374
# Dislikes: 0
# Total Accepted:    308.7K
# Total Submissions: 559.8K
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
        num_set = set(nums)
        result = 0

        while num_set:
            n = num_set.pop()
            curr = 1

            x = n - 1
            while x in num_set:
                curr += 1
                num_set.remove(x)
                x = x - 1

            x = n + 1
            while x in num_set:
                curr += 1
                num_set.remove(x)
                x = x + 1

            result = max(result, curr)

        return result
# @lc code=end
