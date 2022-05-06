#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (76.93%)
# Likes:    1193
# Dislikes: 0
# Total Accepted:    688.1K
# Total Submissions: 894.6K
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


from typing import Optional
from commons.Tree import TreeNode


# @lc code=start
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def walk(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            return max(walk(node.left), walk(node.right)) + 1


        return walk(root)
# @lc code=end
