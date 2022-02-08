#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (44.67%)
# Likes:    1389
# Dislikes: 0
# Total Accepted:    184.7K
# Total Submissions: 413.4K
# Testcase Example:  '[1,2,3]'
#
# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个
# 节点，且不一定经过根节点。
# 
# 路径和 是路径中各节点值的总和。
# 
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
# 
# 示例 2：
# 
# 
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目范围是 [1, 3 * 10^4]
# -1000 
# 
# 
#


from typing import Optional
from commons.Tree import TreeNode


# @lc code=start
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')

        def helper(node: Optional[TreeNode]):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            max_single = max(left + node.val, right + node.val, node.val)
            nonlocal result
            result = max(max_single, result, left + right + node.val)
            return max_single

        helper(root)
        return result
# @lc code=end

s = Solution()
print(s.maxPathSum(TreeNode.deserialize([-10,9,20,None,None,15,7])))
