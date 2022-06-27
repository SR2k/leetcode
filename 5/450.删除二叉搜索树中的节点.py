#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#
# https://leetcode-cn.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (50.39%)
# Likes:    701
# Dislikes: 0
# Total Accepted:    98.9K
# Total Submissions: 196.4K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key
# 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
# 
# 一般来说，删除节点可分为两个步骤：
# 
# 
# 首先找到需要删除的节点；
# 如果找到了，删除它。
# 
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入：root = [5,3,6,2,4,null,7], key = 3
# 输出：[5,4,6,2,null,null,7]
# 解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
# 另一个正确答案是 [5,2,6,null,4,null,7]。
# 
# 
# 
# 
# 示例 2:
# 
# 
# 输入: root = [5,3,6,2,4,null,7], key = 0
# 输出: [5,3,6,2,4,null,7]
# 解释: 二叉树不包含值为 0 的节点
# 
# 
# 示例 3:
# 
# 
# 输入: root = [], key = 0
# 输出: []
# 
# 
# 
# 提示:
# 
# 
# 节点数的范围 [0, 10^4].
# -10^5 <= Node.val <= 10^5
# 节点值唯一
# root 是合法的二叉搜索树
# -10^5 <= key <= 10^5
# 
# 
# 
# 
# 进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。
# 
#


from commons.Tree import TreeNode
from typing import Optional


# @lc code=start
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        if not root.left and not root.right:
            return None

        next_child = next_parent = None

        if root.right:
            next_child, next_parent = self.find_suc(root)
        elif root.left:
            next_child, next_parent = self.find_pre(root)

        root.val = next_child.val
        if next_parent.left == next_child:
            next_parent.left = self.deleteNode(next_child, next_child.val)
        else:
            next_parent.right = self.deleteNode(next_child, next_child.val)

        return root


    def find_pre(self, node: TreeNode):
        if not node or not node.left:
            return None, None

        pre = node.left
        prev = node
        while pre.right:
            prev = pre
            pre = pre.right

        return pre, prev


    def find_suc(self, node: TreeNode):
        if not node or not node.right:
            return None, None

        suc = node.right
        prev = node
        while suc.left:
            prev = suc
            suc = suc.left

        return suc, prev
# @lc code=end
