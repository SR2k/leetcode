#
# @lc app=leetcode.cn id=689 lang=python3
#
# [689] 三个无重叠子数组的最大和
#
# https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
#
# algorithms
# Hard (49.16%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    7.7K
# Total Submissions: 14.1K
# Testcase Example:  '[1,2,1,2,6,7,5,1]\n2'
#
# 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且 3 * k 项的和最大的子数组，并返回这三个子数组。
# 
# 以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,1,2,6,7,5,1], k = 2
# 输出：[0,3,5]
# 解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
# 也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
# 输出：[0,2,4]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] < 2^16
# 1 <= k <= floor(nums.length / 3)
# 
# 
#

# @lc code=start
from collections import deque


def max_and_min_pos(sum_a: int, pos_a: list[int], sum_b: int, pos_b: list[int]):
    if sum_b > sum_a:
        return sum_b, pos_b
    return sum_a, pos_a


class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        dp = deque([[0, 0, 0] for _ in range(k)])
        result = deque([[[k - 1], [], []] for _ in range(k)])

        curr_sum = sum(nums[:k - 1] or [0])

        for i in range(k - 1, len(nums)):
            curr_result = [0, 0, 0]
            curr_pos = [[], [], []]

            curr_sum += nums[i] - (nums[i - k] if i >= k else 0)
            curr_group_begin = i - k + 1

            s, pos = max_and_min_pos(dp[-1][0], result[-1][0], curr_sum, [curr_group_begin])
            curr_result[0] = s
            curr_pos[0] = pos

            if i + 1 >= 2 * k:
                s, pos = max_and_min_pos(dp[-1][1], result[-1][1], dp[0][0] + curr_sum, result[0][0] + [curr_group_begin])
                curr_result[1] = s
                curr_pos[1] = pos
            if i + 1 >= 3 * k:
                s, pos = max_and_min_pos(dp[-1][2], result[-1][2], dp[0][1] + curr_sum, result[0][1] + [curr_group_begin])
                curr_result[2] = s
                curr_pos[2] = pos

            dp.popleft()
            result.popleft()
            dp.append(curr_result)
            result.append(curr_pos)

        return result[-1][-1]
# @lc code=end

s = Solution()
print(s.maxSumOfThreeSubarrays(nums = [1,2,1,2,6,7,5,1], k = 2))
print(s.maxSumOfThreeSubarrays(nums = [1,2,1,2,1,2,1,2,1], k = 2))
