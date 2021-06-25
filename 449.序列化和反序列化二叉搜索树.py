#
# @lc app=leetcode.cn id=449 lang=python3
#
# [449] 序列化和反序列化二叉搜索树
#
# https://leetcode-cn.com/problems/serialize-and-deserialize-bst/description/
#
# algorithms
# Medium (55.40%)
# Likes:    187
# Dislikes: 0
# Total Accepted:    13.1K
# Total Submissions: 23.6K
# Testcase Example:  '[2,1,3]'
#
# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
# 
# 设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。
# 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
# 
# 编码的字符串应尽可能紧凑。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [2,1,3]
# 输出：[2,1,3]
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数范围是 [0, 10^4]
# 0 
# 题目数据 保证 输入的树是一棵二叉搜索树。
# 
# 
# 
# 
# 注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root: return '#'

        ret_temp: list[str] = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            ret_temp.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(ret_temp)

    @staticmethod
    def value_to_node(val: str) -> TreeNode:
        if val == '#': return None
        return TreeNode(int(val))

    def deserialize(self, data: str) -> TreeNode:
        node_values = data.split(',')
        if not node_values: return None

        root = Codec.value_to_node(node_values.pop(0))
        if not root: return root

        queue = [root]

        while node_values and queue:
            curr = queue.pop(0)

            curr.left = Codec.value_to_node(node_values.pop(0))
            curr.right = Codec.value_to_node(node_values.pop(0))

            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)

        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

