#
# @lc app=leetcode.cn id=879 lang=python3
#
# [879] 盈利计划
#
# https://leetcode-cn.com/problems/profitable-schemes/description/
#
# algorithms
# Hard (51.84%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 20.8K
# Testcase Example:  '5\n3\n[2,2]\n[2,3]'
#
# 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。
# 
# 第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。
# 
# 工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。
# 
# 有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# 输出：2
# 解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
# 总的来说，有两种计划。
# 
# 示例 2：
# 
# 
# 输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# 输出：7
# 解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
# 有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 1 
# 1 
# profit.length == group.length
# 0 
# 
# 
#

# @lc code=start
MD = 10 ** 9 + 7

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1

        for i in range(1, length + 1):
            members, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= members:
                        dp[i][j][k] += dp[i - 1][j - members][max(0, k - earn)]
                    dp[i][j][k] %= MD
        
        total = sum(dp[length][j][minProfit] for j in range(n + 1))
        return total % MD

    # def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
    #     jobCount = len(profit)

    #     dp: list[list[list[int]]] = []
    #     for i in range(jobCount):
    #         dp.append([])
    #         currProfit, currGroup = profit[i], group[i]

    #         for j in range(n + 1):
    #             dp[i].append([])

    #             for k in range(minProfit + 1):
    #                 dp[i][j].append(0)

    #                 if i == 0:
    #                     dp[i][j][k] = 1 if k == 0 or (k <= currProfit and currGroup) <= j else 0
    #                 elif j >= currGroup:
    #                     dp[i][j][k] = dp[i - 1][j - currGroup][max(0, k - currProfit)] + dp[i - 1][j][k]
    #                 else:
    #                     dp[i][j][k] = dp[i - 1][j][k]

    #                 dp[i][j][k] %= MD

    #                 # print('i=',i, 'j=', j, 'k=', k, 'dp=', dp[i][j][k])
    #     total = sum(dp[jobCount - 1][j][minProfit] for j in range(n + 1))
    #     return total % MD

# @lc code=end

# print(Solution().profitableSchemes(n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]))
