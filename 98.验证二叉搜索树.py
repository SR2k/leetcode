#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode.cn/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (36.00%)
# Likes:    1569
# Dislikes: 0
# Total Accepted:    503K
# Total Submissions: 1.4M
# Testcase Example:  '[2,1,3]'
#
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
# 
# 有效 二叉搜索树定义如下：
# 
# 
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [2,1,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目范围在[1, 10^4] 内
# -2^31 <= Node.val <= 2^31 - 1
# 
# 
#


from commons.Tree import TreeNode
from typing import Optional


# @lc code=start
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(float('-inf'), float('inf'), root)]

        while stack:
            min_val, max_val, node = stack.pop()

            if not min_val < node.val < max_val:
                return False

            if node.left:
                stack.append((min_val, node.val, node.left))
            if node.right:
                stack.append((node.val, max_val, node.right))

        return True
# @lc code=end
