#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (63.41%)
# Likes:    867
# Dislikes: 0
# Total Accepted:    168.5K
# Total Submissions: 265.6K
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
        tail = Solution.find_middle_and_cut(head)
        tail = Solution.reverse(tail)
        return Solution.merge(head, tail)


    @staticmethod
    def find_middle_and_cut(head: ListNode):
        fast = slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        next = slow.next
        slow.next = None
        return next


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
        prev = dummy = ListNode(-1)

        while l1 and l2:
            next1, next2 = l1.next, l2.next

            prev.next = l1
            prev = prev.next
            prev.next = l2
            prev = prev.next

            l2.next = None
            l1 = next1
            l2 = next2

        prev.next = l1
        return dummy.next
# @lc code=end
