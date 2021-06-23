#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#
# https://leetcode-cn.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (45.76%)
# Likes:    354
# Dislikes: 0
# Total Accepted:    38.4K
# Total Submissions: 83.9K
# Testcase Example:  '[1,2,3]'
#
# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i],
# answer[j]) 都应当满足：
# 
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 
# 
# 如果存在多个有效解子集，返回其中任何一个均可。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# nums 中的所有整数 互不相同
# 
# 
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        dp, ptr = [1], [None]
        max_len, max_index = 1, 0

        for i in range(1, len(nums)):
            dp.append(1)
            ptr.append(None)

            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    ptr[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        ret = []
        while max_index != None:
            ret.append(nums[max_index])
            max_index = ptr[max_index]

        ret.reverse()
        return ret
# @lc code=end

