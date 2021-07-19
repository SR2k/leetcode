#
# @lc app=leetcode.cn id=1315 lang=python3
#
# [1315] 祖父节点值为偶数的节点和
#
# https://leetcode-cn.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
#
# algorithms
# Medium (80.96%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    12.2K
# Total Submissions: 15.1K
# Testcase Example:  '[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]'
#
# 给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：
# 
# 
# 该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
# 
# 
# 如果不存在祖父节点值为偶数的节点，那么返回 0 。
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：18
# 解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在 1 到 10^4 之间。
# 每个节点的值在 1 到 100 之间。
# 
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
from collections import deque


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ret = 0
        queue = deque([(root, root.val % 2 == 0, False)])

        while queue:
            node, l2, l1 = queue.popleft()
            left, right = node.left, node.right

            if left:
                queue.append((left, left.val % 2 == 0, l2))
            if right:
                queue.append((right, right.val % 2 == 0, l2))

            if l1:
                ret += left.val if left else 0
                ret += right.val if right else 0

        return ret
# @lc code=end
