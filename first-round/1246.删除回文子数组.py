#
# @lc app=leetcode.cn id=1246 lang=python3
#
# [1246] 删除回文子数组
#
# https://leetcode-cn.com/problems/palindrome-removal/description/
#
# algorithms
# Hard (48.29%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    3K
# Total Submissions: 6.2K
# Testcase Example:  '[1,2]'
#
# 给你一个整数数组 arr，每一次操作你都可以选择并删除它的一个 回文 子数组 arr[i], arr[i+1], ..., arr[j]（ i <=
# j）。
# 
# 注意，每当你删除掉一个子数组，右侧元素都会自行向前移动填补空位。
# 
# 请你计算并返回从数组中删除所有数字所需的最少操作次数。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [1,2]
# 输出：2
# 
# 
# 示例 2：
# 
# 输入：arr = [1,3,4,1,5]
# 输出：3
# 解释：先删除 [4]，然后删除 [1,3,1]，最后再删除 [5]。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 100
# 1 <= arr[i] <= 20
# 
# 
#

# @lc code=start
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
# @lc code=end

