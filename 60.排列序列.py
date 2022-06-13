#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#
# https://leetcode.cn/problems/permutation-sequence/description/
#
# algorithms
# Hard (53.05%)
# Likes:    676
# Dislikes: 0
# Total Accepted:    108.2K
# Total Submissions: 203.9K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
# 
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 给定 n 和 k，返回第 k 个排列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3, k = 3
# 输出："213"
# 
# 
# 示例 2：
# 
# 
# 输入：n = 4, k = 9
# 输出："2314"
# 
# 
# 示例 3：
# 
# 
# 输入：n = 3, k = 1
# 输出："123"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
from math import ceil


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(x) for x in range(1, n + 1)]
        result = []

        while nums:
            digit, k = self.pop_num(nums, k)
            result.append(digit)

        return ''.join(result)


    def pop_num(self, candidates: list[int], k: int):
        group_size = 1
        for i in range(1, len(candidates) - 1 + 1):
            group_size *= i

        index = ceil(k / group_size)
        result = candidates[index - 1]
        candidates.remove(result)

        return result, k % group_size
# @lc code=end

print(Solution().getPermutation(n = 3, k = 3)) # "213"
print(Solution().getPermutation(n = 4, k = 9)) # "2314"
print(Solution().getPermutation(n = 3, k = 1)) # "123"
