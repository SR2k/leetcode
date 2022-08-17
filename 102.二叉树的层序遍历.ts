/*
 * @lc app=leetcode.cn id=102 lang=typescript
 *
 * [102] 二叉树的层序遍历
 *
 * https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
 *
 * algorithms
 * Medium (65.02%)
 * Likes:    1426
 * Dislikes: 0
 * Total Accepted:    648.8K
 * Total Submissions: 997.8K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [3,9,20,null,null,15,7]
 * 输出：[[3],[9,20],[15,7]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [1]
 * 输出：[[1]]
 *
 *
 * 示例 3：
 *
 *
 * 输入：root = []
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数目在范围 [0, 2000] 内
 * -1000 <= Node.val <= 1000
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function levelOrder(root: TreeNode | null): number[][] {
  const result: number[][] = []
  const queue = [root].filter(Boolean)

  while (queue.length) {
    const levelLength = queue.length
    const levelResult: number[] = []

    for (let i = 0; i < levelLength; i++) {
      const node = queue.shift()!

      if (node.left) {
        queue.push(node.left)
      }
      if (node.right) {
        queue.push(node.right)
      }

      levelResult.push(node.val)
    }

    result.push(levelResult)
  }

  return result
}
// @lc code=end
