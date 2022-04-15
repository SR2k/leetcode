#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#
# https://leetcode-cn.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (40.86%)
# Likes:    328
# Dislikes: 0
# Total Accepted:    40.3K
# Total Submissions: 98.6K
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
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left = {}
        right = {}
        result = 0


        def walk(node: Optional[TreeNode], level: int, x: int):
            if not node:
                return

            if level not in left:
                left[level] = x
                right[level] = x
            else:
                left[level] = min(left[level], x)
                right[level] = max(right[level], x)

            nonlocal result
            result = max(result, right[level] - left[level] + 1)

            walk(node.left, level + 1, 2 * x)
            walk(node.right, level + 1, 2 * x + 1)


        walk(root, 0, 0)
        return result
# @lc code=end
