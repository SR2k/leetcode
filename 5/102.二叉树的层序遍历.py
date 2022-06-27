#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (64.78%)
# Likes:    1338
# Dislikes: 0
# Total Accepted:    580.4K
# Total Submissions: 895.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1]
# 输出：[[1]]
# 
# 
# 示例 3：
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
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000
# 
# 
#


from commons.Tree import TreeNode


# @lc code=start
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        result = []
        if not root:
            return result

        queue = deque([root])

        while queue:
            level_length = len(queue)
            level_result = []

            for _ in range(level_length):
                node = queue.popleft()
                level_result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_result)

        return result
# @lc code=end
