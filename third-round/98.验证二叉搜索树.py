#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (35.59%)
# Likes:    1457
# Dislikes: 0
# Total Accepted:    449.5K
# Total Submissions: 1.3M
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


# @lc code=start
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = -float('inf')
        curr = root
        stack = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if curr.val <= prev:
                return False
            prev = curr.val

            curr = curr.right

        return True
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def helper(node: TreeNode, min_val: int, max_val: int) -> bool:
#             if not node:
#                 return True

#             if not min_val < node.val < max_val:
#                 return False

#             next_min, next_max = max(node.val, min_val), min(node.val, max_val)
#             return helper(node.left, min_val, next_max) and helper(node.right, next_min, max_val)

#         return helper(root, -float('inf'), float('inf'))
# @lc code=end
