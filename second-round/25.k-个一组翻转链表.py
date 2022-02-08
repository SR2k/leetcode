#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (65.92%)
# Likes:    1438
# Dislikes: 0
# Total Accepted:    263.4K
# Total Submissions: 399.6K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 进阶：
# 
# 
# 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1,2,3,4,5], k = 1
# 输出：[1,2,3,4,5]
# 
# 
# 示例 4：
# 
# 
# 输入：head = [1], k = 1
# 输出：[1]
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 列表中节点的数量在范围 sz 内
# 1 
# 0 
# 1 
# 
# 
#



from typing import Optional
from commons.List import ListNode



# @lc code=start
class Solution:
    def find_k(self, prev: ListNode, k: int):
        curr = prev

        while k:
            curr = curr.next
            k -= 1

            if not curr:
                return None

        return curr


    def reverse(self, prev_begin: ListNode, end: ListNode):
        begin = prev_begin.next
        post_end = end.next

        prev = prev_begin
        curr = prev_begin.next

        while curr != post_end:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        prev_begin.next = end
        begin.next = post_end
        return begin


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        prev_begin = dummy
        end = self.find_k(dummy, k)

        while end:
            prev_begin = self.reverse(prev_begin, end)
            end = self.find_k(prev_begin, k)

        return dummy.next
# @lc code=end

s = Solution()
print(s.reverseKGroup(ListNode.from_arr([1,2,3,4,5,6,7]), 1))
print(s.reverseKGroup(ListNode.from_arr([1,2,3,4,5,6,7]), 1))
print(s.reverseKGroup(ListNode.from_arr([1,2,3,4,5,6,7]), 2))
print(s.reverseKGroup(ListNode.from_arr([1]), 1))
