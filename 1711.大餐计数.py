#
# @lc app=leetcode.cn id=1711 lang=python3
#
# [1711] 大餐计数
#
# https://leetcode-cn.com/problems/count-good-meals/description/
#
# algorithms
# Medium (25.43%)
# Likes:    57
# Dislikes: 0
# Total Accepted:    10.3K
# Total Submissions: 33.1K
# Testcase Example:  '[1,3,5,7,9]'
#
# 大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。
# 
# 你可以搭配 任意 两道餐品做一顿大餐。
# 
# 给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i^​​​​​​​​​​​​​​
# 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 10^9 + 7 取余。
# 
# 注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：deliciousness = [1,3,5,7,9]
# 输出：4
# 解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
# 它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。
# 
# 
# 示例 2：
# 
# 
# 输入：deliciousness = [1,1,1,3,3,3,7]
# 输出：15
# 解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

import math
# @lc code=start
from collections import Counter


def get_max_pow(n: int) -> int:
    r = 0
    n *= 2

    while n > 1:
        n //= 2
        r += 1

    return r


def count(c: Counter, d: int) -> int:
    max_pow = get_max_pow(d)
    ret = 0

    if max_pow == d * 2:
        if c[d] >= 2:
            ret += c[d] * (c[d] - 1) // 2
        max_pow //= 2

    while max_pow:
        if max_pow % d == 0:
            target = max_pow // d
            if c[target]:
                ret += c[target] * c[d]
        max_pow //= 2

    return ret


class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        counter = Counter(deliciousness)
        ret = 0
        for d in counter:
            ret += count(counter, d)
        return ret

# @lc code=end
