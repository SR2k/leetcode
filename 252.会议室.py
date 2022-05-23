#
# @lc app=leetcode.cn id=252 lang=python3
#
# [252] 会议室
#
# https://leetcode.cn/problems/meeting-rooms/description/
#
# algorithms
# Easy (57.15%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    17.4K
# Total Submissions: 30.5K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# 给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi]
# ，请你判断一个人是否能够参加这里面的全部会议。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：false
# 
# 
# 示例 2：
# 
# 
# 输入：intervals = [[7,10],[2,4]]
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# intervals[i].length == 2
# 0 i i 
# 
# 
#

# @lc code=start
from re import L
from typing import Callable, Any
from random import randrange


class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        Solution.quick_sort(intervals, lambda a, b: a[0] - b[0], 0, len(intervals) - 1)

        prev_end = -1
        for begin, end in intervals:
            if begin < prev_end:
                return False
            prev_end = end

        return True


    @staticmethod
    def quick_sort(arr: list, cmp: Callable[[Any, Any], int], left: int, right: int):
        if left >= right:
            return

        i = Solution.partition(arr, cmp, left, right)
        Solution.quick_sort(arr, cmp, left, i - 1)
        Solution.quick_sort(arr, cmp, i + 1, right)


    @staticmethod
    def partition(arr: list, cmp: Callable[[Any, Any], int], left: int, right: int):
        rand = randrange(left, right + 1)
        Solution.swap(arr, left, rand)

        pivot = arr[left]
        i, j = left, right

        while i < j:
            while i < j and cmp(arr[j], pivot) > 0:
                j -= 1
            while i < j and cmp(arr[i], pivot) <= 0:
                i += 1

            Solution.swap(arr, i, j)

        Solution.swap(arr, left, i)
        return i


    @staticmethod
    def swap(arr: list, i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]
# @lc code=end
