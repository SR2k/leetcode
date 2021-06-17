#   
# @lc app=leetcode.cn id=1449 lang=python3
#
# [1449] 数位成本和为目标值的最大数字
#
# https://leetcode-cn.com/problems/form-largest-integer-with-digits-that-add-up-to-target/description/
#
# algorithms
# Hard (42.59%)
# Likes:    38
# Dislikes: 0
# Total Accepted:    2.8K
# Total Submissions: 6.5K
# Testcase Example:  '[4,3,2,5,6,7,2,5,5]\n9'
#
# 给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：
# 
# 
# 给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
# 总成本必须恰好等于 target 。
# 添加的数位中没有数字 0 。
# 
# 
# 由于答案可能会很大，请你以字符串形式返回。
# 
# 如果按照上述要求无法得到任何整数，请你返回 "0" 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
# 输出："7772"
# 解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "977"
# 也是满足要求的数字，但 "7772" 是较大的数字。
# ⁠数字     成本
# ⁠ 1  ->   4
# ⁠ 2  ->   3
# ⁠ 3  ->   2
# ⁠ 4  ->   5
# ⁠ 5  ->   6
# ⁠ 6  ->   7
# ⁠ 7  ->   2
# ⁠ 8  ->   5
# ⁠ 9  ->   5
# 
# 
# 示例 2：
# 
# 
# 输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
# 输出："85"
# 解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
# 
# 
# 示例 3：
# 
# 
# 输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
# 输出："0"
# 解释：总成本是 target 的条件下，无法生成任何整数。
# 
# 
# 示例 4：
# 
# 
# 输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
# 输出："32211"
# 
# 
# 
# 
# 提示：
# 
# 
# cost.length == 9
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    @staticmethod
    def max(s1: str, s2: str) -> str:
        if s1 == None: return s2
        if s2 == None: return s1

        l1, l2 = len(s1), len(s2)

        if l1 > l2: return s1
        if l2 > l1: return s2

        for i in range(l1):
            if s1[i] > s2[i]: return s1
            if s2[i] > s1[i]: return s2

        return s1

    def largestNumber(self, costs: list[int], target: int) -> str:
        dp = []

        map: dict[int, int] = {}
        for i in range(len(costs)): map[costs[i]] = i + 1

        digits = list(map.values())
        digits.sort()

        dp = [None for i in range(target + 1)]

        for i in range(len(digits)):
            digit = str(digits[i])
            cost = costs[digits[i] - 1]

            for budget in range(1, target + 1):
                if budget < cost:
                    pass
                elif budget == cost:
                    dp[budget] = Solution.max(dp[budget], digit)
                elif dp[budget - cost] != None:
                    dp[budget] = Solution.max(dp[budget], digit + dp[budget - cost])
                else:
                    pass
            # print(dp)

        return dp[budget] or '0'

# @lc code=end

# print(Solution().largestNumber([4,3,2,5,6,7,2,5,5], 9))
# print(Solution().largestNumber([7,6,5,5,5,6,8,7,8], 12))
# print(Solution().largestNumber([2,4,6,2,4,6,4,4,4], 5))
# print(Solution().largestNumber([6,10,15,40,40,40,40,40,40], 47))
# print(Solution().largestNumber([1,1,1,1,1,1,1,1,1], 9))
