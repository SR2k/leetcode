#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#
# https://leetcode-cn.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (79.10%)
# Likes:    1249
# Dislikes: 0
# Total Accepted:    427.9K
# Total Submissions: 541K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：root = [2,1,3]
# 输出：[2,3,1]
# 
# 
# 示例 3：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目范围在 [0, 100] 内
# -100 <= Node.val <= 100
# 
# 
#


from tkinter import N
from commons.Tree import TreeNode


# @lc code=start
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def walk(node: TreeNode):
            if not node:
                return None

            node.left, node.right = node.right, node.left
            walk(node.left)
            walk(node.right)


        walk(root)
        return root
# @lc code=end
