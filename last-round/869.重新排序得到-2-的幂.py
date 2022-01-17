#
# @lc app=leetcode.cn id=869 lang=python3
#
# [869] 重新排序得到 2 的幂
#
# https://leetcode-cn.com/problems/reordered-power-of-2/description/
#
# algorithms
# Medium (54.43%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 10.6K
# Testcase Example:  '1'
#
# 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
# 
# 如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：1
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：10
# 输出：false
# 
# 
# 示例 3：
# 
# 输入：16
# 输出：true
# 
# 
# 示例 4：
# 
# 输入：24
# 输出：false
# 
# 
# 示例 5：
# 
# 输入：46
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 10^9
# 
# 
#

# @lc code=start
from collections import Counter


def count(n: int) -> Counter:
    s = str(n)
    r = [int(c) for c in s]
    return Counter(r)


powers = [2 ** i for i in range(31)]
power_counters = [count(p) for p in powers]


def is_equal(c1: Counter, c2: Counter):
    keys1, keys2 = sorted(list(c1.keys())), sorted(list(c2.keys()))
    if keys1 != keys2:
        return False
    for key in keys1:
        if c1[key] != c2[key]:
            return False
    return True

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        counter = count(n)

        for p in power_counters:
            if is_equal(p, counter):
                return True
        return False
# @lc code=end
