#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小操作次数使数组元素相等
#
# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/description/
#
# algorithms
# Easy (55.60%)
# Likes:    305
# Dislikes: 0
# Total Accepted:    36.1K
# Total Submissions: 61.7K
# Testcase Example:  '[1,2,3]'
#
# 给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：3
# 解释：
# 只需要3次操作（注意每次操作会增加两个元素的值）：
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,1,1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 答案保证符合 32-bit 整数
# 
# 
#

# @lc code=start
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_n = min(nums)
        r = 0
        for n in nums:
            r += (n - min_n)
        return r
# @lc code=end

s = Solution()
print(s.minMoves([-100,0,100]))
