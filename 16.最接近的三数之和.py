#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.88%)
# Likes:    1056
# Dislikes: 0
# Total Accepted:    311.7K
# Total Submissions: 679.3K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
# 
# 返回这三个数的和。
# 
# 假定每组输入只存在恰好一个解。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,0,0], target = 1
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        result = float('inf')
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            k = len(nums) - 1

            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                while j < k and nums[i] + nums[j] + nums[k] > target:
                    sum = nums[i] + nums[j] + nums[k]
                    delta = abs(sum - target)
                    result = sum if delta < abs(result - target) else result
                    k -= 1

                if j == k:
                    break

                sum = nums[i] + nums[j] + nums[k]
                delta = abs(sum - target)
                result = sum if delta < abs(result - target) else result

                if result == target:
                    return result

        return result
# @lc code=end

