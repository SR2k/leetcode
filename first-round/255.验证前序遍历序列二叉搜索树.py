#
# @lc app=leetcode.cn id=255 lang=python3
#
# [255] 验证前序遍历序列二叉搜索树
#
# https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree/description/
#
# algorithms
# Medium (47.23%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    5K
# Total Submissions: 10.6K
# Testcase Example:  '[5,2,1,3,6]'
#
# 给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。
# 
# 你可以假定该序列中的数都是不相同的。
# 
# 参考以下这颗二叉搜索树：
# 
# ⁠    5
# ⁠   / \
# ⁠  2   6
# ⁠ / \
# ⁠1   3
# 
# 示例 1：
# 
# 输入: [5,2,6,1,3]
# 输出: false
# 
# 示例 2：
# 
# 输入: [5,2,1,3,6]
# 输出: true
# 
# 进阶挑战：
# 
# 您能否使用恒定的空间复杂度来完成此题？
# 
#

# @lc code=start
class Solution:
    def verifyPreorder(self, preorder: list[int]) -> bool:
        if len(preorder) <= 2:
            return True

        # 用一个单调栈来模拟遍历的过程，栈中的元素都是递减的，刚好与从根节点向左遍历表现一致
        # 入栈 -> 从根节点一路向左
        # 出栈 -> 左子树到底了，向右子树进军！最后出栈的就是当前左右子树的根节点（相当于从左子树一路回退）
        stack = []
        prev = float('-inf')
        for n in preorder:
            while stack and stack[-1] < n:
                prev = stack.pop()

            # 由于最后出栈的就是当前左右子树的根节点，我们后面入栈的值都必须比它大
            if n < prev:
                return False

            stack.append(n)

        return True
# @lc code=end

# print(Solution().verifyPreorder([5,2,6,1,3]))
