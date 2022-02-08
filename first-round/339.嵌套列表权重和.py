#
# @lc app=leetcode.cn id=339 lang=python3
#
# [339] 嵌套列表权重和
#
# https://leetcode-cn.com/problems/nested-list-weight-sum/description/
#
# algorithms
# Medium (80.56%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 4.2K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# 给定一个嵌套的整数列表 nestedList ，每个元素要么是整数，要么是列表。同时，列表中元素同样也可以是整数或者是另一个列表。
# 
# 整数的 深度 是其在列表内部的嵌套层数。例如，嵌套列表 [1,[2,2],[[3],2],1] 中每个整数的值就是其深度。
# 
# 请返回该列表按深度加权后所有整数的总和。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：nestedList = [[1,1],2,[1,1]]
# 输出：10 
# 解释：因为列表中有四个深度为 2 的 1 ，和一个深度为 1 的 2。
# 
# 示例 2：
# 
# 
# 输入：nestedList = [1,[4,[6]]]
# 输出：27 
# 解释：一个深度为 1 的 1，一个深度为 2 的 4，一个深度为 3 的 6。所以，1 + 4*2 + 6*3 = 27。
# 
# 示例 3：
# 
# 
# 输入：nestedList = [0]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 嵌套列表中整数的值在范围 [-100, 100] 内
# 任何整数的最大 深度 都小于或等于 50
# 
# 
#

class NestedInteger:
    """
    This is the interface that allows for creating nested lists.
    You should not implement it, or speculate about its implementation
    """

    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        """
        pass

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> list['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


# @lc code=start
from collections import deque


class Solution:
    def depthSum(self, nestedList: list[NestedInteger]) -> int:
        # 对于权重，正着反着是没区别的，所以不用 reverse
        stack: deque[tuple[NestedInteger, int]] = deque((n, 1) for n in nestedList)
        ret = 0

        while stack:
            curr, depth = stack.pop()
            if curr.isInteger():
                ret += curr.getInteger() * depth
            else:
                for n in curr.getList():
                    stack.append((n, depth + 1))

        return ret
# @lc code=end
