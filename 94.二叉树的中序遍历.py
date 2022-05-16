#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (75.84%)
# Likes:    1424
# Dislikes: 0
# Total Accepted:    814.8K
# Total Submissions: 1.1M
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
# 
# 
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#


from commons.Tree import TreeNode
from typing import Optional, List


# @lc code=start
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result
# @lc code=end
