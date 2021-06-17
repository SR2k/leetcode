#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# algorithms
# Medium (60.67%)
# Likes:    916
# Dislikes: 0
# Total Accepted:    147.9K
# Total Submissions: 241.7K
# Testcase Example:  '12'
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
# 
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11
# 不是。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4
# 
# 示例 2：
# 
# 
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
import math

class Solution:
    sqrtMap: dict[int, int] = {}

    @staticmethod
    def getSqrt(n):
        if not n in Solution.sqrtMap:
            Solution.sqrtMap[n] = math.floor(math.sqrt(n)) + 1
        return Solution.sqrtMap[n]

    def numSquares(self, n: int) -> int:
        # bfs:
        queue: list[int] = [n]
        visited: set[int] = set()
        ret = 0

        while queue:
            ret += 1
            levelLen = len(queue)

            for _ in range(levelLen):
                num = queue.pop(0)

                for i in range(1, Solution.getSqrt(n)):
                    next = num - i * i
                    if next == 0: return ret
                    if next > 0 and not next in visited:
                        queue.append(next)
                        visited.add(next)

        # dp:
        # maxJ = math.floor(math.sqrt(n))

        # dp: list[int] = [i for i in range(n + 1)]

        # for i in range(2, maxJ + 1):
        #     s = i * i

        #     for j in range(n + 1):
        #         if j == 0:
        #             dp[j] = 0
        #         elif j >= s:
        #             dp[j] = min(dp[j], dp[j - s] + 1)

        # return dp[n]
# @lc code=end
