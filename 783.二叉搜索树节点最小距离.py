#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (59.48%)
# Likes:    193
# Dislikes: 0
# Total Accepted:    66.6K
# Total Submissions: 111.9K
# Testcase Example:  '[4,2,6,1,3]'
#
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 
# 注意：本题与
# 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
# 相同
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [4,2,6,1,3]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [2, 100] 内
# 0 
# 差值是一个正数，其数值等于两值之差的绝对值
# 
# 
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
    def minDiffInBST(self, root: TreeNode) -> int:
        stack = []
        prev = None
        ret = float('inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if prev != None: ret = min(abs(root.val - prev), ret)
            prev = root.val

            root = root.right

        return ret
# @lc code=end

