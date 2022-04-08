#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (53.28%)
# Likes:    827
# Dislikes: 0
# Total Accepted:    225.9K
# Total Submissions: 424K
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
        dummuy = ListNode(-10000)
        prev_result = dummuy

        prev = dummuy
        curr = head
        count = 2

        while curr:
            next = curr.next
            curr.next = None

            if curr.val != prev.val:
                if count == 1:
                    prev_result.next = prev
                    prev_result = prev

                count = 1
            else:
                count += 1

            prev = curr
            curr = next

        if count == 1:
            prev_result.next = prev

        return dummuy.next
# @lc code=end
