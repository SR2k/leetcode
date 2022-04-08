#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#
# https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (60.83%)
# Likes:    508
# Dislikes: 0
# Total Accepted:    40K
# Total Submissions: 65.8K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 k 。
# 
# 返回到目标结点 target 距离为 k 的所有结点的值的列表。 答案可以以 任何顺序 返回。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# 输出：[7,4,1]
# 解释：所求结点为与目标结点（值为 5）距离为 2 的结点，值分别为 7，4，以及 1
# 
# 
# 示例 2:
# 
# 
# 输入: root = [1], target = 1, k = 3
# 输出: []
# 
# 
# 
# 
# 提示:
# 
# 
# 节点数在 [1, 500] 范围内
# 0 <= Node.val <= 500
# Node.val 中所有值 不同
# 目标结点 target 是树上的结点。
# 0 <= k <= 1000
# 
# 
# 
# 
#


from commons.Tree import TreeNode


# @lc code=start
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        parent = {}
        self.find_node(None, root, target, parent)

        result = []
        self.find_child_n(target, None, k, result, parent)

        return result


    def find_node(self, prev: TreeNode, node: TreeNode, target: TreeNode, parent: dict):
        if not node:
            return None

        parent[node] = prev

        if node == target:
            return target
            
        self.find_node(node, node.left, target, parent)
        self.find_node(node, node.right, target, parent)


    def find_child_n(self, node: TreeNode, source: TreeNode, n: int, result: list, parent: dict):
        if not node:
            return

        if n == 0:
            result.append(node.val)
            return

        if source != node.left:
            self.find_child_n(node.left, node, n - 1, result, parent)
        if source != node.right:
            self.find_child_n(node.right, node, n - 1, result, parent)

        p = parent.get(node)
        if p and source != p:
            self.find_child_n(p, node, n - 1, result, parent)
# @lc code=end

