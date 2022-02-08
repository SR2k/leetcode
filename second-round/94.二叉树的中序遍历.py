#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (75.55%)
# Likes:    1237
# Dislikes: 0
# Total Accepted:    658.2K
# Total Submissions: 870.7K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：[1]
# 
# 
# 示例 4：
# 
# 
# 输入：root = [1,2]
# 输出：[2,1]
# 
# 
# 示例 5：
# 
# 
# 输入：root = [1,null,2]
# 输出：[1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [0, 100] 内
# -100 
# 
# 
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#


from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result
# @lc code=end

t = TreeNode(
    1,
    TreeNode(
        2,
        TreeNode(4),
        TreeNode(
            5,
            TreeNode(8),
            TreeNode(9),
        )
    ),
    TreeNode(
        3,
        None,
        TreeNode(7),
    )
)

print(Solution().inorderTraversal(t))
