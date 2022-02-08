#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (34.29%)
# Likes:    4207
# Dislikes: 0
# Total Accepted:    766.6K
# Total Submissions: 2.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
# 且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [0]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^5 
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j, k = i + 1, len(nums) - 1

            while True:
                while j < k and nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                while j < k and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1

                if j >= k:
                    break

                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

                if j >= k:
                    break

        return result
# @lc code=end

print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]))

# [[-82,-11,93],[-82,13,69],[-82,17,65],[-82,21,61],[-82,26,56],[-82,33,49],[-82,34,48],[-82,36,46],[-70,-14,84],[-70,-6,76],[-70,1,69],[-70,13,57],[-70,15,55],[-70,21,49],[-70,34,36],[-66,-11,77],[-66,-3,69],[-66,1,65],[-66,10,56],[-66,17,49],[-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],[-49,13,36],[-49,15,34],[-49,21,28],[-43,-14,57],[-43,-6,49],[-43,-3,46],[-43,10,33],[-43,12,31],[-43,15,28],[-43,17,26],[-29,-14,43],[-29,1,28],[-29,12,17],[-14,-3,17],[-14,1,13],[-14,2,12],[-11,-6,17],[-11,1,10],[-3,1,2]]
