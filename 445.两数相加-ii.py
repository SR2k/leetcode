#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode.cn/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (59.66%)
# Likes:    523
# Dislikes: 0
# Total Accepted:    102.5K
# Total Submissions: 171.6K
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
# 0 <= node.val <= 9
# 输入数据保证链表代表的数字无前导 0
# 
# 
# 
# 
# 进阶：如果输入链表不能翻转该如何解决？
# 
#

from commons.List import ListNode

# @lc code=start
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = Solution.list_to_stack(l1), Solution.list_to_stack(l2)
        prev = None
        carry = 0

        while s1 or s2 or carry:
            v1 = s1.pop().val if s1 else 0
            v2 = s2.pop().val if s2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            node = ListNode(val % 10, prev)
            prev = node

        return prev


    @staticmethod
    def list_to_stack(l: ListNode):
        stack: list[ListNode] = []
        while l:
            stack.append(l)
            l = l.next
        return stack
# @lc code=end
