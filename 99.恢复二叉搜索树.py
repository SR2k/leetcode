#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#
# https://leetcode.cn/problems/recover-binary-search-tree/description/
#
# algorithms
# Medium (60.47%)
# Likes:    733
# Dislikes: 0
# Total Accepted:    104.2K
# Total Submissions: 172.3K
# Testcase Example:  '[1,3,null,null,2]'
#
# 给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,3,null,null,2]
# 输出：[3,1,null,null,2]
# 解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [3,1,4,null,null,2]
# 输出：[2,1,4,null,null,3]
# 解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
# 
# 
# 
# 提示：
# 
# 
# 树上节点的数目在范围 [2, 1000] 内
# -2^31 <= Node.val <= 2^31 - 1
# 
# 
# 
# 
# 进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用 O(1) 空间的解决方案吗？
# 
#


from commons.Tree import TreeNode
from typing import Optional


# @lc code=start
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev = None
        first = last = None

        def walk(node: Optional[TreeNode]):
            if not node:
                return

            walk(node.left)

            nonlocal first, last, prev
            if prev and (prev.val > node.val):
                if not first:
                    first = prev
                last = node
 
            prev = node

            walk(node.right)

        walk(root)

        if first and last:
            first.val, last.val = last.val, first.val
# @lc code=end

# [1,3,null,null,2]

#     1
#   3    x
# x   2

# 1 7 3 4 5 6 2 8 9
