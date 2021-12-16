#
# @lc app=leetcode.cn id=2016 lang=python3
#
# [2016] 增量元素之间的最大差值
#
# https://leetcode-cn.com/problems/maximum-difference-between-increasing-elements/description/
#
# algorithms
# Easy (55.35%)
# Likes:    5
# Dislikes: 0
# Total Accepted:    6.4K
# Total Submissions: 11.5K
# Testcase Example:  '[7,1,5,4]'
#
# 给你一个下标从 0 开始的整数数组 nums ，该数组的大小为 n ，请你计算 nums[j] - nums[i] 能求得的 最大差值 ，其中 0 <=
# i < j < n 且 nums[i] < nums[j] 。
# 
# 返回 最大差值 。如果不存在满足要求的 i 和 j ，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [7,1,5,4]
# 输出：4
# 解释：
# 最大差值出现在 i = 1 且 j = 2 时，nums[j] - nums[i] = 5 - 1 = 4 。
# 注意，尽管 i = 1 且 j = 0 时 ，nums[j] - nums[i] = 7 - 1 = 6 > 4 ，但 i > j 不满足题面要求，所以
# 6 不是有效的答案。
# 
# 
# 示例 2：
# 
# 输入：nums = [9,4,3,2]
# 输出：-1
# 解释：
# 不存在同时满足 i < j 和 nums[i] < nums[j] 这两个条件的 i, j 组合。
# 
# 
# 示例 3：
# 
# 输入：nums = [1,5,2,10]
# 输出：9
# 解释：
# 最大差值出现在 i = 0 且 j = 3 时，nums[j] - nums[i] = 10 - 1 = 9 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 2 <= n <= 1000
# 1 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        result, curr_min = float('-inf'), nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            if n > curr_min:
                result = max(n - curr_min, result)
            curr_min = min(n, curr_min)

        return max(result, -1)
# @lc code=end

s = Solution()
print(s.maximumDifference([7,1,5,4]))
print(s.maximumDifference([9,4,3,2]))
print(s.maximumDifference([1,5,2,10]))
print(s.maximumDifference([999,997,980,976,948,940,938,928,924,917,907,907,881,878,864,862,859,857,848,840,824,824,824,805,802,798,788,777,775,766,755,748,735,732,727,705,700,697,693,679,676,644,634,624,599,596,588,583,562,558,553,539,537,536,509,491,485,483,454,449,438,425,403,368,345,327,287,285,270,263,255,248,235,234,224,221,201,189,187,183,179,168,155,153,150,144,107,102,102,87,80,57,55,49,48,45,26,26,23,15]))
