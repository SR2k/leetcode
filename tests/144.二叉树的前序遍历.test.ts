import { preorderTraversal } from '../144.二叉树的前序遍历'
import { TreeNode } from '../commons/Tree'

describe('144. Binary Tree Preorder Traversal', () => {
  it('should work', () => {
    expect(preorderTraversal(TreeNode.fromArray([1, 2, 3, 4, 5, 6, 7, 8])))
      .toStrictEqual([1, 2, 4, 8, 5, 3, 6, 7])
    expect(preorderTraversal(null))
      .toStrictEqual([])
    expect(preorderTraversal(TreeNode.fromArray([1, null, 3, null, 2, 5, 7])))
      .toStrictEqual([1, 3, 2, 5, 7])
  })
})
