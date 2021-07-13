#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#
# https://leetcode-cn.com/problems/univalued-binary-tree/description/
#
# algorithms
# Easy (68.26%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    30.5K
# Total Submissions: 44.7K
# Testcase Example:  '[1,1,1,1,1,null,1]'
#
# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
# 
# 只有给定的树是单值二叉树时，才返回 true；否则返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[1,1,1,1,1,null,1]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 
# 输入：[2,2,2,5,2]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 给定树的节点数范围是 [1, 100]。
# 每个节点的值都是整数，范围为 [0, 99] 。
# 
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
from collections import deque


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        p, q = root.val, deque([root])

        while q:
            curr = q.popleft()

            if curr.val != p:
                return False

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return True
# @lc code=end

