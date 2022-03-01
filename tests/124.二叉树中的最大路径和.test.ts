import { maxPathSum } from '../124.二叉树中的最大路径和'
import { TreeNode } from '../commons/Tree'

describe('124.二叉树中的最大路径和', () => {
  it('should work', () => {
    expect(maxPathSum(TreeNode.fromArray([1, 2, 3])))
      .toBe(6)
    expect(maxPathSum(TreeNode.fromArray([-10, 9, 20, null, null, 15, 7])))
      .toBe(42)
  })
})
