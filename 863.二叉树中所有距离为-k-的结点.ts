/*
 * @lc app=leetcode.cn id=863 lang=typescript
 *
 * [863] 二叉树中所有距离为 K 的结点
 *
 * https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/description/
 *
 * algorithms
 * Medium (61.08%)
 * Likes:    549
 * Dislikes: 0
 * Total Accepted:    43.6K
 * Total Submissions: 71.3K
 * Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
 *
 * 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 k 。
 *
 * 返回到目标结点 target 距离为 k 的所有结点的值的列表。 答案可以以 任何顺序 返回。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
 * 输出：[7,4,1]
 * 解释：所求结点为与目标结点（值为 5）距离为 2 的结点，值分别为 7，4，以及 1
 *
 *
 * 示例 2:
 *
 *
 * 输入: root = [1], target = 1, k = 3
 * 输出: []
 *
 *
 *
 *
 * 提示:
 *
 *
 * 节点数在 [1, 500] 范围内
 * 0 <= Node.val <= 500
 * Node.val 中所有值 不同
 * 目标结点 target 是树上的结点。
 * 0 <= k <= 1000
 *
 *
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function distanceK(root: TreeNode | null, target: TreeNode | null, k: number): number[] {
  const parentMap = new Map<TreeNode, TreeNode | null>()
  buildParentMap(root, target, parentMap)

  const result: number[] = []

  function helper(node: TreeNode | null, from: TreeNode | null, k: number) {
    if (!node) return
    if (k === 0) {
      result.push(node.val)
      return
    }

    if (node.left !== from) {
      helper(node.left, node, k - 1)
    }
    if (node.right !== from) {
      helper(node.right, node, k - 1)
    }
    const parent = parentMap.get(node)
    if (parent && parent !== from) {
      helper(parent, node, k - 1)
    }
  }

  helper(target, null, k)
  return result
}

function buildParentMap(root: TreeNode | null, target: TreeNode | null, map: Map<TreeNode, TreeNode | null>) {
  if (!root) return
  if (root === target) return

  if (root.left) {
    map.set(root.left, root)
    buildParentMap(root.left, target, map)
  }
  if (root.right) {
    map.set(root.right, root)
    buildParentMap(root.right, target, map)
  }
}
// @lc code=end

// [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
//              3
//       5            1
//   6      2     0       8
// x  x   7   4
