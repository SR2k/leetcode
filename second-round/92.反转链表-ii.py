#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (55.02%)
# Likes:    1133
# Dislikes: 0
# Total Accepted:    242.2K
# Total Submissions: 440K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回
# 反转后的链表 。
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数目为 n
# 1 
# -500 
# 1 
# 
# 
# 
# 
# 进阶： 你可以使用一趟扫描完成反转吗？
# 
#


# Definition for singly-linked list.
class ListNode:
    @staticmethod
    def from_arr(l: list[int]):
        dummy = ListNode(-1)
        curr = dummy

        for n in l:
            curr.next = ListNode(n)
            curr = curr.next

        return dummy.next


    def __init__(self, val=0, next:'ListNode'=None):
        self.val = val
        self.next = next


    def __str__(self) -> str:
        result = []
        curr = self

        while curr:
            result.append(curr.val)
            curr = curr.next

        return ",".join(str(x) for x in result)


# @lc code=start
# class Solution:
#     def reverse(self, begin: ListNode, end: ListNode):
#         prev = None
#         curr = begin

#         while True: # todo
#             next = curr.next
#             curr.next = prev

#             if curr == end:
#                 break

#             prev = curr
#             curr = next

#     def find_n(self, dummy: ListNode, n: int) -> tuple[ListNode, ListNode, ListNode]:
#         prev = dummy
#         curr = dummy.next
#         while n > 1:
#             prev = curr
#             curr = curr.next
#             n -= 1
#         return prev, curr, curr.next


#     def reverseBetween(self, head: ListNode, l: int, r: int) -> ListNode:
#         dummy = ListNode(-1, head)
#         prev, left, _ = self.find_n(dummy, l)
#         _, right, next = self.find_n(dummy, r)

#         self.reverse(left, right)

#         left, right = right, left

#         prev.next = left
#         right.next = next

#         return dummy.next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(-1, head)
        prev = dummy
        curr = dummy.next
        n = 0

        prev_begin, post_end = None, None
        begin, end = None, None

        while n < right:
            n += 1
            next = curr.next

            if n == left:
                prev_begin = prev
                begin = curr
            if n == right:
                post_end = next
                end = curr

            if n > left:
                curr.next = prev

            prev = curr
            curr = next

        prev_begin.next = end
        begin.next = post_end

        return dummy.next
# @lc code=end

s = Solution()
print(s.reverseBetween(ListNode.from_arr([1,2,3,4,5]), 2, 4))
print(s.reverseBetween(ListNode.from_arr([1,2,3,4,5]), 1, 5))
print(s.reverseBetween(ListNode.from_arr([1,2,3,4,5]), 3, 5))
print(s.reverseBetween(ListNode.from_arr([1]), 1, 1))
