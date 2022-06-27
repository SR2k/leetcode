#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (53.55%)
# Likes:    796
# Dislikes: 0
# Total Accepted:    434.2K
# Total Submissions: 810.8K
# Testcase Example:  '[1,1,2]'
#
# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,1,2]
# 输出：[1,2]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
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
        dummy = prev = ListNode(-1)

        while head:
            prev.next = head
            prev = prev.next

            val = head.val

            while head and head.val == val:
                head = head.next

            prev.next = None

        return dummy.next
# @lc code=end
