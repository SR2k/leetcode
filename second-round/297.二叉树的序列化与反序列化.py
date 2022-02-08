#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#
# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (56.54%)
# Likes:    734
# Dislikes: 0
# Total Accepted:    122.2K
# Total Submissions: 216.1K
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


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x: int):
        self.val = x
        self.left: 'TreeNode' = None
        self.right: 'TreeNode' = None


# @lc code=start
from collections import deque


class Codec:
    def serialize(self, root: 'TreeNode'):
        queue = deque([root])
        result = ''

        while queue:
            curr = queue.popleft()
            if result:
                result += ','

            if not curr:
                result += '#'
            else:
                result += str(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)

        return result


    def deserialize(self, data: str):
        if data == '#':
            return None

        values = deque(data.split(','))
        head = TreeNode(values.popleft())
        nodes = deque([head])

        while values:
            curr_node = nodes.popleft()

            left_val = values.popleft()
            if left_val != '#':
                curr_node.left = TreeNode(int(left_val))
                nodes.append(curr_node.left)

            right_val = values.popleft()
            if right_val != '#':
                curr_node.right = TreeNode(int(right_val))
                nodes.append(curr_node.right)

        return head

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

codec = Codec()

tree = codec.deserialize("1,2,3,#,#,4,5")
print(codec.serialize(tree))

tree = codec.deserialize("1,2,3,#,#,4,5,6,#,7,8")
print(codec.serialize(tree))
