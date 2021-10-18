#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (74.16%)
# Likes:    506
# Dislikes: 0
# Total Accepted:    159.2K
# Total Submissions: 211.9K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数为 n 。
# 1 
# 0 
# 
# 
# 
# 
# 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
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
    def helper(self, node: TreeNode, k: int) -> tuple[int, int]:
        if not node:
            return None, k

        if node.left:
            result, next_k = self.helper(node.left, k)

            if result is not None:
                return result, 0
            else:
                k = next_k

        if k == 1:
            return node.val, 0

        return self.helper(node.right, k - 1)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.helper(root, k)[0]
# @lc code=end
