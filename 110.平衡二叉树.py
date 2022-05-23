#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode.cn/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (56.97%)
# Likes:    1011
# Dislikes: 0
# Total Accepted:    358.6K
# Total Submissions: 629K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：root = []
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数在范围 [0, 5000] 内
# -10^4 
# 
# 
#


from commons.Tree import TreeNode


# @lc code=start
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node: TreeNode):
            if not node:
                return True, 0

            l, r = helper(node.left), helper(node.right)
            return l[0] and r[0] and abs(l[1] - r[1]) <= 1, max(l[1], r[1]) + 1


        return helper(root)[0]
# @lc code=end
