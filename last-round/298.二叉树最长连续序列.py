#
# @lc app=leetcode.cn id=298 lang=python3
#
# [298] 二叉树最长连续序列
#
# https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence/description/
#
# algorithms
# Medium (57.88%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 8.1K
# Testcase Example:  '[1,null,3,2,4,null,null,null,5]'
#
# 给你一棵指定的二叉树的根节点 root ，请你计算其中 最长连续序列路径 的长度。
# 
# 最长连续序列路径 是依次递增 1 的路径。该路径，可以是从某个初始节点到树中任意节点，通过「父 -
# 子」关系连接而产生的任意路径。且必须从父节点到子节点，反过来是不可以的。
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,3,2,4,null,null,null,5]
# 输出：3
# 解释：当中，最长连续序列是 3-4-5 ，所以返回结果为 3 。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [2,null,3,2,null,1]
# 输出：2
# 解释：当中，最长连续序列是 2-3 。注意，不是 3-2-1，所以返回 2 。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [1, 3 * 10^4] 内
# -3 * 10^4 <= Node.val <= 3 * 10^4
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
    def longestConsecutive(self, root: TreeNode) -> int:
        result = 1
        def helper(node: TreeNode, curr = 1):
            nonlocal result
            result = max(result, curr)

            if not node:
                return

            if node.left:
                if node.left.val == node.val + 1:
                    helper(node.left, curr + 1)
                else:
                    helper(node.left)
            if node.right:
                if node.right.val == node.val + 1:
                    helper(node.right, curr + 1)
                else:
                    helper(node.right)

        helper(root)
        return result
# @lc code=end
