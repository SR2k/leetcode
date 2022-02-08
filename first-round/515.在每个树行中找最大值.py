#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#
# https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (64.32%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    36.6K
# Total Submissions: 56.9K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。
# 
# 
# 
# 示例1：
# 
# 
# 输入: root = [1,3,2,5,3,null,9]
# 输出: [1,3,9]
# 解释:
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# 
# 示例2：
# 
# 
# 输入: root = [1,2,3]
# 输出: [1,3]
# 解释:
# ⁠         1
# ⁠        / \
# ⁠       2   3
# 
# 
# 示例3：
# 
# 
# 输入: root = [1]
# 输出: [1]
# 
# 
# 示例4：
# 
# 
# 输入: root = [1,null,2]
# 输出: [1,2]
# 解释:      
# 1 
# \
# 2     
# 
# 
# 示例5：
# 
# 
# 输入: root = []
# 输出: []
# 
# 
# 
# 
# 提示：
# 
# 
# 二叉树的节点个数的范围是 [0,10^4]
# -2^31 
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
from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_length = len(queue)
            level_result = float('-inf')

            for _ in range(level_length):
                node = queue.popleft()
                level_result = max(level_result, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_result)

        return result
# @lc code=end

