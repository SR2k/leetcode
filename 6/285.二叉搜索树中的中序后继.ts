/*
 * @lc app=leetcode.cn id=285 lang=typescript
 *
 * [285] 二叉搜索树中的中序后继
 *
 * https://leetcode.cn/problems/inorder-successor-in-bst/description/
 *
 * algorithms
 * Medium (64.20%)
 * Likes:    170
 * Dislikes: 0
 * Total Accepted:    12.4K
 * Total Submissions: 19.3K
 * Testcase Example:  '[2,1,3]\n1'
 *
 * 给定一棵二叉搜索树和其中的一个节点 p ，找到该节点在树中的中序后继。如果节点没有中序后继，请返回 null 。
 *
 * 节点 p 的后继是值比 p.val 大的节点中键值最小的节点。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：root = [2,1,3], p = 1
 * 输出：2
 * 解释：这里 1 的中序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。
 *
 *
 * 示例 2：
 *
 *
 *
 *
 * 输入：root = [5,3,6,2,4,null,null,1], p = 6
 * 输出：null
 * 解释：因为给出的节点没有中序后继，所以答案就返回 null 了。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点的数目在范围 [1, 10^4] 内。
 * -10^5
 * 树中各节点的值均保证唯一。
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function inorderSuccessor(root: TreeNode | null, p: TreeNode | null): TreeNode | null {
  if (!root || !p) return null

  if (p.right) {
    let result = p.right
    while (result.left) {
      result = result.left
    }
    return result
  }

  const path: TreeNode[] = []
  let curr: TreeNode | null = root
  while (curr && curr !== p) {
    path.push(curr)
    if (p.val < curr.val) {
      curr = curr.left
    } else {
      curr = curr.right
    }
  }
  if (!curr) return null

  while (path.length && path[path.length - 1].right === p) {
    p = path.pop()!
  }

  return path.length ? path[path.length - 1] : null
}
// @lc code=end
