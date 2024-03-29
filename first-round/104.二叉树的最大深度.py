#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (76.67%)
# Likes:    1054
# Dislikes: 0
# Total Accepted:    561.6K
# Total Submissions: 732.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
# 
#

class TreeNode:
    def __init__(self, val = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
from collections import deque


class Solution:
    def maxDepth(self, root: 'TreeNode') -> int:
        result = 0
        queue = deque([(root, 1)])

        while queue:
            node, height = queue.popleft()

            if not node:
                continue

            result = max(height, result)
            queue.append((node.left, height + 1))
            queue.append((node.right, height + 1))

        return result
# @lc code=end
