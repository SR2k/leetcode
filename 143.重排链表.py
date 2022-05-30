#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode.cn/problems/reorder-list/description/
#
# algorithms
# Medium (63.66%)
# Likes:    918
# Dislikes: 0
# Total Accepted:    180.8K
# Total Submissions: 283.7K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
# 
# 
# L0 → L1 → … → Ln - 1 → Ln
# 
# 
# 请将其重新排列后变为：
# 
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
# 
# 示例 2：
# 
# 
# 
# 
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]
# 
# 
# 
# 提示：
# 
# 
# 链表的长度范围为 [1, 5 * 10^4]
# 1 <= node.val <= 1000
# 
# 
#


from commons.List import ListNode


# @lc code=start
class Solution:
    def reorderList(self, head: ListNode) -> None:
        pass


    @staticmethod
    def find_and_cut_middle(head: ListNode):
        fast = slow = ListNode(-1, head)

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow.next


    @staticmethod
    def reverse(head: ListNode):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


    @staticmethod
    def merge(l1: ListNode, l2: ListNode):
        dum,m
        while l1 and l2:
# @lc code=end
