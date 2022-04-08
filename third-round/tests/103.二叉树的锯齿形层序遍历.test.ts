import { TreeNode } from '../commons/Tree'
import { zigzagLevelOrder } from '../103.二叉树的锯齿形层序遍历'

describe('103. Binary Tree Zigzag Level Order Traversal', () => {
  it('should work', () => {
    expect(zigzagLevelOrder(TreeNode.fromArray([3, 9, 20, null, null, 15, 7]))).toStrictEqual([[3], [20, 9], [15, 7]])
    expect(zigzagLevelOrder(TreeNode.fromArray([1]))).toStrictEqual([[1]])
    expect(zigzagLevelOrder(TreeNode.fromArray([]))).toStrictEqual([])
  })
})
