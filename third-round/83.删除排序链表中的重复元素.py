#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (53.74%)
# Likes:    738
# Dislikes: 0
# Total Accepted:    383.1K
# Total Submissions: 713.1K
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
        dummy = ListNode(-1000, head)
        prev = dummy
        curr = head

        while curr:
            next = curr.next
            curr.next = None

            if prev.val != curr.val:
                prev.next = curr
                prev = curr

            curr = next

        return dummy.next
# @lc code=end
