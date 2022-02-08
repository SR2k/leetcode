#
# @lc app=leetcode.cn id=314 lang=python3
#
# [314] 二叉树的垂直遍历
#
# https://leetcode-cn.com/problems/binary-tree-vertical-order-traversal/description/
#
# algorithms
# Medium (54.89%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树的根结点，返回其结点按 垂直方向（从上到下，逐列）遍历的结果。
# 
# 如果两个结点在同一行和列，那么顺序则为 从左到右。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[9],[3,15],[20],[7]]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [3,9,8,4,0,1,7]
# 输出：[[4],[9],[3,0,1],[8],[7]]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [3,9,8,4,0,1,7,null,null,null,2,5]
# 输出：[[4],[9,5],[3,0,1],[8,2],[7]]
# 
# 
# 示例 4：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中结点的数目在范围 [0, 100] 内
# -100 
# 
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


# @lc code=start
class Solution:
    def verticalOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
 
        traversed: dict[int, list[int]] = {}
        queue: deque[tuple[TreeNode, int]] = deque([(root, 0)])

        while queue:
            node, distance = queue.popleft()
            if distance not in traversed:
                traversed[distance] = [node.val]
            else:
                traversed[distance].append(node.val)

            if node.left:
                queue.append((node.left, distance - 1))
            if node.right:
                queue.append((node.right, distance + 1))

        keys = list(traversed.keys())
        keys.sort()
        return [traversed[k] for k in keys]
# @lc code=end
