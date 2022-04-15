#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (76.25%)
# Likes:    689
# Dislikes: 0
# Total Accepted:    113.3K
# Total Submissions: 148.7K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为高度平衡的二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差不超过 1。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入: head = [-10,-3,0,5,9]
# 输出: [0,-3,9,-10,null,5]
# 解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
# 
# 
# 示例 2:
# 
# 
# 输入: head = []
# 输出: []
# 
# 
# 
# 
# 提示:
# 
# 
# head 中的节点数在[0, 2 * 10^4] 范围内
# -10^5 <= Node.val <= 10^5
# 
# 
#

from typing import Optional
from commons.Tree import TreeNode
from commons.List import ListNode


# @lc code=start
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next


        def helper(left: int, right: int):
            if left > right:
                return None
            if left == right:
                return TreeNode(values[left])
            if left + 1 == right:
                return TreeNode(values[right], TreeNode(values[left]))

            middle = (left + right) // 2
            root = TreeNode(values[middle])
            root.left = helper(left, middle - 1)
            root.right = helper(middle + 1, right)
            return root


        return helper(0, len(values) - 1)
# @lc code=end
