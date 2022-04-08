#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#
# https://leetcode-cn.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (72.59%)
# Likes:    420
# Dislikes: 0
# Total Accepted:    57.9K
# Total Submissions: 79.8K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# 给你一个嵌套的整数列表 nestedList
# 。每个元素要么是一个整数，要么是一个列表；该列表的元素也可能是整数或者是其他列表。请你实现一个迭代器将其扁平化，使之能够遍历这个列表中的所有整数。
# 
# 实现扁平迭代器类 NestedIterator ：
# 
# 
# NestedIterator(List<NestedInteger> nestedList) 用嵌套列表 nestedList 初始化迭代器。
# int next() 返回嵌套列表的下一个整数。
# boolean hasNext() 如果仍然存在待迭代的整数，返回 true ；否则，返回 false 。
# 
# 
# 你的代码将会用下述伪代码检测：
# 
# 
# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
# ⁠   append iterator.next() to the end of res
# return res
# 
# 如果 res 与预期的扁平化列表匹配，那么你的代码将会被判为正确。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nestedList = [[1,1],2,[1,1]]
# 输出：[1,1,2,1,1]
# 解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
# 
# 示例 2：
# 
# 
# 输入：nestedList = [1,[4,[6]]]
# 输出：[1,4,6]
# 解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nestedList.length <= 500
# 嵌套列表中的整数值在范围 [-10^6, 10^6] 内
# 
# 
#

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
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
class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.stack = list(nestedList)
        self.stack.reverse()


    def _normalize(self):
        while self.stack and not self.stack[-1].isInteger():
            nested = self.stack.pop().getList()

            while nested:
                self.stack.append(nested.pop())


    def next(self) -> int:
        self._normalize()
        return self.stack.pop().getInteger()


    def hasNext(self) -> bool:
        self._normalize()
        return self.stack

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

