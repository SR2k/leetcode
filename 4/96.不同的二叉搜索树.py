#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (70.13%)
# Likes:    1696
# Dislikes: 0
# Total Accepted:    230.7K
# Total Submissions: 328.9K
# Testcase Example:  '3'
#
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：5
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 
# 
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
from functools import lru_cache


class Solution:
    @lru_cache
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        if n == 2:
            return 2

        result = 0
        for i in range(0, n - 1 + 1):
            result += self.numTrees(i) * self.numTrees(n - i - 1)

        return result
# @lc code=end
