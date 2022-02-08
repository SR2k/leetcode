#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/description/
#
# algorithms
# Medium (56.64%)
# Likes:    886
# Dislikes: 0
# Total Accepted:    83.4K
# Total Submissions: 147.2K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树，它的每个结点都存放着一个整数值。
# 
# 找出路径和等于给定数值的路径总数。
# 
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
# 
# 示例：
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# 返回 3。和等于 8 的路径有:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.ret = 0

    def helper(self, prev_prefix_sum: list[int], curr_node: TreeNode, target: int):
        if not curr_node:
            return

        prev_prefix_sum.append(prev_prefix_sum[-1] + curr_node.val)

        for i in range(len(prev_prefix_sum) - 1):
            if prev_prefix_sum[-1] - prev_prefix_sum[i] == target:
                self.ret += 1

        self.helper(prev_prefix_sum, curr_node.left, target)
        self.helper(prev_prefix_sum, curr_node.right, target)

        prev_prefix_sum.pop()

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.helper([0], root, targetSum)
        return self.ret

# @lc code=end

