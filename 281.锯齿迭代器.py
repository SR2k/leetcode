#
# @lc app=leetcode.cn id=281 lang=python3
#
# [281] 锯齿迭代器
#
# https://leetcode-cn.com/problems/zigzag-iterator/description/
#
# algorithms
# Medium (75.70%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    2.4K
# Total Submissions: 3.2K
# Testcase Example:  '[1,2]\n[3,4,5,6]'
#
# 给出两个一维的向量，请你实现一个迭代器，交替返回它们中间的元素。
# 
# 示例:
# 
# 输入:
# v1 = [1,2]
# v2 = [3,4,5,6] 
# 
# 输出: [1,3,2,4,5,6]
# 
# 解析: 通过连续调用 next 函数直到 hasNext 函数返回 false，
# next 函数返回值的次序应依次为: [1,3,2,4,5,6]。
# 
# 拓展：假如给你 k 个一维向量呢？你的代码在这种情况下的扩展性又会如何呢?
# 
# 拓展声明：
# “锯齿” 顺序对于 k > 2 的情况定义可能会有些歧义。所以，假如你觉得 “锯齿” 这个表述不妥，也可以认为这是一种 “循环”。例如：
# 
# 输入:
# [1,2,3]
# [4,5,6,7]
# [8,9]
# 
# 输出: [1,4,8,2,5,9,3,6,7].
# 
# 
#

# @lc code=start
class Node:
    def __init__(self, v: list[int] = None, next: 'Node' = None) -> None:
        self.list = v
        self.next = next
        self. p = 0


class ZigzagIterator:
    def __init__(self, v1: list[int], v2: list[int]):
        vectors = list(filter(lambda x: x, [v1, v2]))

        head = Node()
        prev = head

        for v in vectors:
            prev.next = Node(v)
            prev = prev.next

        prev.next = head.next
        self.head = head.next

    def next(self) -> int:
        value = self.head.list[self.head.p]

        self.head.p += 1
        
        if self.head.p == len(self.head.list):
            self.head.list = self.head.next.list
            self.head.p = self.head.next.p
            self.head.next = self.head.next.next
        else:
            self.head = self.head.next

        return value

    def hasNext(self) -> bool:
        return self.head.next != self.head or self.head.p < len(self.head.list)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

z = ZigzagIterator([1,2], [3,4,5,6])
print(z)
while z.hasNext():
    print(z.next())
