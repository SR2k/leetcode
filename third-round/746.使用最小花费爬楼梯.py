#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#
# https://leetcode-cn.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (60.60%)
# Likes:    819
# Dislikes: 0
# Total Accepted:    180.7K
# Total Submissions: 297.4K
# Testcase Example:  '[10,15,20]'
#
# 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
# 
# 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
# 
# 请你计算并返回达到楼梯顶部的最低花费。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：cost = [10,15,20]
# 输出：15
# 解释：你将从下标为 1 的台阶开始。
# - 支付 15 ，向上爬两个台阶，到达楼梯顶部。
# 总花费为 15 。
# 
# 
# 示例 2：
# 
# 
# 输入：cost = [1,100,1,1,1,100,1,1,100,1]
# 输出：6
# 解释：你将从下标为 0 的台阶开始。
# - 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
# - 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
# - 支付 1 ，向上爬一个台阶，到达楼梯顶部。
# 总花费为 6 。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
# 
# 
#

# [10, 15, 20]

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev = [0, 0]

        for i in range(2, len(cost)):
            curr = min(prev[-1] + cost[i - 1], prev[-2] + cost[i - 2])
            prev = [prev[1], curr]

        return min(prev[1] + cost[-1], prev[0] + cost[-2])
# @lc code=end

s = Solution()
print(s.minCostClimbingStairs([10,15,20]))
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print(s.minCostClimbingStairs([1,100]))
