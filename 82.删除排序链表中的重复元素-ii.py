#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (53.31%)
# Likes:    902
# Dislikes: 0
# Total Accepted:    258.8K
# Total Submissions: 485.4K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列
# 
# 
#


from commons.List import ListNode


# @lc code=start
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(-1)

        while head:
            val = head.val

            if head.next and head.next.val == val:
                while head and head.val == val:
                    head = head.next
                continue

            prev.next = head
            prev = prev.next
            head = head.next
            prev.next = None

        return dummy.next
# @lc code=end
