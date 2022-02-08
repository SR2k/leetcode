#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (38.15%)
# Likes:    707
# Dislikes: 0
# Total Accepted:    151.9K
# Total Submissions: 398.2K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 
# 
# 示例 2：
# 
# 输入：n = 0
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：n = 1
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 5 * 10^6
# 
# 
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True for i in range(n)]
        count = 0

        for i in range(2, n):
            if not is_prime[i]: continue

            count += 1
            t = i * i

            while t < n:
                is_prime[t] = False
                t += t

        return count
# @lc code=end

