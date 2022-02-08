#
# @lc app=leetcode.cn id=483 lang=python3
#
# [483] 最小好进制
#
# https://leetcode-cn.com/problems/smallest-good-base/description/
#
# algorithms
# Hard (43.65%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    5.4K
# Total Submissions: 9.8K
# Testcase Example:  '"13"'
#
# 对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。
# 
# 以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。
# 
# 
# 
# 示例 1：
# 
# 
# 输入："13"
# 输出："3"
# 解释：13 的 3 进制是 111。
# 
# 
# 示例 2：
# 
# 
# 输入："4681"
# 输出："8"
# 解释：4681 的 8 进制是 11111。
# 
# 
# 示例 3：
# 
# 
# 输入："1000000000000000000"
# 输出："999999999999999999"
# 解释：1000000000000000000 的 999999999999999999 进制是 11。
# 
# 
# 
# 
# 提示：
# 
# 
# n的取值范围是 [3, 10^18]。
# 输入总是有效且没有前导 0。
# 
# 
# 
# 
#

import math

# @lc code=start
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        x = int(n)

        # def get_max_digits(n: int):
        #     return math.floor(math.log(1 + n, 2))

        for i in range(59, 2 - 1, -1):
            # print(i)
            l, r = 2, x - 1

            while l + 1 < r:
                mid = (r - l) // 2 + l
                curr = (1 - mid ** i) // (1 - mid)

                if curr == x:
                    return str(mid)
                elif curr > x:
                    r = mid
                else:
                    l = mid

            if (1 - l ** i) // (1 - l) == x:
                return str(l)
            elif (1 - r ** i) // (1 - r) == x:
                return str(r)

        return str(x - 1)
# @lc code=end

# print(Solution().smallestGoodBase(str(10 ** 18)))
