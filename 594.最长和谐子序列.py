#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#
# https://leetcode-cn.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (51.14%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    25.4K
# Total Submissions: 49.6K
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。
# 
# 现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。
# 
# 数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,3,2,2,5,2,3,7]
# 输出：5
# 解释：最长的和谐子序列是 [3,2,2,2,3]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3,4]
# 输出：2
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1,1,1,1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^9 
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counter = Counter(nums)

        ret = 0
        for k in counter.keys():
            c0 = counter[k]
            if k + 1 in counter:
                c1 = counter[k + 1]
                ret = max(ret, c0 + c1)
            if k - 1 in counter:
                c1 = counter[k - 1]
                ret = max(ret, c0 + c1)

        return ret
# @lc code=end

