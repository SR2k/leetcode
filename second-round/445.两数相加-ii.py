#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (58.88%)
# Likes:    436
# Dislikes: 0
# Total Accepted:    83.6K
# Total Submissions: 142K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 
# 
# 
# 示例1：
# 
# 
# 
# 
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
# 
# 
# 示例2：
# 
# 
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
# 
# 
# 示例3：
# 
# 
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表的长度范围为 [1, 100]
# 0 
# 输入数据保证链表代表的数字无前导 0
# 
# 
# 
# 
# 进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。
# 
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next:'ListNode'=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    @staticmethod
    def list_2_stack(l: ListNode):
        stack = []
        while l:
            stack.append(l)
            l = l.next
        return stack

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = Solution.list_2_stack(l1), Solution.list_2_stack(l2)
        extra = 0
        prev = None

        while s1 or s2 or extra:
            v1 = s1.pop().val if s1 else 0
            v2 = s2.pop().val if s2 else 0
            value = v1 + v2 + extra
            extra = value // 10
            node = ListNode(value % 10)

            node.next = prev
            prev = node

        return prev
# @lc code=end
