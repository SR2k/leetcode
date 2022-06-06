#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode.cn/problems/path-sum-iii/description/
#
# algorithms
# Medium (56.71%)
# Likes:    1348
# Dislikes: 0
# Total Accepted:    168.5K
# Total Submissions: 297.7K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
# 
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3
# 
# 
# 
# 
# 提示:
# 
# 
# 二叉树的节点个数的范围是 [0,1000]
# -10^9  
# -1000  
# 
# 
#


from commons.Tree import TreeNode
from typing import Optional


# @lc code=start
from collections import Counter


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0

        def walk(node: Optional[TreeNode], prefix_sum: int, counter: Counter):
            if not node:
                return

            nonlocal result
            prefix_sum += node.val
            result += counter[prefix_sum - targetSum]
            counter[prefix_sum ] += 1

            walk(node.left, prefix_sum, counter)
            walk(node.right, prefix_sum, counter)

            counter[prefix_sum] -= 1

        counter = Counter([0])
        walk(root, 0, counter)

        return result
# @lc code=end

# [10,5,-3,3,2,null,11,3,-2,null,1]
                 10
        5                -3
    3       2       x          11
  3  -2   x   1
