#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#
# https://leetcode-cn.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (67.71%)
# Likes:    127
# Dislikes: 0
# Total Accepted:    14.7K
# Total Submissions: 21.7K
# Testcase Example:  '[5,2,-3]'
#
# 给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
# 
# 你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
# 
# 
# 
# 示例 1：
# 输入:
# 
# ⁠ 5
# ⁠/  \
# 2   -3
# 
# 
# 返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。
# 
# 示例 2：
# 输入：
# 
# ⁠ 5
# ⁠/  \
# 2   -5
# 
# 
# 返回 [2]，只有 2 出现两次，-5 只出现 1 次。
# 
# 
# 
# 提示： 假设任意子树元素和均可以用 32 位有符号整数表示。
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> list[int]:
        max_freq = 0
        freq_2_sum = defaultdict(set)
        sum_2_freq = defaultdict(int)

        def add(val: int):
            nonlocal max_freq
            prev_freq = sum_2_freq[val]
            sum_2_freq[val] = prev_freq + 1
            freq_2_sum[prev_freq].discard(val)
            freq_2_sum[prev_freq + 1].add(val)
            max_freq = max(prev_freq + 1, max_freq)

        def helper(node: 'TreeNode'):
            if not node:
                return 0

            result = node.val + helper(node.left) + helper(node.right)
            add(result)
            return result

        helper(root)
        return list(freq_2_sum[max_freq])
# @lc code=end
