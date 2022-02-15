/*
 * @lc app=leetcode.cn id=103 lang=typescript
 *
 * [103] 二叉树的锯齿形层序遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
 *
 * algorithms
 * Medium (57.23%)
 * Likes:    591
 * Dislikes: 0
 * Total Accepted:    201.2K
 * Total Submissions: 351.6K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [3,9,20,null,null,15,7]
 * 输出：[[3],[20,9],[15,7]]
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
 * -100 <= Node.val <= 100
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function zigzagLevelOrder(root: TreeNode | null): number[][] {
  if (!root) return []

  const queue = [root]
  const result = []

  while (queue.length) {
    const levelLength = queue.length
    const levelResult = []

    for (let i = 0; i < levelLength; i++) {
      const node = queue.shift()!

      if (result.length % 2) {
        levelResult.unshift(node.val)
      } else {
        levelResult.push(node.val)
      }

      if (node.left) {
        queue.push(node.left)
      }
      if (node.right) {
        queue.push(node.right)
      }
    }

    result.push(levelResult)
  }

  return result
}
// @lc code=end
