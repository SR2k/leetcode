/*
 * @lc app=leetcode.cn id=98 lang=typescript
 *
 * [98] 验证二叉搜索树
 *
 * https://leetcode-cn.com/problems/validate-binary-search-tree/description/
 *
 * algorithms
 * Medium (35.48%)
 * Likes:    1407
 * Dislikes: 0
 * Total Accepted:    419.4K
 * Total Submissions: 1.2M
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
function isValidBST(root: TreeNode): boolean {
  function helper(node: TreeNode | null, max: number, min: number): boolean {
    if (!node) return true

    if (node.val >= max || node.val <= min) {
      return false
    }

    return helper(node.left, Math.min(node.val, max), min)
      && helper(node.right, max, Math.max(node.val, min))
  }

  return helper(root, Infinity, -Infinity)
}
// @lc code=end
