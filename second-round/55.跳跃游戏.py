#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (43.45%)
# Likes:    1595
# Dislikes: 0
# Total Accepted:    391K
# Total Submissions: 899.9K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个下标。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_can_jump = 0

        for i, n in enumerate(nums):
            if i > max_can_jump:
                break
            max_can_jump = max(n + i, max_can_jump)

        return max_can_jump >= len(nums) - 1
# @lc code=end

s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
