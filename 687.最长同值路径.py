#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#
# https://leetcode-cn.com/problems/longest-univalue-path/description/
#
# algorithms
# Medium (43.54%)
# Likes:    472
# Dislikes: 0
# Total Accepted:    34.1K
# Total Submissions: 78.2K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
# 
# 注意：两个节点之间的路径长度由它们之间的边数表示。
# 
# 示例 1:
# 
# 输入:
# 
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# 输出:
# 
# 
# 2
# 
# 
# 示例 2:
# 
# 输入:
# 
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# 输出:
# 
# 
# 2
# 
# 
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        ret = [0]

        def helper(root: TreeNode) -> tuple[int, int]:
            if not root:
                return 1001, 0
            left, right = helper(root.left), helper(root.right)

            curr, max_path = 0, 1
            if left[0] == root.val:
                curr += left[1]
                max_path = max(max_path, left[1] + 1)
            if right[0] == root.val:
                curr += right[1]
                max_path = max(max_path, right[1] + 1)
            ret[0] = max(curr, ret[0])

            return root.val, max_path

        helper(root)
        return ret[0]
# @lc code=end

