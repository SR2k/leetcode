/*
 * @lc app=leetcode.cn id=101 lang=typescript
 *
 * [101] 对称二叉树
 *
 * https://leetcode.cn/problems/symmetric-tree/description/
 *
 * algorithms
 * Easy (58.21%)
 * Likes:    2088
 * Dislikes: 0
 * Total Accepted:    676.8K
 * Total Submissions: 1.2M
 * Testcase Example:  '[1,2,2,3,4,4,3]'
 *
 * 给你一个二叉树的根节点 root ， 检查它是否轴对称。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,2,2,3,4,4,3]
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [1,2,2,null,3,null,3]
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数目在范围 [1, 1000] 内
 * -100 <= Node.val <= 100
 *
 *
 *
 *
 * 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function isSymmetric(root: TreeNode): boolean {
  function check(l: TreeNode | null, r: TreeNode | null): boolean {
    if (!l) return !r
    if (!r) return !l

    return l.val === r.val && check(l.left, r.right) && check(l.right, r.left)
  }

  return check(root.left, root.right)
}
// @lc code=end
