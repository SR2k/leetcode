#
# @lc app=leetcode.cn id=251 lang=python3
#
# [251] 展开二维向量
#
# https://leetcode-cn.com/problems/flatten-2d-vector/description/
#
# algorithms
# Medium (54.74%)
# Likes:    51
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 7.5K
# Testcase Example:  '["Vector2D","next","next","next","hasNext","hasNext","next","hasNext"]\n' +
#  '[[[[1,2],[3],[4]]],[],[],[],[],[],[],[]]'
#
# 请设计并实现一个能够展开二维向量的迭代器。该迭代器需要支持 next 和 hasNext 两种操作。
# 
# 
# 
# 示例：
# 
# 
# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);
# 
# iterator.next(); // 返回 1
# iterator.next(); // 返回 2
# iterator.next(); // 返回 3
# iterator.hasNext(); // 返回 true
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 4
# iterator.hasNext(); // 返回 false
# 
# 
# 
# 
# 注意：
# 
# 
# 请记得 重置 在 Vector2D 中声明的类变量（静态变量），因为类变量会 在多个测试用例中保持不变，影响判题准确。请 查阅 这里。
# 你可以假定 next() 的调用总是合法的，即当 next() 被调用时，二维向量总是存在至少一个后续元素。
# 
# 
# 
# 
# 进阶：尝试在代码中仅使用 C++ 提供的迭代器 或 Java 提供的迭代器。
# 
#

# @lc code=start
from collections import deque


class Vector2D:
    def __init__(self, vec: list[list[int]]):
        self.all = deque(vec)
        self.curr = deque()
        self.move()


    def move(self):
        while not self.curr and self.all:
            self.curr = deque(self.all.popleft())


    def next(self) -> int:
        result = self.curr.popleft()
        self.move()
        return result


    def hasNext(self) -> bool:
        return not not (self.curr or self.all)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
