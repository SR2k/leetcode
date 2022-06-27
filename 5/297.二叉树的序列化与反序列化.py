#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#
# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (57.45%)
# Likes:    855
# Dislikes: 0
# Total Accepted:    151.1K
# Total Submissions: 263K
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


from commons.Tree import TreeNode


# @lc code=start
from collections import deque


class Codec:
    def serialize(self, root: 'TreeNode') -> str:
        if not root:
            return '#'

        result: list[str] = []
        queue = deque([root])
        none_count = 0

        while queue:
            curr_node = queue.popleft()

            if curr_node is None:
                none_count += 1
                continue

            while none_count:
                result.append('#')
                none_count -= 1

            result.append(str(curr_node.val))

            queue.append(curr_node.left)
            queue.append(curr_node.right)

        return ','.join(result)


    def deserialize(self, data: str) -> 'TreeNode':
        if not data or data == '#':
            return None

        values = [None if x == '#' else int(x) for x in data.split(',')]
        values.reverse()
        root = TreeNode(values.pop(), None, None)
        nodes = deque([root])

        while nodes:
            curr = nodes.popleft()

            left_val = values.pop() if values else None
            right_val = values.pop() if values else None

            if left_val is not None:
                curr.left = TreeNode(left_val)
                nodes.append(curr.left)

            if right_val is not None:
                curr.right = TreeNode(right_val)
                nodes.append(curr.right)

        return root
# @lc code=end

