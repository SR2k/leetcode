#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (62.74%)
# Likes:    764
# Dislikes: 0
# Total Accepted:    146.1K
# Total Submissions: 232.9K
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
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next


        l1, l2 = head, prev

        while l1 and l2:
            l1_next, l2_next = l1.next, l2.next
            l1.next = l2
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next

        return head
# @lc code=end

s = Solution()
# print(s.reorderList(ListNode.from_arr([])))
print(s.reorderList(ListNode.from_arr([1])))
print(s.reorderList(ListNode.from_arr([1,2])))
print(s.reorderList(ListNode.from_arr([1,2,3])))
print(s.reorderList(ListNode.from_arr([1,2,3,4])))
print(s.reorderList(ListNode.from_arr([1,2,3,4,5])))
print(s.reorderList(ListNode.from_arr([1,2,3,4,5,6])))
print(s.reorderList(ListNode.from_arr([1,2,3,4,5,6,7])))
print(s.reorderList(ListNode.from_arr([1,2,3,4,5,6,7,8])))
