#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#
# https://leetcode-cn.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (41.00%)
# Likes:    313
# Dislikes: 0
# Total Accepted:    36.8K
# Total Submissions: 89.8K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary
# tree）结构相同，但一些节点为空。
# 
# 每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
# 
# 示例 1:
# 
# 
# 输入: 
# 
# ⁠          1
# ⁠        /   \
# ⁠       3     2
# ⁠      / \     \  
# ⁠     5   3     9 
# 
# 输出: 4
# 解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        /  
# ⁠       3    
# ⁠      / \       
# ⁠     5   3     
# 
# 输出: 2
# 解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
# 
# 
# 示例 3:
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2 
# ⁠      /        
# ⁠     5      
# 
# 输出: 2
# 解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
# 
# 
# 示例 4:
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      /     \  
# ⁠     5       9 
# ⁠    /         \
# ⁠   6           7
# 输出: 8
# 解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
# 
# 
# 注意: 答案在32位有符号整数的表示范围内。
# 
#


from typing import Optional
from commons.Tree import TreeNode


# @lc code=start
from collections import defaultdict


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        edges = defaultdict(lambda: (float('inf'), -float('inf')))

        def helper(node: TreeNode, i: int, j: int):
            if not node:
                return

            prev = edges[i]
            curr = (min(j, prev[0]), max(j, prev[1]))
            edges[i] = curr
            nonlocal result
            result = max(curr[1] - curr[0] + 1, result)

            helper(node.left, i + 1, 2 * j)
            helper(node.right, i + 1, 2 * j + 1)

        helper(root, 0, 0)
        return result
# @lc code=end
