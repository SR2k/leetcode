#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (40.45%)
# Likes:    877
# Dislikes: 0
# Total Accepted:    188.7K
# Total Submissions: 465.9K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 
# 注意：答案中不可以包含重复的四元组。
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
# 输入：nums = [], target = 0
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ret = []
        total = len(nums)

        for i1 in range(0, total - 3):
            num1 = nums[i1]

            for i2 in range(i1 + 1, total - 2):
                num2 = nums[i2]
                i3, i4 = i2 + 1, total - 1

                while i3 < i4:
                    num3, num4 = nums[i3], nums[i4]
                    curr = [num1, num2, num3, num4]
                    curr_sum = sum(curr)
                    if curr_sum == target:
                        ret.append(curr)
                        while i3 < i4 and nums[i3] == nums[i3 + 1]: i3 += 1
                        while i4 > i3 and nums[i4] == nums[i4 - 1]: i4 -= 1
                        i4 -= 1
                        i3 += 1
                    elif curr_sum > target:
                        i4 -= 1
                    else:
                        i3 += 1

            while i2 < i1 and nums[i2] == nums[i2 + 1]: i2 += 1

        return ret

# @lc code=end

print(Solution().fourSum([1,0,-1,0,-2,2], 0))
