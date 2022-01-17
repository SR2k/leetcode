#
# @lc app=leetcode.cn id=1110 lang=python3
#
# [1110] 删点成林
#
# https://leetcode-cn.com/problems/delete-nodes-and-return-forest/description/
#
# algorithms
# Medium (62.82%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 17.2K
# Testcase Example:  '[1,2,3,4,5,6,7]\n[3,5]'
#
# 给出二叉树的根节点 root，树上每个节点都有一个不同的值。
# 
# 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
# 
# 返回森林中的每棵树。你可以按任意顺序组织答案。
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
# 输出：[[1,2,null,4],[6],[7]]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数最大为 1000。
# 每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
# to_delete.length <= 1000
# to_delete 包含一些从 1 到 1000、各不相同的值。
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
    def get_parent_map(self, root: TreeNode):
        parents: dict[int, TreeNode] = {}
        nodes: dict[int, TreeNode] = {}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            nodes[node.val] = node

            if node.left:
                parents[node.left.val] = node
                queue.append(node.left)
            if node.right:
                parents[node.right.val] = node
                queue.append(node.right)

        return parents, nodes


    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        parents, nodes = self.get_parent_map(root)
        result = set([root])

        for val in to_delete:
            node = nodes[val]

            if node in result:
                result.remove(node)
            elif val in parents:
                parent = parents.get(val)
                if parent.left and parent.left == node:
                    parent.left = None
                if parent.right and parent.right == node:
                    parent.right = None

            if node and node.left:
                result.add(node.left)
            if node and node.right:
                result.add(node.right)

        return list(result)

# @lc code=end
