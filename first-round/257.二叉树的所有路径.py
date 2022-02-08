#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (68.56%)
# Likes:    615
# Dislikes: 0
# Total Accepted:    154.9K
# Total Submissions: 225.9K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
# 
# 叶子节点 是指没有子节点的节点。
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1]
# 输出：["1"]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [1, 100] 内
# -100 <= Node.val <= 100
# 
# 
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def binaryTreePaths(self, root: 'TreeNode') -> list[str]:
        routes = []
        result = []

        def helper(node: 'TreeNode'):
            routes.append(str(node.val))

            if not node.left and not node.right:
                result.append("->".join(routes))
            else:
                if node.left:
                    helper(node.left)
                if node.right:
                    helper(node.right)

            routes.pop()

        helper(root)
        return result
# @lc code=end
