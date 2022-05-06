#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (39.45%)
# Likes:    1134
# Dislikes: 0
# Total Accepted:    271.9K
# Total Submissions: 689.1K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a],
# nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
# 
# 
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# 
# 你可以按 任意顺序 返回答案 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []

        for a in range(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                d = len(nums) - 1

                for c in range(b + 1, len(nums) - 1):
                    if c > b + 1 and nums[c] == nums[c - 1]:
                        continue

                    while c < d and nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1

                    if c == d:
                        break

                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])

        return result
# @lc code=end
