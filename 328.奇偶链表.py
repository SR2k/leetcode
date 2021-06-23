#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#
# https://leetcode-cn.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (65.64%)
# Likes:    434
# Dislikes: 0
# Total Accepted:    113.7K
# Total Submissions: 173.2K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
# 
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
# 
# 示例 1:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# 
# 
# 示例 2:
# 
# 输入: 2->1->3->5->6->4->7->NULL 
# 输出: 2->3->6->7->1->5->4->NULL
# 
# 说明:
# 
# 
# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
# 
# 
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

# @lc code=start
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy_1, dummy_2 = ListNode(), ListNode()
        curr = head
        prev_1, prev_2 = dummy_1, dummy_2

        while curr and curr.next:
            prev_1.next = curr
            prev_2.next = curr.next

            curr = curr.next.next
            prev_1 = prev_1.next
            prev_2 = prev_2.next

        if curr:
            prev_1.next = curr
            prev_1 = prev_1.next

        prev_1.next = dummy_2.next
        return dummy_1.next
# @lc code=end

