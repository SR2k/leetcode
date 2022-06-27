#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#
# https://leetcode.cn/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (47.62%)
# Likes:    744
# Dislikes: 0
# Total Accepted:    127K
# Total Submissions: 266.7K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# 
# 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true
# ；否则，返回 false 。
# 
# 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,4,5,1,2], subRoot = [4,1,2]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# root 树上的节点数量范围是 [1, 2000]
# subRoot 树上的节点数量范围是 [1, 1000]
# -10^4 
# -10^4 
# 
# 
# 
# 
#


from commons.Tree import TreeNode

# @lc code=start
SCALE = 31
MODULO = 60000000
NONE_REPR = -20000


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        root_values = Solution.pre_order(root)
        sub_values = Solution.pre_order(subRoot)

        return Solution.rabin_crab_find(root_values, sub_values)


    @staticmethod
    def pre_order(node: TreeNode, result: list[int] = None):
        if result is None:
            result = []

        if not node:
            result.append(NONE_REPR)
            return result

        result.append(node.val)
        Solution.pre_order(node.left, result)
        Solution.pre_order(node.right, result)

        return result


    @staticmethod
    def rabin_crab_find(l1: list[int], l2: list[int]):
        if len(l2) > len(l1):
            return False

        hash_2 = Solution.hash(l2, 0, len(l2) - 1)
        hash = Solution.hash(l1, 0, len(l2) - 1)

        if hash == hash_2 and Solution.check(l1, 0, len(l2) - 1, l2):
            return True

        top_scale = 1
        for _ in range(len(l2) - 1):
            top_scale = (top_scale * SCALE) % MODULO

        for i in range(len(l2), len(l1)):
            prev_begin = i - len(l2)

            hash = (hash - top_scale * l1[prev_begin]) % MODULO
            hash = (hash * SCALE + l1[i]) % MODULO

            if hash == hash_2 and Solution.check(l1, prev_begin + 1, i, l2):
                return True

        return False


    @staticmethod
    def hash(l: list[int], begin: int, end: int):
        result = 0
        for i in range(begin, end + 1):
            result = (result * SCALE + l[i]) % MODULO
        return result


    @staticmethod
    def check(l1: list[int], begin: int, end: int, l2: list[int]) -> bool:
        for i in range(begin, end + 1):
            if l1[i] != l2[i - begin]:
                return False
        return True
# @lc code=end
