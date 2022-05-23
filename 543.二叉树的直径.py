#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode.cn/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (56.89%)
# Likes:    1037
# Dislikes: 0
# Total Accepted:    217.9K
# Total Submissions: 382.7K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
# 
# 
# 
# 示例 :
# 给定二叉树
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
# 
# 
# 
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
# 
#


from commons.Tree import TreeNode
from typing import Optional


# @lc code=start
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def helper(node: Optional[TreeNode]):
            if not node:
                return 0

            left, right = helper(node.left), helper(node.right)

            nonlocal result
            result = max(result, left + right)
            return max(left, right) + 1

        helper(root)
        return result
# @lc code=end
