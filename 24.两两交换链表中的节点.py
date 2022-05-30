#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode.cn/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (70.81%)
# Likes:    1395
# Dislikes: 0
# Total Accepted:    446.2K
# Total Submissions: 629.6K
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
        dummy = prev = ListNode(-1, head)

        while prev and prev.next and prev.next.next:
            a = prev.next
            b = a.next
            next = b.next

            prev.next = b
            b.next = a
            a.next = next

            prev =  a

        return dummy.next
# @lc code=end
