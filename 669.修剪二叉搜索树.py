#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#
# https://leetcode-cn.com/problems/trim-a-binary-search-tree/description/
#
# algorithms
# Medium (66.63%)
# Likes:    422
# Dislikes: 0
# Total Accepted:    34.8K
# Total Submissions: 52.3K
# Testcase Example:  '[1,0,2]\n1\n2'
#
# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low,
# high]中。修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。
# 
# 所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,0,2], low = 1, high = 2
# 输出：[1,null,2]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# 输出：[3,2,null,1]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1], low = 1, high = 2
# 输出：[1]
# 
# 
# 示例 4：
# 
# 
# 输入：root = [1,null,2], low = 1, high = 3
# 输出：[1,null,2]
# 
# 
# 示例 5：
# 
# 
# 输入：root = [1,null,2], low = 2, high = 4
# 输出：[2]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数在范围 [1, 10^4] 内
# 0 
# 树中每个节点的值都是唯一的
# 题目数据保证输入是一棵有效的二叉搜索树
# 0 
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
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(node: TreeNode):
            if not node:
                return node

            if node.val > high:
                return trim(node.left) 
            if node.val < low:
                return trim(node.right)

            node.left = trim(node.left)
            node.right = trim(node.right)
            return node

        return trim(root)
# @lc code=end
