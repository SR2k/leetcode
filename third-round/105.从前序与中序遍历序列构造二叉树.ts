/*
 * @lc app=leetcode.cn id=105 lang=typescript
 *
 * [105] 从前序与中序遍历序列构造二叉树
 *
 * https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 *
 * algorithms
 * Medium (70.72%)
 * Likes:    1385
 * Dislikes: 0
 * Total Accepted:    288.1K
 * Total Submissions: 407.3K
 * Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
 *
 * 给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。
 *
 *
 *
 * 示例 1:
 *
 *
 * Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
 * Output: [3,9,20,null,null,15,7]
 *
 *
 * 示例 2:
 *
 *
 * Input: preorder = [-1], inorder = [-1]
 * Output: [-1]
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1
 * inorder.length == preorder.length
 * -3000
 * preorder 和 inorder 均无重复元素
 * inorder 均出现在 preorder
 * preorder 保证为二叉树的前序遍历序列
 * inorder 保证为二叉树的中序遍历序列
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  function helper(preBegin: number, preEnd: number, inBegin: number, inEnd: number): TreeNode|null {
    if (preEnd < preBegin) {
      return null
    }

    const root = new TreeNode(preorder[preBegin])
    if (preBegin === preEnd) {
      return root
    }

    const rootVal = preorder[preBegin]
    const rootInOrderIndex = inorder.indexOf(rootVal)

    const leftInOrderBegin = inBegin
    const leftInOrderEnd = rootInOrderIndex - 1
    const rightInOrderBegin = rootInOrderIndex + 1
    const rightInOrderEnd = inEnd

    const leftLength = leftInOrderEnd - leftInOrderBegin

    const leftPreOrderBegin = preBegin + 1
    const leftPreOrderEnd = leftPreOrderBegin + leftLength
    const rightPreOrderBegin = leftPreOrderEnd + 1
    const rightPreOrderEnd = preEnd

    root.left = helper(leftPreOrderBegin, leftPreOrderEnd, leftInOrderBegin, leftInOrderEnd)
    root.right = helper(rightPreOrderBegin, rightPreOrderEnd, rightInOrderBegin, rightInOrderEnd)
    return root
  }

  const result = helper(0, preorder.length - 1, 0, inorder.length - 1)
  return result
}
// @lc code=end
