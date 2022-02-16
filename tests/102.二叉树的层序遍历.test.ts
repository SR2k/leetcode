import { TreeNode } from './commons/Tree'
import { levelOrder } from './102.二叉树的层序遍历'

describe('102. Binary Tree Level Order Traversal', () => {
  it('should work', () => {
    expect(levelOrder(TreeNode.fromArray([3, 9, 20, null, null, 15, 7])))
      .toStrictEqual([[3], [9, 20], [15, 7]])
    expect(levelOrder(TreeNode.fromArray([3, null, 20, 15, 7])))
      .toStrictEqual([[3], [20], [15, 7]])
    expect(levelOrder(null))
      .toStrictEqual([])
  })
})
