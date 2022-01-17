#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 重复 N 次的元素
#
# https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array/description/
#
# algorithms
# Easy (67.70%)
# Likes:    99
# Dislikes: 0
# Total Accepted:    36K
# Total Submissions: 53.2K
# Testcase Example:  '[1,2,3,3]'
#
# 在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
# 
# 返回重复了 N 次的那个元素。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[1,2,3,3]
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：[2,1,2,5,3,2]
# 输出：2
# 
# 
# 示例 3：
# 
# 
# 输入：[5,1,5,2,5,3,5,4]
# 输出：5
# 
# 
# 
# 
# 提示：
# 
# 
# 4 
# 0 
# A.length 为偶数
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        count = {}

        for n in nums:
            if n in count:
                return n
            else:
                count[n] = 1
# @lc code=end

