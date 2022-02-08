#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (53.32%)
# Likes:    2124
# Dislikes: 0
# Total Accepted:    669.1K
# Total Submissions: 1.3M
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]

        if n <= 2:
            return dp[n - 1]

        for _ in range(3, n + 1):
            dp = [dp[1], dp[0] + dp[1]]
        return dp[-1]
# @lc code=end

print(Solution().climbStairs(1))
print(Solution().climbStairs(2))
print(Solution().climbStairs(45))
print(Solution().climbStairs(16))
print(Solution().climbStairs(4))
print(Solution().climbStairs(11))
