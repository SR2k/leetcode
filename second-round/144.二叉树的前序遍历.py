#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Easy (70.45%)
# Likes:    716
# Dislikes: 0
# Total Accepted:    480.8K
# Total Submissions: 681.5K
# Testcase Example:  '[1,null,2,3]'
#
# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
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
# 输出：[1,2]
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
# 进阶：递归算法很简单，你可以通过迭代算法完成吗？
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        curr = root
        stack = []

        while stack or curr:
            while curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.left

            curr = stack.pop().right

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

print(Solution().preorderTraversal(t))
