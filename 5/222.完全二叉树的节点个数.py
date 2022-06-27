#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
# https://leetcode.cn/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (79.81%)
# Likes:    705
# Dislikes: 0
# Total Accepted:    188.5K
# Total Submissions: 236.1K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
# 
# 完全二叉树
# 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h
# 层，则该层包含 1~ 2^h 个节点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,4,5,6]
# 输出：6
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目范围是[0, 5 * 10^4]
# 0 
# 题目数据保证输入的树是 完全二叉树
# 
# 
# 
# 
# 进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
# 
#


from commons.Tree import TreeNode


# @lc code=start
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        left, right = 0, 50000

        while left + 1 < right:
            middle = (left + right) // 2

            if Solution.check(root, middle):
                left = middle
            else:
                right = middle

        if Solution.check(root, right):
            return right
        return left


    @staticmethod
    def check(root: TreeNode, n: int) -> bool:
        stack: list[int] = []
        while n > 1:
            stack.append(n % 2)
            n = n // 2

        while stack and root:
            direction = stack.pop()

            if direction == 0:
                root = root.left
            else:
                root = root.right

        return not not root
# @lc code=end

# 12 - 6 - 3 - 1
#
#            1
#       2          3
#    4    5     6     7
#   8 9 10 11 12 13 14 15
