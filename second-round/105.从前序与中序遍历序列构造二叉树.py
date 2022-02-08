#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (70.72%)
# Likes:    1385
# Dislikes: 0
# Total Accepted:    288.1K
# Total Submissions: 407.3K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。
# 
# 
# 
# 示例 1:
# 
# 
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 
# 
# 示例 2:
# 
# 
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 
# inorder.length == preorder.length
# -3000 
# preorder 和 inorder 均无重复元素
# inorder 均出现在 preorder
# preorder 保证为二叉树的前序遍历序列
# inorder 保证为二叉树的中序遍历序列
# 
# 
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left:'TreeNode'=None, right:'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        # print(s.buildTree([1,2,3],[2,3,1]))

        def helper(a: int, b: int, c: int, d: int) -> TreeNode:
            if a > b:
                return None

            root_val = preorder[a] # 3
            root_node = TreeNode(root_val)

            if a == b:
                return root_node

            root_inorder_index= inorder.index(root_val) # 1

            left_inorder_begin = c # 0
            left_inorder_end = root_inorder_index - 1 # 0
            right_inorder_begin = root_inorder_index + 1 # 2
            right_inorder_end = d # 4

            left_length = left_inorder_end - left_inorder_begin + 1 # 1
            # right_length = right_inorder_end - right_inorder_begin + 1

            left_preorder_begin = a + 1 # 1
            left_preorder_end = left_preorder_begin + left_length - 1
            right_preorder_begin = left_preorder_end + 1
            right_preorder_end = b

            root_node.left = helper(left_preorder_begin, left_preorder_end, left_inorder_begin, left_inorder_end)
            root_node.right = helper(right_preorder_begin, right_preorder_end, right_inorder_begin, right_inorder_end)

            return root_node

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
# @lc code=end

s = Solution()
# print(s.buildTree([1,2,3],[3,2,1]))
print(s.buildTree([1,2,3],[2,3,1]))
