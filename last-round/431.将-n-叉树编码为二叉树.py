#
# @lc app=leetcode.cn id=431 lang=python3
#
# [431] 将 N 叉树编码为二叉树
#
# https://leetcode-cn.com/problems/encode-n-ary-tree-to-binary-tree/description/
#
# algorithms
# Hard (72.20%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    823
# Total Submissions: 1.1K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 设计一个算法，可以将 N 叉树编码为二叉树，并能将该二叉树解码为原 N 叉树。一个 N 叉树是指每个节点都有不超过 N
# 个孩子节点的有根树。类似地，一个二叉树是指每个节点都有不超过 2 个孩子节点的有根树。你的编码 / 解码的算法的实现没有限制，你只需要保证一个 N
# 叉树可以编码为二叉树且该二叉树可以解码回原始 N 叉树即可。
# 
# 例如，你可以将下面的 3-叉 树以该种方式编码：
# 
# 
# 
# 
# 
# 
# 
# 注意，上面的方法仅仅是一个例子，可能可行也可能不可行。你没有必要遵循这种形式转化，你可以自己创造和实现不同的方法。
# 
# 注意：
# 
# 
# N 的范围在 [1, 1000]
# 不要使用类成员 / 全局变量 / 静态变量来存储状态。你的编码和解码算法应是无状态的。
# 
# 
#

# Definition for a Node.
class Node:
    def __init__(self, val = None, children: list['Node'] = None):
        self.val = val
        self.children = children


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: 'TreeNode' = None
        self.right: 'TreeNode' = None


# @lc code=start
from collections import deque


class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None

        queue = deque([root])
        node_2_tree_node = { root: TreeNode(root.val) }

        while queue:
            node = queue.popleft()
            tree_node = node_2_tree_node[node]

            if not node.children:
                continue

            prev = None
            for child in node.children:
                queue.append(child)

                if not child in node_2_tree_node:
                    node_2_tree_node[child] = TreeNode(child.val)

                if not prev:
                    tree_node.left = node_2_tree_node[child]
                    prev = tree_node.left
                else:
                    prev.right = node_2_tree_node[child]
                    prev = prev.right

        return node_2_tree_node[root]

	# Decodes your binary tree to an n-ary tree.
    def decode(self, tree_root: 'TreeNode') -> 'Node':
        if not tree_root:
            return None

        queue = deque([tree_root])
        parents = {}
        tree_node_2_node = { tree_root: Node(tree_root.val, []) }

        while queue:
            tree_node = queue.popleft()
            node = tree_node_2_node[tree_node]

            if tree_node.left:
                left_node = Node(tree_node.left.val, [])
                tree_node_2_node[tree_node.left] = left_node
                queue.append(tree_node.left)
                parents[left_node] = node
                node.children.append(left_node)

            if tree_node.right:
                right_node = Node(tree_node.right.val, [])
                tree_node_2_node[tree_node.right] = right_node
                queue.append(tree_node.right)
                parents[node].children.append(right_node)
                parents[right_node] = parents[node]

        return tree_node_2_node[tree_root]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
# @lc code=end

