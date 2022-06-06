#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (76.78%)
# Likes:    1050
# Dislikes: 0
# Total Accepted:    264.4K
# Total Submissions: 344.2K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
# 
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
# 
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums 按 严格递增 顺序排列
# 
# 
#


from commons.Tree import TreeNode
from typing import Optional, List


# @lc code=start
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return Solution.build_tree(nums, 0, len(nums) - 1)


    @staticmethod
    def build_tree(nums: list[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        if left == right:
            return TreeNode(nums[left])
        if left == right - 1:
            return TreeNode(nums[right], TreeNode(nums[left]))

        middle = (left + right) // 2
        return TreeNode(
            nums[middle],
            Solution.build_tree(nums, left, middle - 1),
            Solution.build_tree(nums, middle + 1, right),
        )
# @lc code=end
