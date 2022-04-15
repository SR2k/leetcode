#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (70.72%)
# Likes:    1347
# Dislikes: 0
# Total Accepted:    419.6K
# Total Submissions: 593.2K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 
# 
# 示例 2：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100
# 
# 
#


from commons.List import ListNode


# @lc code=start
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(-1, head)
        curr = head

        while curr and curr.next:
            l1 = curr
            l2 = curr.next
            next = curr.next.next

            prev.next = l2
            l2.next = l1
            l1.next = next
            prev = l1
            curr = next

        return dummy.next
# @lc code=end
