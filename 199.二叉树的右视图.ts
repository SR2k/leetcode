/*
 * @lc app=leetcode.cn id=199 lang=typescript
 *
 * [199] 二叉树的右视图
 *
 * https://leetcode.cn/problems/binary-tree-right-side-view/description/
 *
 * algorithms
 * Medium (65.70%)
 * Likes:    749
 * Dislikes: 0
 * Total Accepted:    237.3K
 * Total Submissions: 361.1K
 * Testcase Example:  '[1,2,3,null,5,null,4]'
 *
 * 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
 *
 *
 *
 * 示例 1:
 *
 *
 *
 *
 * 输入: [1,2,3,null,5,null,4]
 * 输出: [1,3,4]
 *
 *
 * 示例 2:
 *
 *
 * 输入: [1,null,3]
 * 输出: [1,3]
 *
 *
 * 示例 3:
 *
 *
 * 输入: []
 * 输出: []
 *
 *
 *
 *
 * 提示:
 *
 *
 * 二叉树的节点个数的范围是 [0,100]
 * -100
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function rightSideView(root: TreeNode | null): number[] {
  const result: number[] = []
  const queue = [root!].filter(Boolean)

  while (queue.length) {
    let rightmost = -1
    const levelLength = queue.length

    for (let i = 0; i < levelLength; i++) {
      const node = queue.shift()!
      rightmost = node.val

      if (node.left) {
        queue.push(node.left)
      }
      if (node.right) {
        queue.push(node.right)
      }
    }

    result.push(rightmost)
  }

  return result
}
// @lc code=end
