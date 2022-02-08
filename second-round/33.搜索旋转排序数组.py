#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (42.94%)
# Likes:    1725
# Dislikes: 0
# Total Accepted:    408.5K
# Total Submissions: 950.2K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
# 
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 ）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ...,
# nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如，
# [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
# 
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 
# 示例 3：
# 
# 
# 输入：nums = [1], target = 0
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^4 
# nums 中的每个值都 独一无二
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 
# 
# 
# 
# 
# 进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？
# 
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            middle = (left + right) // 2
            num_middle = nums[middle]

            if num_middle == target:
                return middle
            elif num_middle >= nums[0]:
                if nums[0] <= target <= num_middle:
                    right = middle
                else:
                    left = middle
            else:
                if target >= nums[0] or target < num_middle:
                    right = middle
                else:
                    left = middle

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
# @lc code=end

s = Solution()
print(s.search(nums = [4,5,6,7,0,1,2], target = 0))
print(s.search(nums = [4,5,6,7,0,1,2], target = 3))
print(s.search(nums = [0,1,2,4,5,6,7], target = 0))
print(s.search(nums = [0,1,2,4,5,6,7], target = 7))
print(s.search(nums = [0,1,2,4,5,6,7], target = 4))
print(s.search(nums = [0,1,2,4,5,6,7], target = 3))
print(s.search(nums = [1], target = 0))
