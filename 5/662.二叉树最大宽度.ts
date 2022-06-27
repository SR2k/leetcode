/*
 * @lc app=leetcode.cn id=662 lang=typescript
 *
 * [662] 二叉树最大宽度
 *
 * https://leetcode.cn/problems/maximum-width-of-binary-tree/description/
 *
 * algorithms
 * Medium (40.99%)
 * Likes:    361
 * Dislikes: 0
 * Total Accepted:    45K
 * Total Submissions: 109.7K
 * Testcase Example:  '[1,3,2,5,3,null,9]'
 *
 * 给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary
 * tree）结构相同，但一些节点为空。
 *
 * 每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
 *
 * 示例 1:
 *
 *
 * 输入:
 *
 * ⁠          1
 * ⁠        /   \
 * ⁠       3     2
 * ⁠      / \     \
 * ⁠     5   3     9
 *
 * 输出: 4
 * 解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
 *
 *
 * 示例 2:
 *
 *
 * 输入:
 *
 * ⁠         1
 * ⁠        /
 * ⁠       3
 * ⁠      / \
 * ⁠     5   3
 *
 * 输出: 2
 * 解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
 *
 *
 * 示例 3:
 *
 *
 * 输入:
 *
 * ⁠         1
 * ⁠        / \
 * ⁠       3   2
 * ⁠      /
 * ⁠     5
 *
 * 输出: 2
 * 解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
 *
 *
 * 示例 4:
 *
 *
 * 输入:
 *
 * ⁠         1
 * ⁠        / \
 * ⁠       3   2
 * ⁠      /     \
 * ⁠     5       9
 * ⁠    /         \
 * ⁠   6           7
 * 输出: 8
 * 解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
 *
 *
 * 注意: 答案在32位有符号整数的表示范围内。
 *
 */

import { TreeNode } from './commons/Tree'

// @lc code=start
function widthOfBinaryTree(root: TreeNode | null): number {
  if (!root) return 0

  const levels: Array<[number, number]> = []
  const levelEntry: number[] = []
  let result = 0

  const stack: Array<[TreeNode, number, number]> = [[root, 0, 0]]
  while (stack.length) {
    const [node, level, offset] = stack.pop()!

    if (level > levels.length - 1) {
      levels.push([0, 0])
      levelEntry.push(offset)
    }

    const l = levels[level], entry = levelEntry[level]
    l[0] = Math.min(l[0], offset - entry)
    l[1] = Math.max(l[1], offset - entry)
    result = Math.max(result, l[1] - l[0] + 1)

    if (node.left) {
      stack.push([node.left, level + 1, (offset - entry) * 2])
    }
    if (node.right) {
      stack.push([node.right, level + 1, (offset - entry) * 2 + 1])
    }
  }

  return result
}
// @lc code=end
