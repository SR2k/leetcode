#
# @lc app=leetcode.cn id=250 lang=python3
#
# [250] 统计同值子树
#
# https://leetcode-cn.com/problems/count-univalue-subtrees/description/
#
# algorithms
# Medium (63.49%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 7.1K
# Testcase Example:  '[5,1,5,5,5,null,5]'
#
# 给定一个二叉树，统计该二叉树数值相同的子树个数。
# 
# 同值子树是指该子树的所有节点都拥有相同的数值。
# 
# 示例：
# 
# 输入: root = [5,1,5,5,5,null,5]
# 
# ⁠             5
# ⁠            / \
# ⁠           1   5
# ⁠          / \   \
# ⁠         5   5   5
# 
# 输出: 4
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
    def countUnivalSubtrees(self, root: 'TreeNode') -> int:
        result = 0

        def helper(node: 'TreeNode') -> int:
            nonlocal result

            if not node:
                return None

            l, r = helper(node.left), helper(node.right)
            if node.right and r != node.val:
                return None
            if node.left and l != node.val:
                return None

            result += 1
            return node.val

        helper(root)
        return result
# @lc code=end

