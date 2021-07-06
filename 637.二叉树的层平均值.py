#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#
# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (68.84%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    66.2K
# Total Submissions: 96.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
# 
# 
# 
# 示例 1：
# 
# 输入：
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 输出：[3, 14.5, 11]
# 解释：
# 第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 节点值的范围在32位有符号整数范围内。
# 
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        ret = []
        if not root:
            return ret

        queue = deque([root])
        while queue:
            level_length = len(queue)
            level_ret = []

            for _ in range(level_length):
                curr = queue.popleft()
                level_ret.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            ret.append(sum(level_ret) / level_length)

        return ret
# @lc code=end

