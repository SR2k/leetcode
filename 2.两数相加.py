#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode.cn/problems/add-two-numbers/description/
#
# algorithms
# Medium (41.74%)
# Likes:    8143
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 3.2M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
# 
# 
# 示例 2：
# 
# 
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 
# 
# 示例 3：
# 
# 
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 每个链表中的节点数在范围 [1, 100] 内
# 0 
# 题目数据保证列表表示的数字不含前导零
# 
# 
#


from typing import Optional
from commons.List import ListNode


# @lc code=start
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            prev.next = ListNode(val % 10)
            prev = prev.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
# @lc code=end
