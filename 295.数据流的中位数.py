#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (52.03%)
# Likes:    424
# Dislikes: 0
# Total Accepted:    38.4K
# Total Submissions: 73.8K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
# 
# 例如，
# 
# [2,3,4] 的中位数是 3
# 
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 
# 设计一个支持以下两种操作的数据结构：
# 
# 
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
# 
# 
# 示例：
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 进阶:
# 
# 
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
# 
# 
#

# @lc code=start

import heapq

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if self.count % 2 == 1:
            t = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -t)

    def findMedian(self) -> float:
        if self.count % 2 == 1:
            return 0.0 - self.max_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.arr = []

    # def _findFirsGreaterOrEqualThen(self, n: int) -> int:
    #     if not self.arr: return 0
    #     left, right = 0, len(self.arr) - 1

    #     while left + 1 < right:
    #         middle = math.floor((left + right) / 2)

    #         if self.arr[middle] >= n:
    #             right = middle
    #         else:
    #             left = middle

    #     if self.arr[left] >= n: return left
    #     if self.arr[right] >= n: return right
    #     return len(self.arr)

    # def addNum(self, num: int) -> None:
    #     self.arr.insert(self._findFirsGreaterOrEqualThen(num), num)

    # def findMedian(self) -> float:
    #     cnt = len(self.arr)
    #     if cnt % 2 == 0:
    #         return (self.arr[cnt // 2 - 1] + self.arr[cnt // 2]) / 2
    #     else:
    #         return 0.0 + self.arr[cnt // 2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

