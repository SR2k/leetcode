#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#
# https://leetcode-cn.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (80.96%)
# Likes:    304
# Dislikes: 0
# Total Accepted:    50.5K
# Total Submissions: 62.3K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：
# 
# 
# 二叉树的根是数组 nums 中的最大元素。
# 左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
# 右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
# 
# 
# 返回有给定数组 nums 构建的 最大二叉树 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,2,1,6,0,5]
# 输出：[6,3,5,null,2,0,null,null,1]
# 解释：递归调用如下所示：
# - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
# ⁠   - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
# ⁠       - 空数组，无子节点。
# ⁠       - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
# ⁠           - 空数组，无子节点。
# ⁠           - 只有一个元素，所以子节点是一个值为 1 的节点。
# ⁠   - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
# ⁠       - 只有一个元素，所以子节点是一个值为 0 的节点。
# ⁠       - 空数组，无子节点。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,2,1]
# 输出：[3,null,2,null,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# nums 中的所有整数 互不相同
# 
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        sorted_nums = sorted(nums)
        pos = {}
        for i, n in enumerate(nums):
            pos[n] = i

        root = TreeNode(sorted_nums.pop())
        while sorted_nums:
            node = TreeNode(sorted_nums.pop())
            parent = root
            while True:
                if pos[node.val] > pos[parent.val]:
                    if not parent.right:
                        parent.right = node
                        break
                    else:
                        parent = parent.right
                else:
                    if not parent.left:
                        parent.left = node
                        break
                    else:
                        parent = parent.left

        return root
# @lc code=end

