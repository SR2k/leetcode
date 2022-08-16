/*
 * @lc app=leetcode.cn id=105 lang=typescript
 *
 * [105] 从前序与中序遍历序列构造二叉树
 *
 * https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 *
 * algorithms
 * Medium (71.14%)
 * Likes:    1644
 * Dislikes: 0
 * Total Accepted:    377.5K
 * Total Submissions: 530.6K
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
  const inPosition: Record<number, number> = {}
  inorder.forEach((n, i) => {
    inPosition[n] = i
  })

  function helper(preBegin: number, preEnd: number, inBegin: number, inEnd: number) {
    if (preBegin > preEnd || inBegin > inEnd) return null

    const rootVal = preorder[preBegin]
    const rootNode = new TreeNode(rootVal)
    if (preBegin === preEnd) return rootNode

    const rootInPosition = inPosition[rootVal]

    const leftInBegin = inBegin
    const leftInEnd = rootInPosition - 1
    const rightInBegin = rootInPosition + 1
    const rightInEnd = inEnd

    const leftLength = leftInEnd - leftInBegin + 1

    const leftPreBegin = preBegin + 1
    const leftPreEnd = leftPreBegin + leftLength - 1
    const rightPreBegin = leftPreEnd + 1
    const rightPreEnd = preEnd

    rootNode.left = helper(leftPreBegin, leftPreEnd, leftInBegin, leftInEnd)
    rootNode.right = helper(rightPreBegin, rightPreEnd, rightInBegin, rightInEnd)
    return rootNode
  }

  return helper(0, preorder.length - 1, 0, inorder.length - 1)
}
// @lc code=end
