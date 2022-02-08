#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
# https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.70%)
# Likes:    1275
# Dislikes: 0
# Total Accepted:    176.9K
# Total Submissions: 395.8K
# Testcase Example:  '[1,1,1]\n2'
#
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3], k = 3
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_cnt = defaultdict(int)
        prefix_sum_cnt[0] = 1
        result = 0

        for n in nums:
            prefix_sum += n
            result += prefix_sum_cnt[prefix_sum - k]
            prefix_sum_cnt[prefix_sum] += 1

        return result
# @lc code=end
