#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (62.13%)
# Likes:    289
# Dislikes: 0
# Total Accepted:    86.5K
# Total Submissions: 139.3K
# Testcase Example:  '[4,2,6,1,3]'
#
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 
# 差值是一个正数，其数值等于两值之差的绝对值。
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
# 树中节点的数目范围是 [2, 10^4]
# 0 <= Node.val <= 10^5
#
#
#
#
# 注意：本题与 783
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
#
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: 'TreeNode'=None, right: 'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        prev, result = float('-inf'), float('inf')

        def c(n: int):
            nonlocal prev
            nonlocal result
            result = min(n - prev, result)
            prev = n

        def helper(node: TreeNode):
            if node.left:
                helper(node.left)

            c(node.val)

            if node.right:
                helper(node.right)

        helper(root)
        return result
# @lc code=end

# [236,104,701,null,227,null,911]
