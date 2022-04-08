#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] 二叉树的完全性检验
#
# https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/description/
#
# algorithms
# Medium (54.05%)
# Likes:    179
# Dislikes: 0
# Total Accepted:    31.9K
# Total Submissions: 59K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给定一个二叉树的 root ，确定它是否是一个 完全二叉树 。
# 
# 在一个 完全二叉树 中，除了最后一个关卡外，所有关卡都是完全被填满的，并且最后一个关卡中的所有节点都是尽可能靠左的。它可以包含 1 到 2^h
# 节点之间的最后一级 h 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [1,2,3,4,5,6]
# 输出：true
# 解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：root = [1,2,3,4,5,null,7]
# 输出：false
# 解释：值为 7 的结点没有尽可能靠向左侧。
# 
# 
# 
# 
# 提示：
# 
# 
# 树的结点数在范围  [1, 100] 内。
# 1 <= Node.val <= 1000
# 
# 
#


from commons.Tree import TreeNode


# @lc code=start
from collections import deque


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        has_none = False
        queue = deque([root])

        while queue:
            curr = queue.popleft()

            if curr.left:
                if has_none:
                    return False
                queue.append(curr.left)
            else:
                has_none = True

            if curr.right:
                if has_none:
                    return False
                queue.append(curr.right)
            else:
                has_none = True

        return True
# @lc code=end

# [1,2,3,4,5,null,7]
#      1
#    2   3
#  4  5 x 7
