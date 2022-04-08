#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#
# https://leetcode-cn.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (65.47%)
# Likes:    544
# Dislikes: 0
# Total Accepted:    147K
# Total Submissions: 224.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。
# 
# 第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。
# 
# 请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。
# 
# 你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入: head = [1,2,3,4,5]
# 输出: [1,3,5,2,4]
# 
# 示例 2:
# 
# 
# 
# 
# 输入: head = [2,1,3,5,6,4,7]
# 输出: [2,3,6,7,1,5,4]
# 
# 
# 
# 提示:
# 
# 
# n ==  链表中的节点数
# 0 <= n <= 10^4
# -10^6 <= Node.val <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def oddEvenList(self, head: "ListNode") -> "ListNode":
        if not head:
            return head

        dummy_odd = prev_odd = ListNode(-1)
        dummy_even = prev_even = ListNode(-1)

        curr = 1
        while head:
            next = head.next
            head.next = None

            if curr:
                prev_odd.next = head
                prev_odd = prev_odd.next
            else:
                prev_even.next = head
                prev_even = prev_even.next

            head = next
            curr = 1 - curr

        prev_odd.next = dummy_even.next
        return dummy_odd.next
# @lc code=end
