/*
 * @lc app=leetcode.cn id=110 lang=typescript
 *
 * [110] 平衡二叉树
 *
 * https://leetcode.cn/problems/balanced-binary-tree/description/
 *
 * algorithms
 * Easy (57.30%)
 * Likes:    1120
 * Dislikes: 0
 * Total Accepted:    407.1K
 * Total Submissions: 710.5K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给定一个二叉树，判断它是否是高度平衡的二叉树。
 *
 * 本题中，一棵高度平衡二叉树定义为：
 *
 *
 * 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [3,9,20,null,null,15,7]
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [1,2,2,3,3,null,null,4,4]
 * 输出：false
 *
 *
 * 示例 3：
 *
 *
 * 输入：root = []
 * 输出：true
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中的节点数在范围 [0, 5000] 内
 * -10^4
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function isBalanced(root: TreeNode | null): boolean {
  function check(node: TreeNode | null): [number, boolean] {
    if (!node) {
      return [0, true]
    }

    const [leftHeight, leftBalance] = check(node.left)
    const [rightHeight, rightBalance] = check(node.right)
    return [
      Math.max(leftHeight, rightHeight) + 1,
      leftBalance && rightBalance && Math.abs(leftHeight - rightHeight) <= 1,
    ]
  }

  return check(root)[1]
}
// @lc code=end
