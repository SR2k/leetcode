/*
 * @lc app=leetcode.cn id=863 lang=typescript
 *
 * [863] 二叉树中所有距离为 K 的结点
 *
 * https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/description/
 *
 * algorithms
 * Medium (61.47%)
 * Likes:    580
 * Dislikes: 0
 * Total Accepted:    47.2K
 * Total Submissions: 76.7K
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
  const parent = new Map<TreeNode, TreeNode>()

  function find(curr: TreeNode | null) {
    if (!curr) return
    if (curr === target) return
    if (curr.left) parent.set(curr.left, curr)
    if (curr.right) parent.set(curr.right, curr)
    find(curr.left)
    find(curr.right)
  }
  find(root)

  const result: number[] = []
  const seen = new Set<TreeNode>()
  function getChildN(node: TreeNode | null | undefined, n: number) {
    if (!node || seen.has(node)) return
    seen.add(node)
    if (n === 0) {
      result.push(node.val)
      return
    }

    getChildN(node.left, n - 1)
    getChildN(node.right, n - 1)
  }

  let curr: TreeNode | null | undefined = target
  while (curr && k >= 0) {
    getChildN(curr, k)
    curr = parent.get(curr)
    k--
  }

  return result
}
// @lc code=end
