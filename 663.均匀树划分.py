#
# @lc app=leetcode.cn id=663 lang=python3
#
# [663] 均匀树划分
#
# https://leetcode-cn.com/problems/equal-tree-partition/description/
#
# algorithms
# Medium (46.40%)
# Likes:    39
# Dislikes: 0
# Total Accepted:    1.8K
# Total Submissions: 3.9K
# Testcase Example:  '[5,10,10,null,null,2,3]'
#
# 给定一棵有 n 个结点的二叉树，你的任务是检查是否可以通过去掉树上的一条边将树分成两棵，且这两棵树结点之和相等。
# 
# 样例 1:
# 
# 输入:     
# ⁠   5
# ⁠  / \
# ⁠ 10 10
# ⁠   /  \
# ⁠  2   3
# 
# 输出: True
# 解释: 
# ⁠   5
# ⁠  / 
# ⁠ 10
# ⁠     
# 和: 15
# 
# ⁠  10
# ⁠ /  \
# ⁠2    3
# 
# 和: 15
# 
# 
# 
# 
# 样例 2:
# 
# 输入:     
# ⁠   1
# ⁠  / \
# ⁠ 2  10
# ⁠   /  \
# ⁠  2   20
# 
# 输出: False
# 解释: 无法通过移除一条树边将这棵树划分成结点之和相等的两棵子树。
# 
# 
# 
# 
# 注释 :
# 
# 
# 树上结点的权值范围 [-100000, 100000]。
# 1 <= n <= 10000
# 
# 
# 
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


import math


# @lc code=start
class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        seen_sum = set()
        total_sum = 0

        def helper(node: TreeNode) -> int:
            if not node:
                return 0

            l, r = helper(node.left), helper(node.right)
            sub_tree_sum = sum([l, r, node.val])

            if node != root:
                seen_sum.add(sub_tree_sum)

            nonlocal total_sum
            total_sum += node.val

            return sub_tree_sum

        helper(root)
        return total_sum % 2 == 0 and total_sum // 2 in seen_sum
# @lc code=end
