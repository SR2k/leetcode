#
# @lc app=leetcode.cn id=1940 lang=python3
#
# [1940] 排序数组之间的最长公共子序列
#
# https://leetcode-cn.com/problems/longest-common-subsequence-between-sorted-arrays/description/
#
# algorithms
# Medium (83.24%)
# Likes:    1
# Dislikes: 0
# Total Accepted:    326
# Total Submissions: 393
# Testcase Example:  '[[1,3,4],[1,4,7,9]]'
#
# 给定一个由整数数组组成的数组arrays，其中arrays[i]是严格递增排序的，返回一个表示所有数组之间的最长公共子序列的整数数组。
# 
# 子序列是从另一个序列派生出来的序列，删除一些元素或不删除任何元素，而不改变其余元素的顺序。
# 
# 示例1:
# 
# 
# 输入: arrays = [[1,3,4],
# [1,4,7,9]]
# 输出: [1,4]
# 解释: 这两个数组中的最长子序列是[1,4]。
# 
# 
# 示例 2:
# 
# 
# 输入: arrays = [[2,3,6,8],
# [1,2,3,5,6,7,10],
# [2,3,4,6,9]]
# 输出: [2,3,6]
# 解释: 这三个数组中的最长子序列是[2,3,6]。
# 
# 
# 示例 3:
# 
# 
# 输入: arrays = [[1,2,3,4,5],
# [6,7,8]]
# 输出: []
# 解释: 这两个数组之间没有公共子序列。
# 
# 
# 
# 
# 限制条件:
# 
# 
# 2 
# 1 
# 1 
# arrays[i] 是严格递增排序.
# 
# 
#

# @lc code=start
# def b_find(arr, n):
#     if arr[0] > n or arr[-1] < n:
#         return False

#     left, right = 0, len(arr) - 1

#     while left + 1 < right:
#         middle = (left + right) // 2
#         num_middle = arr[middle]

#         if num_middle == n:
#             return True
#         elif num_middle > n:
#             right = middle
#         else:
#             left = middle

#     return arr[left] == n or arr[right] == n


# class Solution:
#     def longestCommonSubsequence(self, arrays: list[list[int]]) -> list[int]:
#         r = None
#         for l in arrays:
#             if not r or len(r) > len(l):
#                 r = l

#         result = []
#         for n in r:
#             flag = True
#             for arr in arrays:
#                 if not b_find(arr, n):
#                     flag = False
#                     break
#             if flag:
#                 result.append(n)

#         return result



from collections import defaultdict


class Solution:
    def longestCommonSubsequence(self, arrays: list[list[int]]) -> list[int]:
        count = defaultdict(int)
        for arr in arrays:
            for n in arr:
                count[n] += 1

        return list(filter(lambda x: count[x] == len(arrays), count.keys()))
# @lc code=end
