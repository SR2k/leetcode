#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#
# https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position/description/
#
# algorithms
# Easy (69.38%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    20.2K
# Total Submissions: 29.2K
# Testcase Example:  '[1,2,3]'
#
# 数轴上放置了一些筹码，每个筹码的位置存在数组 chips 当中。
# 
# 你可以对 任何筹码 执行下面两种操作之一（不限操作次数，0 次也可以）：
# 
# 
# 将第 i 个筹码向左或者右移动 2 个单位，代价为 0。
# 将第 i 个筹码向左或者右移动 1 个单位，代价为 1。
# 
# 
# 最开始的时候，同一位置上也可能放着两个或者更多的筹码。
# 
# 返回将所有筹码移动到同一位置（任意位置）上所需要的最小代价。
# 
# 
# 
# 示例 1：
# 
# 输入：chips = [1,2,3]
# 输出：1
# 解释：第二个筹码移动到位置三的代价是 1，第一个筹码移动到位置三的代价是 0，总代价为 1。
# 
# 
# 示例 2：
# 
# 输入：chips = [2,2,2,3,3]
# 输出：2
# 解释：第四和第五个筹码移动到位置二的代价都是 1，所以最小总代价为 2。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= chips.length <= 100
# 1 <= chips[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count = [0, 0]
        for pos in position: count[pos % 2] += 1
        return min(count)
# @lc code=end

