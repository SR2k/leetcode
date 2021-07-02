#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (68.03%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    13.1K
# Total Submissions: 19.3K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# 返回与给定的前序和后序遍历匹配的任何二叉树。
# 
# pre 和 post 遍历中的值是不同的正整数。
# 
# 
# 
# 示例：
# 
# 输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= pre.length == post.length <= 30
# pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
# 每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。
# 
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
class Solution:
    def constructFromPrePost(self, pre: list[int], post: list[int]) -> TreeNode:
        def helper(pre_l: int, pre_r: int, post_l: int, post_r: int) -> TreeNode:
            if pre_r - pre_l < 0:
                return None
            if pre_r - pre_l == 0:
                return TreeNode(pre[pre_l])
            if pre_r - pre_l == 1:
                left = TreeNode(post[post_l])
                return TreeNode(pre[pre_l], left)

            root_val = pre[pre_l]
            root = TreeNode(root_val)

            left_val = pre[pre_l + 1]
            right_val = post[post_r - 1]

            if left_val == right_val:
                root.left = helper(pre_l + 1, pre_r, post_l, post_r - 1)
            else:
                right_root_pre_idx = pre.index(right_val)
                left_root_post_idx = post.index(left_val)
                root.left = helper(pre_l + 1, right_root_pre_idx - 1, post_l, left_root_post_idx)
                root.right = helper(right_root_pre_idx, pre_r, left_root_post_idx + 1, post_r - 1)
            return root

        return helper(0, len(pre) - 1, 0, len(post) - 1)
# @lc code=end

