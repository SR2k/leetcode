#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
# https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (41.34%)
# Likes:    589
# Dislikes: 0
# Total Accepted:    155.8K
# Total Submissions: 376.8K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
# 
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始
# 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
# 
# 给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值
# target ，则返回 true ，否则返回 false 。
# 
# 你必须尽可能减少整个操作步骤。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,5,6,0,0,1,2], target = 0
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,5,6,0,0,1,2], target = 3
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4
# 
# 
# 
# 
# 进阶：
# 
# 
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return True

            elif nums[left] == nums[middle] == nums[right]:
                left += 1
                right -= 1

            elif nums[left] <= nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle
                else:
                    left = middle

            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle
                else:
                    right = middle

        return nums[left] == target or nums[right] == target
# @lc code=end

# 001111000000000

#        7 7 7 7 7 7 8 9 # 无重复项目 or 重复项目不跨越头尾
# 左有序： l <= mid

#        |       |         |
#        7 8 9 9 9 7 7 7 7 7 # 重复项目跨越头尾 arr[0] === arr[1]
# 左有序：l < mid

# 无法判断：arr[l] === arr[mid] === arr[r]

# |       |       |
# 7 8 9 9 7 7 7 7 7 # 左侧有序
# 7 8 9 9 1 7 7 7 7 # 右侧有序
