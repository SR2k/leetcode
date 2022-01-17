#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#
# https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/description/
#
# algorithms
# Easy (52.79%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    36.9K
# Total Submissions: 69.7K
# Testcase Example:  '[4,2,3]\n1'
#
# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：
# 
# 
# 选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
# 
# 
# 重复这个过程恰好 k 次。可以多次选择同一个下标 i 。
# 
# 以这种方式修改数组后，返回数组 可能的最大和 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [4,2,3], k = 1
# 输出：5
# 解释：选择下标 1 ，nums 变为 [4,-2,3] 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,-1,0,2], k = 3
# 输出：6
# 解释：选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [2,-3,-1,5,-4], k = 2
# 输出：13
# 解释：选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^4
# -100 <= nums[i] <= 100
# 1 <= k <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        p = 0
        min_pos = float('inf')

        while k and p < len(nums) and nums[p] < 0:
            nums[p] = -nums[p]
            min_pos = min(nums[p], min_pos)
            p += 1
            k -= 1
        
        k %= 2
        result = sum(nums)
        if not k:
            return result

        if p < len(nums):
            min_pos = min(min_pos, nums[p])
        return result - 2 * min_pos
# @lc code=end

s = Solution()
print(s.largestSumAfterKNegations(nums = [4,2,3], k = 1))
print(s.largestSumAfterKNegations(nums = [3,-1,0,2], k = 3))
print(s.largestSumAfterKNegations(nums = [2,-3,-1,5,-4], k = 2))
print(s.largestSumAfterKNegations([-8,3,-5,-3,-5,-2], 6))
print(s.largestSumAfterKNegations([-4,-2,-3], 4))
print(s.largestSumAfterKNegations([-2,5,0,2,-2], 3))
