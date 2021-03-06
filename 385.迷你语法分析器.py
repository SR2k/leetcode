#
# @lc app=leetcode.cn id=385 lang=python3
#
# [385] 迷你语法分析器
#
# https://leetcode-cn.com/problems/mini-parser/description/
#
# algorithms
# Medium (41.37%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    6.8K
# Total Submissions: 16.5K
# Testcase Example:  '"324"'
#
# 给定一个用字符串表示的整数的嵌套列表，实现一个解析它的语法分析器。
# 
# 列表中的每个元素只可能是整数或整数嵌套列表
# 
# 提示：你可以假定这些字符串都是格式良好的：
# 
# 
# 字符串非空
# 字符串不包含空格
# 字符串只包含数字0-9、[、-、,、]
# 
# 
# 
# 
# 示例 1：
# 
# 给定 s = "324",
# 
# 你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
# 
# 
# 示例 2：
# 
# 给定 s = "[123,[456,[789]]]",
# 
# 返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
# 
# 1. 一个 integer 包含值 123
# 2. 一个包含两个元素的嵌套列表：
# ⁠   i.  一个 integer 包含值 456
# ⁠   ii. 一个包含一个元素的嵌套列表
# ⁠        a. 一个 integer 包含值 789
# 
# 
#


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
   def __init__(self, value = None):
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
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        buffer = ''
        root = None
        stack: list[NestedInteger] = []

        if not s:
            return NestedInteger()
        if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):
            return NestedInteger(int(s))

        for char in s:
            if char == '[':
                curr = NestedInteger()
                stack.append(curr)
                if not root:
                    root = curr
                else:
                    stack[-2].add(curr)
            elif char == ']':
                if buffer:
                    stack[-1].add(NestedInteger(int(buffer)))
                    buffer = ''
                stack.pop()
            elif char == ',':
                if buffer:
                    stack[-1].add(NestedInteger(int(buffer)))
                buffer = ''
            else:
                buffer += char

        return root
# @lc code=end


print(Solution().deserialize("-3"))

