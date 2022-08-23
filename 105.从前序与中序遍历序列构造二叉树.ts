/*
 * @lc app=leetcode.cn id=105 lang=typescript
 *
 * [105] 从前序与中序遍历序列构造二叉树
 *
 * https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 *
 * algorithms
 * Medium (71.32%)
 * Likes:    1699
 * Dislikes: 0
 * Total Accepted:    406.1K
 * Total Submissions: 569.3K
 * Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
 *
 * 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder
 * 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
 * 输出: [3,9,20,null,null,15,7]
 *
 *
 * 示例 2:
 *
 *
 * 输入: preorder = [-1], inorder = [-1]
 * 输出: [-1]
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= preorder.length <= 3000
 * inorder.length == preorder.length
 * -3000 <= preorder[i], inorder[i] <= 3000
 * preorder 和 inorder 均 无重复 元素
 * inorder 均出现在 preorder
 * preorder 保证 为二叉树的前序遍历序列
 * inorder 保证 为二叉树的中序遍历序列
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  const inOrderIndexMapping: Record<number, number> = {}
  inorder.forEach((n, i) => {
    inOrderIndexMapping[n] = i
  })

  function build(preBegin: number, preEnd: number, inBegin: number, inEnd: number) {
    if (preBegin > preEnd) return null

    const rootVal = preorder[preBegin]
    const inRoot = inOrderIndexMapping[rootVal]

    const leftLength = inRoot - 1 - inBegin + 1

    const leftPreBegin = preBegin + 1
    const leftPreEnd = leftPreBegin + leftLength - 1
    const rightPreBegin = leftPreEnd + 1
    const rightPreEnd = preEnd

    const rootNode = new TreeNode(rootVal)
    rootNode.left = build(leftPreBegin, leftPreEnd, inBegin, inRoot - 1)
    rootNode.right = build(rightPreBegin, rightPreEnd, inRoot + 1, inEnd)
    return rootNode
  }

  const m = preorder.length
  return build(0, m - 1, 0, m - 1)
}
// @lc code=end
