#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#
# https://leetcode-cn.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (66.71%)
# Likes:    836
# Dislikes: 0
# Total Accepted:    136.9K
# Total Submissions: 204.9K
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
# 
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random
# 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
# 
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random
# --> y 。
# 
# 返回复制链表的头节点。
# 
# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
# 
# 
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 
# 
# 你的代码 只 接受原链表的头节点 head 作为传入参数。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
# 
# 
# 示例 3：
# 
# 
# 
# 
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random 为 null 或指向链表中的节点。
# 
# 
#


# Definition for a Node.
from cgitb import reset


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# @lc code=start
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         map = {}
#         prev_copied = dummy = Node(-1)
#         curr_original = head

#         while curr_original:
#             copied_node = map.get(curr_original) or Node(curr_original.val)
#             map[curr_original] = copied_node

#             if curr_original.random:
#                 copied_random = map.get(curr_original.random) or Node(curr_original.random.val)
#                 map[curr_original.random] = copied_random
#                 copied_node.random = copied_random

#             if prev_copied:
#                 prev_copied.next = copied_node

#             prev_copied = copied_node
#             curr_original = curr_original.next

#         return dummy.next


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        while curr:
            next = curr.next
            curr.next = cloned = Node(curr.val)
            cloned.next = next
            curr = next

        curr = head
        while curr:
            copied = curr.next
            next = copied.next

            if curr.random:
                copied.random = curr.random.next

            curr = next

        result = head.next
        prev_copied = None
        curr = head
        while curr:
            copied = curr.next
            next = copied.next

            if prev_copied:
                prev_copied.next = copied
            curr.next = next

            prev_copied = copied
            curr = next

        return result
# @lc code=end
