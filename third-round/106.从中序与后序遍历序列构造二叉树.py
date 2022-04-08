#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (72.31%)
# Likes:    685
# Dislikes: 0
# Total Accepted:    167.8K
# Total Submissions: 232.2K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder
# 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
# 
# 
# 示例 2:
# 
# 
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder 和 postorder 都由 不同 的值组成
# postorder 中每一个值都在 inorder 中
# inorder 保证是树的中序遍历
# postorder 保证是树的后序遍历
# 
# 
#


from typing import List, Optional
from commons.Tree import TreeNode


# @lc code=start
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_begin: int, in_end: int, post_begin: int, post_end: int) -> Optional[TreeNode]:
            if in_begin > in_end:
                return None

            if in_begin == in_end:
                return TreeNode(inorder[in_begin])

            root_post_index = post_end
            root_val = postorder[root_post_index]
            root_in_index = inorder.index(root_val)
            root = TreeNode(root_val)

            left_in_begin = in_begin
            left_in_end = root_in_index - 1
            right_in_begin = root_in_index + 1
            right_in_end = in_end

            left_length = left_in_end - left_in_begin + 1
            # right_length = right_in_end - right_in_begin + 1

            left_post_begin = post_begin
            left_post_end = post_begin + left_length - 1
            right_post_begin = left_post_end + 1
            right_post_end = root_post_index - 1

            root.left = helper(left_in_begin, left_in_end, left_post_begin, left_post_end)
            root.right = helper(right_in_begin, right_in_end, right_post_begin, right_post_end)
            return root

        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)
# @lc code=end

# [9,3,15,20,7]
# [9,15,7,20,3]
