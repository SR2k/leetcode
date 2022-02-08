#
# @lc app=leetcode.cn id=1669 lang=python3
#
# [1669] 合并两个链表
#
# https://leetcode-cn.com/problems/merge-in-between-linked-lists/description/
#
# algorithms
# Medium (76.67%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 14.1K
# Testcase Example:  '[0,1,2,3,4,5]\n3\n4\n[1000000,1000001,1000002]'
#
# 给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。
# 
# 请你将 list1 中第 a 个节点到第 b 个节点删除，并将list2 接在被删除节点的位置。
# 
# 下图中蓝色边和节点展示了操作后的结果：
# 
# 请你返回结果链表的头指针。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# 输出：[0,1,2,1000000,1000001,1000002,5]
# 解释：我们删除 list1 中第三和第四个节点，并将 list2 接在该位置。上图中蓝色的边和节点为答案链表。
# 
# 
# 示例 2：
# 
# 
# 输入：list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 =
# [1000000,1000001,1000002,1000003,1000004]
# 输出：[0,1,1000000,1000001,1000002,1000003,1000004,6]
# 解释：上图中蓝色的边和节点为答案链表。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 
# 1 
# 1 
# 
# 
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

# @lc code=start
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(-1, list1)
        prev, curr, n = dummy, list1, 0

        while n < a:
            prev = curr
            curr = curr.next
            n += 1

        prev.next = list2

        list_2_end = list2
        while list_2_end.next:
            list_2_end = list_2_end.next

        while n < b:
            prev = curr
            curr = curr.next
            n += 1

        list_2_end.next = curr.next

        return dummy.next
# @lc code=end

