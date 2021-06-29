#
# @lc app=leetcode.cn id=536 lang=python3
#
# [536] 从字符串生成二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-string/description/
#
# algorithms
# Medium (53.68%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 5K
# Testcase Example:  '"4(2(3)(1))(6(5))"'
#
# 你需要从一个包括括号和整数的字符串构建一棵二叉树。
# 
# 输入的字符串代表一棵二叉树。它包括整数和随后的 0 ，1 或 2 对括号。整数代表根的值，一对括号内表示同样结构的子树。
# 
# 若存在左子结点，则从左子结点开始构建。
# 
# 
# 
# 示例：
# 
# 输入："4(2(3)(1))(6(5))"
# 输出：返回代表下列二叉树的根节点:
# 
# ⁠      4
# ⁠    /   \
# ⁠   2     6
# ⁠  / \   / 
# ⁠ 3   1 5   
# 
# 
# 
# 
# 提示：
# 
# 
# 输入字符串中只包含 '(', ')', '-' 和 '0' ~ '9' 
# 空树由 "" 而非"()"表示。
# 
# 
# 
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
from typing import Optional


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        stack: list[TreeNode] = []
        i, buffer = 0, ''

        while i < len(s):
            char = s[i]
            if char.isdigit() or char == '-':
                buffer += char
            elif buffer:
                node = TreeNode(int(buffer))
                if stack:
                    prev = stack[-1]
                    if prev.left:
                        prev.right = node
                    else:
                        prev.left = node
                stack.append(node)
                buffer = ''
            if char == ')':
                stack.pop()
            i += 1

        if buffer:
            return TreeNode(int(buffer))

        return stack[0] if stack else None
# @lc code=end
