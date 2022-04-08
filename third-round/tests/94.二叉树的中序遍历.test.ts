import { TreeNode } from '../commons/Tree'
import { inorderTraversal } from '../94.二叉树的中序遍历'

describe('94. Binary Tree Inorder Traversal', () => {
  it('should work', () => {
    expect(inorderTraversal(TreeNode.fromArray([1, 2, 3, 4, 5, 6, 7, 8])))
      .toStrictEqual([8, 4, 2, 5, 1, 6, 3, 7])
    expect(inorderTraversal(null))
      .toStrictEqual([])
    expect(inorderTraversal(TreeNode.fromArray([1, null, 3, null, 2, 5, 7])))
      .toStrictEqual([1, 3, 5, 2, 7])
  })
})
