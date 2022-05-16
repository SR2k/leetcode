#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (48.33%)
# Likes:    1419
# Dislikes: 0
# Total Accepted:    414.6K
# Total Submissions: 857.8K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2：
# 
# 
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
# 
# 
# 提示：
# 
# 
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
# 
# 
#

# @lc code=start
from random import randrange


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        self.quick_sort(intervals, 0, len(intervals) - 1)
        result = []

        for begin, end in intervals:
            if not result or result[-1][1] < begin:
                result.append([begin, end])
            else:
                result[-1][1] = max(end, result[-1][1])

        return result


    def quick_sort(self, arr: list[list[int]], left: int, right: int):
        if left >= right:
            return

        i = self.partition(arr, left, right)
        self.quick_sort(arr, left, i - 1)
        self.quick_sort(arr, i + 1, right)


    def partition(self, arr: list[list[int]], left: int, right: int):
        rand = randrange(left, right + 1)
        self.swap(arr, left, rand)

        i, j = left, right
        pivot = arr[left][0]
        while i < j:
            while i < j and arr[j][0] > pivot:
                j -= 1
            while i < j and arr[i][0] <= pivot:
                i += 1
            self.swap(arr, i, j)

        self.swap(arr, left, i)
        return i


    def swap(self, arr: list, i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]
# @lc code=end
