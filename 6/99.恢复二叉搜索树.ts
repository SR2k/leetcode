/*
 * @lc app=leetcode.cn id=99 lang=typescript
 *
 * [99] 恢复二叉搜索树
 *
 * https://leetcode.cn/problems/recover-binary-search-tree/description/
 *
 * algorithms
 * Medium (60.40%)
 * Likes:    743
 * Dislikes: 0
 * Total Accepted:    106.9K
 * Total Submissions: 177K
 * Testcase Example:  '[1,3,null,null,2]'
 *
 * 给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,3,null,null,2]
 * 输出：[3,1,null,null,2]
 * 解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [3,1,4,null,null,2]
 * 输出：[2,1,4,null,null,3]
 * 解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
 *
 *
 *
 * 提示：
 *
 *
 * 树上节点的数目在范围 [2, 1000] 内
 * -2^31 <= Node.val <= 2^31 - 1
 *
 *
 *
 *
 * 进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用 O(1) 空间的解决方案吗？
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function recoverTree(root: TreeNode | null): void {
  const pair: Array<TreeNode | null> = [null, null]

  let curr: TreeNode | null = root
  const stack: TreeNode[] = []
  let prev = new TreeNode(-Infinity)
  while (stack.length || curr) {
    while (curr) {
      stack.push(curr)
      curr = curr.left
    }

    curr = stack.pop()!

    if (prev.val >= curr.val) {
      if (!pair[0]) {
        pair[0] = prev
        pair[1] = curr
      } else {
        pair[1] = curr;
        break
      }
    }

    prev = curr
    curr = curr.right
  }

  if (pair[0] && pair[1]) {
    [pair[0].val, pair[1].val] = [pair[1].val, pair[0].val]
  }
}
// @lc code=end
