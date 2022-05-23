#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#
# https://leetcode.cn/problems/invert-binary-tree/description/
#
# algorithms
# Easy (79.12%)
# Likes:    1290
# Dislikes: 0
# Total Accepted:    457.4K
# Total Submissions: 577.9K
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


from commons.Tree import TreeNode


# @lc code=start
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
# @lc code=end

