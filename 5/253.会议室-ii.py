#
# @lc app=leetcode.cn id=253 lang=python3
#
# [253] 会议室 II
#
# https://leetcode.cn/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (51.40%)
# Likes:    435
# Dislikes: 0
# Total Accepted:    47.8K
# Total Submissions: 92.9K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# 给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回
# 所需会议室的最小数量 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：intervals = [[7,10],[2,4]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= intervals.length <= 10^4
# 0 <= starti < endi <= 10^6
# 
# 
#

# @lc code=start
from typing import Callable, Any


class Heap:
    def __init__(self, values = [], cmp: Callable[[Any, Any], int] = None) -> None:
        self.values = values
        self.cmp = cmp
        self.__heapify()


    @staticmethod
    def __parent(i: int):
        return (i - 1) // 2


    @staticmethod
    def __child(i: int):
        l = i * 2 + 1
        return l, l + 1


    def __pick_child(self, i: int):
        left, right = Heap.__child(i)

        if left >= len(self.values):
            return -1
        if right >= len(self.values):
            return left

        if self.cmp(self.values[left], self.values[right]) <= 0:
            return left
        return right


    @staticmethod
    def __swap(arr: list, i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]


    def __heapify(self):
        for i in range(0, len(self.values)):
            self.__shift_up(i)


    def __shift_up(self, i: int):
        if i >= len(self.values):
            return

        while i > 0:
            parent = Heap.__parent(i)

            if self.cmp(self.values[i], self.values[parent]) < 0:
                Heap.__swap(self.values, i, parent)
                i = parent
            else:
                break


    def __shift_down(self, i: int):
        while True:
            child = self.__pick_child(i)

            if child < 0:
                break
            if self.cmp(self.values[child], self.values[i]) >= 0:
                break

            Heap.__swap(self.values, i, child)
            i = child


    def pop(self):
        Heap.__swap(self.values, 0, len(self.values) - 1)
        result = self.values.pop()
        self.__shift_down(0)
        return result


    # def push(self):
    #     pass


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        values = []
        for begin, end in intervals:
            values.append((begin, 1))
            values.append((end, -1))

        heap = Heap(values, lambda a, b: a[0] - b[0] if a[0] != b[0] else a[1] - b[1])

        result = cnt = 0
        while heap.values:
            _, delta = heap.pop()
            cnt += delta
            result = max(result, cnt)

        return result
# @lc code=end

Solution().minMeetingRooms([[65,424],[351,507],[314,807],[387,722],[19,797],[259,722],[165,221],[136,897]])
