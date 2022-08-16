/*
 * @lc app=leetcode.cn id=98 lang=typescript
 *
 * [98] 验证二叉搜索树
 *
 * https://leetcode.cn/problems/validate-binary-search-tree/description/
 *
 * algorithms
 * Medium (36.16%)
 * Likes:    1635
 * Dislikes: 0
 * Total Accepted:    535.1K
 * Total Submissions: 1.5M
 * Testcase Example:  '[2,1,3]'
 *
 * 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
 *
 * 有效 二叉搜索树定义如下：
 *
 *
 * 节点的左子树只包含 小于 当前节点的数。
 * 节点的右子树只包含 大于 当前节点的数。
 * 所有左子树和右子树自身必须也是二叉搜索树。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [2,1,3]
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [5,1,4,null,null,3,6]
 * 输出：false
 * 解释：根节点的值是 5 ，但是右子节点的值是 4 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数目范围在[1, 10^4] 内
 * -2^31 <= Node.val <= 2^31 - 1
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function isValidBST(root: TreeNode | null): boolean {
  const stack: TreeNode[] = []

  let prev = Number.MIN_SAFE_INTEGER
  let curr = root

  while (stack.length || curr) {
    while (curr) {
      stack.push(curr)
      curr = curr.left
    }

    curr = stack.pop()!
    if (curr.val <= prev) {
      return false
    }
    prev = curr.val
    curr = curr.right
  }

  return true
}
// @lc code=end
