#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#
# https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (46.85%)
# Likes:    351
# Dislikes: 0
# Total Accepted:    42.7K
# Total Submissions: 90.9K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# 给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的（连续、非空） 子数组 的数目。
# 
# 子数组 是数组的 连续 部分。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [4,5,0,-2,-3,1], k = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 k = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [5], k = 9
# 输出: 0
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# 2 <= k <= 10^4
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        modulo = 0
        counter = defaultdict(int)
        counter[0] = 1
        result = 0

        for n in nums:
            modulo = (modulo + n) % k
            result += counter[modulo]
            counter[modulo] += 1

        return result
# @lc code=end
