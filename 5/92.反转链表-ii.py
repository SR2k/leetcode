#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (55.28%)
# Likes:    1232
# Dislikes: 0
# Total Accepted:    279.4K
# Total Submissions: 505.3K
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


from commons.List import ListNode


# @lc code=start
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        # make dummy
        dummy = ListNode(-1, head)

        # find head and save prev tail
        curr = dummy
        for _ in range(left - 1):
            curr = curr.next
        prev_tail = curr
        begin = curr.next
        prev_tail.next = None

        # reverse until right
        prev = None
        curr = begin
        for _ in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        prev_tail.next = prev
        begin.next = curr

        return dummy.next
# @lc code=end
