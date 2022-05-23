#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode.cn/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (52.66%)
# Likes:    683
# Dislikes: 0
# Total Accepted:    83.3K
# Total Submissions: 158K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
#  '[[],[1],[2],[],[3],[]]'
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


# @lc code=start
from typing import Any, Callable


class Heap:
    def __init__(self, values: list, cmp: Callable[[Any, Any], int]) -> None:
        self.values = values
        self.cmp = cmp
        self.__heapify()


    @staticmethod
    def __parent(i):
        return (i - 1) // 2


    @staticmethod
    def __children(i):
        left = i * 2 + 1
        return left, left + 1


    def __pick_child(self, i):
        left, right = Heap.__children(i)

        if left >= len(self.values):
            return -1
        if right >= len(self.values):
            return left

        if self.cmp(self.values[left], self.values[right]) <= 0:
            return left
        return right


    def __swap(self, i: int, j: int):
        self.values[i], self.values[j] = self.values[j], self.values[i]


    def __shift_up(self, i):
        while 0 < i < len(self.values):
            parent = Heap.__parent(i)

            if self.cmp(self.values[i], self.values[parent]) < 0:
                self.__swap(i, parent)
            else:
                break
            
            i = parent


    def __shift_down(self, i: int):
        while 0 <= i < len(self.values):
            child = self.__pick_child(i)

            if not 0 <= child < len(self.values):
                break
            if self.cmp(self.values[i], self.values[child]) < 0:
                break

            self.__swap(i, child)
            i = child


    def __heapify(self):
        for i in range(len(self.values)):
            self.__shift_up(i)


    def pop(self):
        self.__swap(0, len(self.values) - 1)
        ret = self.values.pop()
        self.__shift_down(0)
        return ret


    def push(self, val: any):
        self.values.append(val)
        self.__shift_up(len(self.values) - 1)


class MedianFinder:
    def __init__(self):
        self.heap1 = Heap([], lambda a, b: a - b)
        self.heap2 = Heap([], lambda a, b: b - a)


    def addNum(self, num: int) -> None:
        if self.heap1.values and num >= self.heap1.values[0]:
            self.heap1.push(num)
            # print(f"push {num} to heap 1", self.heap1.values)
        else:
            self.heap2.push(num)
            # print(f"push {num} to heap 2", self.heap2.values)

        while len(self.heap2.values) > len(self.heap1.values):
            self.heap1.push(self.heap2.pop())

        while len(self.heap1.values) > len(self.heap2.values):
            self.heap2.push(self.heap1.pop())

        # print(self.heap1.values, self.heap2.values)


    def findMedian(self) -> float:
        if len(self.heap1.values) == len(self.heap2.values):
            return (self.heap1.values[0] + self.heap2.values[0]) / 2

        return self.heap2.values[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end


cmd = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
q = [[],[40],[],[12],[],[16],[],[14],[],[35],[],[19],[],[34],[],[35],[],[28],[],[35],[],[26],[],[6],[],[8],[],[2],[],[14],[],[25],[],[25],[],[4],[],[33],[],[18],[],[10],[],[14],[],[27],[],[3],[],[35],[],[13],[],[24],[],[27],[],[14],[],[5],[],[0],[],[38],[],[19],[],[25],[],[11],[],[14],[],[31],[],[30],[],[11],[],[31],[],[0],[]]

mf = None

for i, c in enumerate(cmd):
    if c == "MedianFinder":
        mf = MedianFinder()
    elif c == 'addNum':
        mf.addNum(q[i][0])
    else:
        print(mf.findMedian())

# 12 16 40 

# [null,null,40.0,null,26.0,null,40.0,null,15.00000,null,16.00000,null,17.50000,null,19.00000,null,26.50000,null,28.00000,null,31.00000,null,28.00000,null,27.00000,null,26.00000,null,22.50000,null,19.00000,null,22.00000,null,25.00000,null,22.00000,null,25.00000,null,22.00000,null,19.00000,null,18.50000,null,19.00000,null,18.50000,null,19.00000,null,18.50000,null,19.00000,null,21.50000,null,19.00000,null,18.50000,null,18.00000,null,18.50000,null,19.00000,null,19.00000,null,19.00000,null,18.50000,null,19.00000,null,19.00000,null,19.00000,null,19.00000,null,19.00000]
# Expected Answer
# [null,null,40.0,null,26.0,null,16.0,null,15.0,null,16.0,null,17.5,null,19.0,null,26.5,null,28.0,null,31.0,null,28.0,null,27.0,null,26.0,null,22.5,null,19.0,null,22.0,null,25.0,null,22.0,null,25.0,null,22.0,null,19.0,null,18.5,null,19.0,null,18.5,null,19.0,null,18.5,null,19.0,null,21.5,null,19.0,null,18.5,null,18.0,null,18.5,null,19.0,null,19.0,null,19.0,null,18.5,null,19.0,null,19.0,null,19.0,null,19.0,null,19.0]
