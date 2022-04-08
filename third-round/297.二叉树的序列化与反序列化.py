#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#
# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (56.78%)
# Likes:    787
# Dislikes: 0
# Total Accepted:    135.4K
# Total Submissions: 237.9K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# 
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
# 
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 /
# 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# 
# 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode
# 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：[1]
# 
# 
# 示例 4：
# 
# 
# 输入：root = [1,2]
# 输出：[1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中结点数在范围 [0, 10^4] 内
# -1000 
# 
# 
#

# @lc code=start
from collections import deque


class Codec:
    def serialize(self, root):
        if not root:
            return ""

        queue = deque([root])
        result = [root]

        while queue:
            curr = queue.popleft()

            result.append(curr.left)
            result.append(curr.right)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


        while result[-1] is None:
            result.pop()

        return ",".join(['#' if x is None else str(x.val) for x in result])


    def deserialize(self, data):
        if not data:
            return None

        cut = data.split(',')
        values = deque([int(v) if v != '#' else None for v in cut])
        root = TreeNode(values.popleft())
        nodes = deque([root])

        while values:
            node = nodes.popleft()

            if values:
                vl = values.popleft()
                node.left = TreeNode(vl) if vl is not None else None
            if values:
                vr = values.popleft()
                node.right = TreeNode(vr) if vr is not None else None

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
