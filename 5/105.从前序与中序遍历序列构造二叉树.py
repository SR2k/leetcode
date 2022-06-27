#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (71.08%)
# Likes:    1624
# Dislikes: 0
# Total Accepted:    367.1K
# Total Submissions: 516.4K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder
# 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
# 
# 
# 示例 2:
# 
# 
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder 和 inorder 均 无重复 元素
# inorder 均出现在 preorder
# preorder 保证 为二叉树的前序遍历序列
# inorder 保证 为二叉树的中序遍历序列
# 
# 
#


from commons.Tree import TreeNode


# @lc code=start
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        in_index = {}
        for i, n in enumerate(inorder):
            in_index[n] = i

        def build(pre_begin: int, pre_end: int, in_begin: int, in_end: int) -> TreeNode:
            if pre_begin > pre_end:
                return None
            if pre_begin == pre_end:
                return TreeNode(preorder[pre_begin])


            root_val = preorder[pre_begin]
            root_node = TreeNode(root_val)

            root_in = in_index[root_val]

            left_in_begin = in_begin
            left_in_end = root_in - 1
            right_in_begin = root_in + 1
            right_in_end = in_end

            left_len = left_in_end - left_in_begin + 1

            left_pre_begin = pre_begin + 1
            left_pre_end = left_pre_begin + left_len - 1
            right_pre_begin = left_pre_end + 1
            right_pre_end = pre_end

            root_node.left = build(left_pre_begin, left_pre_end, left_in_begin, left_in_end)
            root_node.right = build(right_pre_begin, right_pre_end, right_in_begin, right_in_end)

            return root_node

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
# @lc code=end

# [3,9,20,15,7]
# [9,3,15,20,7]

# 1 // 0 4 0 4
