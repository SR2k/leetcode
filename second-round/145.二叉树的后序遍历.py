      #
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (75.30%)
# Likes:    740
# Dislikes: 0
# Total Accepted:    351.7K
# Total Submissions: 467.1K
# Testcase Example:  '[1,null,2,3]'
#
# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 输出：[3,2,1]
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
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
# 
# 
# 
# 
# 进阶：递归算法很简单，你可以通过迭代算法完成吗？
# 
#


from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = deque()
        stack = []
        curr = root

        while stack or curr:
            while curr:
                result.appendleft(curr.val)
                stack.append(curr)
                curr = curr.right

            curr = stack.pop().left

        return list(result)
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

print(Solution().postorderTraversal(t))
