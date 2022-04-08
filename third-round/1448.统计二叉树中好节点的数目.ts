/*
 * @lc app=leetcode.cn id=1448 lang=typescript
 *
 * [1448] 统计二叉树中好节点的数目
 *
 * https://leetcode-cn.com/problems/count-good-nodes-in-binary-tree/description/
 *
 * algorithms
 * Medium (71.42%)
 * Likes:    41
 * Dislikes: 0
 * Total Accepted:    11.6K
 * Total Submissions: 16.2K
 * Testcase Example:  '[3,1,4,3,null,1,5]'
 *
 * 给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。
 *
 * 「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：root = [3,1,4,3,null,1,5]
 * 输出：4
 * 解释：图中蓝色节点为好节点。
 * 根节点 (3) 永远是个好节点。
 * 节点 4 -> (3,4) 是路径中的最大值。
 * 节点 5 -> (3,4,5) 是路径中的最大值。
 * 节点 3 -> (3,1,3) 是路径中的最大值。
 *
 * 示例 2：
 *
 *
 *
 * 输入：root = [3,3,null,4,2]
 * 输出：3
 * 解释：节点 2 -> (3, 3, 2) 不是好节点，因为 "3" 比它大。
 *
 * 示例 3：
 *
 * 输入：root = [1]
 * 输出：1
 * 解释：根节点是好节点。
 *
 *
 *
 * 提示：
 *
 *
 * 二叉树中节点数目范围是 [1, 10^5] 。
 * 每个节点权值的范围是 [-10^4, 10^4] 。
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function goodNodes(root: TreeNode): number {
  function helper(node: TreeNode | null, maxValue: number): number {
    if (!node) return 0

    const result = helper(node.left, Math.max(node.val, maxValue))
      + helper(node.right, Math.max(node.val, maxValue))

    if (maxValue <= node.val) {
      return result + 1
    }
    return result
  }

  return helper(root, root.val)
}
// @lc code=end

export function goodNodesIteration(root: TreeNode): number {
  const queue = [[root.val, root]]
  let result = 0

  while (queue.length) {
    const [maxValue, node] = queue.shift()!

    if (node.val >= maxValue) {
      result += 1
    }

    const nextMax = Math.max(node.val, maxValue)
    if (node.left) {
      queue.push([nextMax, node.left])
    }
    if (node.right) {
      queue.push([nextMax, node.right])
    }
  }

  return result
}
