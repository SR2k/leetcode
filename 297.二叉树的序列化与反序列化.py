#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#
# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (57.18%)
# Likes:    814
# Dislikes: 0
# Total Accepted:    142.5K
# Total Submissions: 249.2K
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
class Codec:
    def serialize(self, root: TreeNode):
        result: list[str] = []

        def helper(node: TreeNode):
            if not node:
                result.append('#')
                return

            result.append(str(node.val))
            helper(node.left)
            helper(node.right)


        helper(root)
        return ','.join(result)


    def deserialize(self, data: str):
        values = data.split(',')
        values = [int(x) if x != '#' else None for x in values]
        values.reverse()

        root_val = values.pop()
        if root_val is None:
            return None

        root = TreeNode(root_val)

        def helper(parent):
            if not parent:
                return

            left_val = values.pop()
            if left_val is not None:
                parent.left = TreeNode(left_val)
                helper(parent.left)

            right_val = values.pop()
            if right_val is not None:
                parent.right = TreeNode(right_val)
                helper(parent.right)

            # print(parent.val, left_val, right_val)

        helper(root)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
