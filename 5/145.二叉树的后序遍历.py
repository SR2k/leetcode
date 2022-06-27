#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (75.77%)
# Likes:    837
# Dislikes: 0
# Total Accepted:    435.2K
# Total Submissions: 574.2K
# Testcase Example:  '[1,null,2,3]'
#
# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 输出：[3,2,1]
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
# 树中节点的数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
# 
# 
# 
# 
# 进阶：递归算法很简单，你可以通过迭代算法完成吗？
# 
#


from commons.Tree import TreeNode
from typing import Optional, List


# @lc code=start
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        curr = root
        stack = []
        while curr or stack:
            while curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.right

            curr = stack.pop().left

        result.reverse()
        return result
# @lc code=end

